import qrcode
import qrcode.constants

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrimage.png")

generate_qrcode("https://github.com/adilmrcodeaz")