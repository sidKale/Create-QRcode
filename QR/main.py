import qrcode

def generate_qr(data,image_name="QR.png"):
    image=qrcode.make(data)
    image.save(image_name)
    return image

qr_url="https://github.com/sidKale"
generate_qr(qr_url)


