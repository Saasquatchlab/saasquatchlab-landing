import Foundation
import CoreGraphics
import CoreText
import ImageIO
import UniformTypeIdentifiers

let srgb = CGColorSpace(name: CGColorSpace.sRGB)!
func rgb(_ r: Double,_ g: Double,_ b: Double,_ a: Double = 1) -> CGColor { CGColor(colorSpace: srgb, components: [r/255,g/255,b/255,a])! }
let ground = rgb(5,9,7), ink = rgb(234,241,231), key = rgb(82,183,136), muted = rgb(150,168,157)

func loadImage(_ p: String) -> CGImage {
    let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: p) as CFURL, nil)!
    return CGImageSourceCreateImageAtIndex(src, 0, nil)!
}
func font(_ name: String, _ size: CGFloat) -> CTFont { CTFontCreateWithName(name as CFString, size, nil) }
func draw(_ ctx: CGContext, _ text: String, _ f: CTFont, _ color: CGColor, x: CGFloat, y: CGFloat, maxW: CGFloat, lineH: CGFloat, tracking: CGFloat = 0, center: Bool = false) -> CGFloat {
    // simple greedy wrap; returns total height used
    let attrs: [CFString: Any] = [kCTFontAttributeName: f, kCTForegroundColorAttributeName: color, kCTKernAttributeName: tracking]
    var lines: [String] = []; var cur = ""
    for w in text.split(separator: " ").map(String.init) {
        let t = cur.isEmpty ? w : cur + " " + w
        let l = CTLineCreateWithAttributedString(NSAttributedString(string: t, attributes: attrs as [NSAttributedString.Key: Any]))
        if CTLineGetTypographicBounds(l, nil, nil, nil) > Double(maxW) && !cur.isEmpty { lines.append(cur); cur = w } else { cur = t }
    }
    if !cur.isEmpty { lines.append(cur) }
    var yy = y
    for ln in lines {
        let l = CTLineCreateWithAttributedString(NSAttributedString(string: ln, attributes: attrs as [NSAttributedString.Key: Any]))
        let w = CGFloat(CTLineGetTypographicBounds(l, nil, nil, nil))
        ctx.textPosition = CGPoint(x: center ? x - w/2 : x, y: yy)
        CTLineDraw(l, ctx); yy -= lineH
    }
    return CGFloat(lines.count) * lineH
}
func roundedPath(_ r: CGRect, _ rad: CGFloat) -> CGPath { CGPath(roundedRect: r, cornerWidth: rad, cornerHeight: rad, transform: nil) }

/// Phone mock: crop status bar off the ASC screenshot, draw with device-like rounded corners + thin bezel + shadow.
func phone(_ ctx: CGContext, _ shot: CGImage, in rect: CGRect, radius: CGFloat) {
    let cropTop = 150 // status bar + breadcrumb
    let cropped = shot.cropping(to: CGRect(x: 0, y: cropTop, width: shot.width, height: shot.height - cropTop))!
    ctx.saveGState()
    ctx.setShadow(offset: CGSize(width: 0, height: -18), blur: 60, color: rgb(0,0,0,0.65))
    ctx.setFillColor(rgb(12,18,14)); ctx.addPath(roundedPath(rect.insetBy(dx: -14, dy: -14), radius + 14)); ctx.fillPath()
    ctx.restoreGState()
    ctx.saveGState(); ctx.addPath(roundedPath(rect, radius)); ctx.clip()
    // aspect-fill from the top
    let scale = rect.width / CGFloat(cropped.width)
    let h = CGFloat(cropped.height) * scale
    ctx.draw(cropped, in: CGRect(x: rect.minX, y: rect.maxY - h, width: rect.width, height: h))
    ctx.restoreGState()
    ctx.setStrokeColor(rgb(255,255,255,0.10)); ctx.setLineWidth(2); ctx.addPath(roundedPath(rect, radius)); ctx.strokePath()
}
func background(_ ctx: CGContext, w: CGFloat, h: CGFloat, glowAt: CGPoint) {
    ctx.setFillColor(ground); ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    let g = CGGradient(colorsSpace: srgb, colors: [rgb(82,183,136,0.22), rgb(82,183,136,0.0)] as CFArray, locations: [0,1])!
    ctx.drawRadialGradient(g, startCenter: glowAt, startRadius: 0, endCenter: glowAt, endRadius: max(w,h)*0.75, options: [])
    // faint ridgeline
    ctx.setFillColor(rgb(11,20,15)); let p = CGMutablePath()
    p.move(to: CGPoint(x: 0, y: 0)); p.addLine(to: CGPoint(x: 0, y: h*0.16))
    p.addCurve(to: CGPoint(x: w*0.5, y: h*0.10), control1: CGPoint(x: w*0.18, y: h*0.20), control2: CGPoint(x: w*0.34, y: h*0.06))
    p.addCurve(to: CGPoint(x: w, y: h*0.14), control1: CGPoint(x: w*0.70, y: h*0.16), control2: CGPoint(x: w*0.86, y: h*0.08))
    p.addLine(to: CGPoint(x: w, y: 0)); p.closeSubpath(); ctx.addPath(p); ctx.fillPath()
}
func brand(_ ctx: CGContext, logo: CGImage, x: CGFloat, y: CGFloat, size: CGFloat) {
    ctx.saveGState(); ctx.addPath(roundedPath(CGRect(x: x, y: y, width: size, height: size), size*0.22)); ctx.clip()
    ctx.draw(logo, in: CGRect(x: x, y: y, width: size, height: size)); ctx.restoreGState()
    _ = draw(ctx, "SQUATCH CONNECT", font("HelveticaNeue-Bold", size*0.30), ink, x: x + size + 22, y: y + size*0.52 - size*0.10, maxW: 800, lineH: 40, tracking: 5)
    _ = draw(ctx, "BY SAASQUATCH LAB", font("HelveticaNeue-Medium", size*0.20), muted, x: x + size + 22, y: y + size*0.52 - size*0.42, maxW: 800, lineH: 30, tracking: 4)
}
func save(_ ctx: CGContext, _ path: String) {
    let img = ctx.makeImage()!
    let d = CGImageDestinationCreateWithURL(URL(fileURLWithPath: path) as CFURL, UTType.png.identifier as CFString, 1, nil)!
    CGImageDestinationAddImage(d, img, nil); CGImageDestinationFinalize(d); print("wrote", path)
}
func canvas(_ w: Int, _ h: Int) -> CGContext {
    CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0, space: srgb, bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)!
}


