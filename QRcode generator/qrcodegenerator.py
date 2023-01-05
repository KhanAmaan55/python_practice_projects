import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 15,
    border = 3
)

# data = "https://www.google.com/search?q=fifa&oq=fifa&aqs=chrome..69i57j69i59l4.1290j0j1&sourceid=chrome&ie=UTF-8"
data = "Ayfaz fazlani"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("Ayfaz.png")