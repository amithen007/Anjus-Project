import qrcode

def generate_qr_code(link, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
generate_qr_code("http://your-app-domain.com/track", "tracking_qr.png")
print("QR Code generated: tracking_qr.png")
