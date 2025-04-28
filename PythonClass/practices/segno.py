from pyzbar.pyzbar import decode
import segno
from PIL import Image


def generate_qr_code(menu_text, filename):
    qr = segno.make(menu_text.strip())
    qr.save(filename)
    print("QR code generated successfully")


def scan_qr_code(filename):
    img = Image.open(filename)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        return data
    return None  # In case nothing is found


if __name__ == "__main__":
    menu_texts = "Dynamites"
    generate_qr_code(menu_texts, "dynamites.png")

    scanned_data = scan_qr_code("dynamites.png")
    if scanned_data:
        print("Scanned QR Code Data:", scanned_data)
    else:
        print("No QR code detected.")