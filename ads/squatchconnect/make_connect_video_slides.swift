import Foundation
import CoreGraphics
import CoreText
import ImageIO
import UniformTypeIdentifiers
let srgb = CGColorSpace(name: CGColorSpace.sRGB)!
func rgb(_ r: Double,_ g: Double,_ b: Double,_ a: Double = 1) -> CGColor { CGColor(colorSpace: srgb, components: [r/255,g/255,b/255,a])! }
let ground = rgb(5,9,7), ink = rgb(234,241,231), key = rgb(82,183,136), muted = rgb(150,168,157)
func load(_ p: String) -> CGImage { let s = CGImageSourceCreateWithURL(URL(fileURLWithPath: p) as CFURL, nil)!; return CGImageSourceCreateImageAtIndex(s, 0, nil)! }
func font(_ n: String,_ s: CGFloat) -> CTFont { CTFontCreateWithName(n as CFString, s, nil) }
func text(_ ctx: CGContext,_ t: String,_ f: CTFont,_ c: CGColor, x: CGFloat, y: CGFloat, tracking: CGFloat = 0, center: Bool = false) {
    let a: [CFString: Any] = [kCTFontAttributeName: f, kCTForegroundColorAttributeName: c, kCTKernAttributeName: tracking]
    let l = CTLineCreateWithAttributedString(NSAttributedString(string: t, attributes: a as [NSAttributedString.Key: Any]))
    let w = CGFloat(CTLineGetTypographicBounds(l, nil, nil, nil))
    ctx.textPosition = CGPoint(x: center ? x - w/2 : x, y: y); CTLineDraw(l, ctx)
}
func rounded(_ r: CGRect,_ rad: CGFloat) -> CGPath { CGPath(roundedRect: r, cornerWidth: rad, cornerHeight: rad, transform: nil) }
func slide(_ src: String,_ out: String,_ label: String,_ line1: String,_ line2: String) {
    let W: CGFloat = 1080, H: CGFloat = 1920
    let ctx = CGContext(data: nil, width: 1080, height: 1920, bitsPerComponent: 8, bytesPerRow: 0, space: srgb, bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)!
    ctx.setFillColor(ground); ctx.fill(CGRect(x: 0, y: 0, width: W, height: H))
    let g = CGGradient(colorsSpace: srgb, colors: [rgb(82,183,136,0.20), rgb(82,183,136,0)] as CFArray, locations: [0,1])!
    ctx.drawRadialGradient(g, startCenter: CGPoint(x: W*0.5, y: H*0.45), startRadius: 0, endCenter: CGPoint(x: W*0.5, y: H*0.45), endRadius: H*0.7, options: [])
    let logo = load(NSString(string: "~/saasquatchlab-landing/logo-squatch-connect.png").expandingTildeInPath)
    ctx.saveGState(); ctx.addPath(rounded(CGRect(x: 90, y: H-150-80, width: 80, height: 80), 18)); ctx.clip(); ctx.draw(logo, in: CGRect(x: 90, y: H-150-80, width: 80, height: 80)); ctx.restoreGState()
    text(ctx, "SQUATCH CONNECT", font("HelveticaNeue-Bold", 26), ink, x: 190, y: H-150-46, tracking: 5)
    ctx.setFillColor(key); ctx.fill(CGRect(x: 90, y: H-330, width: 40, height: 5))
    text(ctx, label, font("HelveticaNeue-Bold", 30), key, x: 146, y: H-338, tracking: 5)
    text(ctx, line1, font("HelveticaNeue-Bold", 84), ink, x: 90, y: H-440)
    text(ctx, line2, font("HelveticaNeue-Bold", 84), key, x: 90, y: H-540)
    let shot = load(src); let crop = shot.cropping(to: CGRect(x: 0, y: 150, width: shot.width, height: shot.height-150))!
    let r = CGRect(x: 150, y: 120, width: 780, height: 1180)
    ctx.saveGState(); ctx.setShadow(offset: CGSize(width: 0, height: -18), blur: 60, color: rgb(0,0,0,0.65)); ctx.setFillColor(rgb(12,18,14)); ctx.addPath(rounded(r.insetBy(dx: -14, dy: -14), 104)); ctx.fillPath(); ctx.restoreGState()
    ctx.saveGState(); ctx.addPath(rounded(r, 90)); ctx.clip()
    let sc = r.width / CGFloat(crop.width); let h = CGFloat(crop.height) * sc
    ctx.draw(crop, in: CGRect(x: r.minX, y: r.maxY - h, width: r.width, height: h)); ctx.restoreGState()
    text(ctx, "DOWNLOAD ON THE APP STORE", font("HelveticaNeue-Bold", 26), key, x: W/2, y: 60, tracking: 4, center: true)
    let img = ctx.makeImage()!; let d = CGImageDestinationCreateWithURL(URL(fileURLWithPath: out) as CFURL, UTType.png.identifier as CFString, 1, nil)!
    CGImageDestinationAddImage(d, img, nil); CGImageDestinationFinalize(d); print("wrote", out)
}
slide("../src/00_asc_iphone_1.png", "s2.png", "EASY", "Pick a destination.", "Tap once.")
slide("../src/01_asc_iphone_2.png", "s3.png", "CHEAP", "France, 10 GB.", "$8.99.")
slide("../src/02_asc_iphone_3.png", "s4.png", "PRIVATE", "No account.", "Nothing to sell.")
