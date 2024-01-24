import qrcode 

Qr = input("Name & Number:")

img = qrcode.make(Qr)
img.save("info.png")
