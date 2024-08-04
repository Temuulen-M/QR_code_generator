import qrcode

def generate_qr(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(file_name)


def main():
    data = input("QR code data:")
    generate_qr(data, "generated qr code.png")

if __name__ == "__main__":
    main()