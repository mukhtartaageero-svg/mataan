import qrcode

img = qrcode.make("MATAAN_USER_001")

img.save("static/qr/test.png")

print("QR Created ✅")