/// Pillar row: green label + one-line proof.
func pillar(_ ctx: CGContext, _ label: String, _ line: String, x: CGFloat, y: CGFloat, maxW: CGFloat, labelSize: CGFloat, lineSize: CGFloat, lineH: CGFloat) -> CGFloat {
    ctx.setFillColor(key); ctx.fill(CGRect(x: x, y: y + labelSize*0.28, width: 34, height: 4))
    _ = draw(ctx, label, font("HelveticaNeue-Bold", labelSize), key, x: x + 52, y: y, maxW: maxW, lineH: labelSize + 8, tracking: 4)
    let used = draw(ctx, line, font("HelveticaNeue", lineSize), ink, x: x, y: y - labelSize - 18, maxW: maxW, lineH: lineH)
    return labelSize + 18 + used + 26
}

let logo = loadImage(NSString(string: "~/saasquatchlab-landing/logo-squatch-connect.png").expandingTildeInPath)
let prices = loadImage("src/01_asc_iphone_2.png")
let privacy = loadImage("src/02_asc_iphone_3.png")

// ---------- FEED 1080x1080: privacy proof on the phone, three pillars in text ----------
do {
    let W: CGFloat = 1080, H: CGFloat = 1080; let ctx = canvas(1080, 1080)
    background(ctx, w: W, h: H, glowAt: CGPoint(x: W*0.80, y: H*0.50))
    brand(ctx, logo: logo, x: 72, y: H - 72 - 84, size: 84)
    var y: CGFloat = H - 292
    _ = draw(ctx, "Private.", font("HelveticaNeue-Bold", 86), ink, x: 72, y: y, maxW: 560, lineH: 92); y -= 92
    _ = draw(ctx, "Easy.", font("HelveticaNeue-Bold", 86), ink, x: 72, y: y, maxW: 560, lineH: 92); y -= 92
    _ = draw(ctx, "Cheap.", font("HelveticaNeue-Bold", 86), key, x: 72, y: y, maxW: 560, lineH: 92); y -= 92 + 30
    y -= pillar(ctx, "PRIVATE", "No account. No tracking. No passport upload.", x: 72, y: y, maxW: 520, labelSize: 22, lineSize: 30, lineH: 38)
    y -= pillar(ctx, "EASY", "Pick a destination, tap once, you're online. Or just ask Siri.", x: 72, y: y, maxW: 520, labelSize: 22, lineSize: 30, lineH: 38)
    y -= pillar(ctx, "CHEAP", "France, 10 GB: $8.99. Carrier day passes cost $10 a day.", x: 72, y: y, maxW: 520, labelSize: 22, lineSize: 30, lineH: 38)
    phone(ctx, privacy, in: CGRect(x: 672, y: -160, width: 380, height: 860), radius: 54)
    save(ctx, "connect-ad-feed.png")
}
// ---------- STORY 1080x1920: price proof on the phone, pillars beneath ----------
do {
    let W: CGFloat = 1080, H: CGFloat = 1920; let ctx = canvas(1080, 1920)
    background(ctx, w: W, h: H, glowAt: CGPoint(x: W*0.5, y: H*0.50))
    brand(ctx, logo: logo, x: 90, y: H - 140 - 96, size: 96)
    var y: CGFloat = H - 350
    y -= draw(ctx, "Private. Easy. Cheap.", font("HelveticaNeue-Bold", 96), ink, x: 90, y: y, maxW: 940, lineH: 104) + 6
    y -= draw(ctx, "The travel eSIM built so there's nothing to sell.", font("HelveticaNeue", 40), muted, x: 90, y: y, maxW: 900, lineH: 52)
    phone(ctx, prices, in: CGRect(x: 240, y: 560, width: 600, height: 780), radius: 84)
    var py: CGFloat = 470
    py -= pillar(ctx, "PRIVATE", "No account, no tracking, no passport upload.", x: 90, y: py, maxW: 900, labelSize: 24, lineSize: 34, lineH: 42)
    py -= pillar(ctx, "EASY", "Pick a destination, tap once, you're online.", x: 90, y: py, maxW: 900, labelSize: 24, lineSize: 34, lineH: 42)
    py -= pillar(ctx, "CHEAP", "From $1.99 — not $10 a day in roaming passes.", x: 90, y: py, maxW: 900, labelSize: 24, lineSize: 34, lineH: 42)
    _ = draw(ctx, "DOWNLOAD ON THE APP STORE", font("HelveticaNeue-Bold", 26), key, x: W/2, y: 60, maxW: 1000, lineH: 34, tracking: 4, center: true)
    save(ctx, "connect-ad-story.png")
}
