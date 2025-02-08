import qrcode
from qrcode import QRCode
import qrcode.constants
import cv2 as cv
from datetime import datetime as t
import os 

base_dir = os.path.abspath(__file__)
def employee_qr(name: str,  id_number):
    time_in = t.now().strftime("%Y-%m-%d %H:%M:%S")
    name = name.replace(" ", "_") .lower()
    qr = QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=5)
    qr.add_data(f"Name: {name}\nID: {id_number} \nTime In: {time_in}")
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'{name}-{id_number}.png')
    return img


if __name__ == "__main__":
    employee_qr("John Doe", "123456789")
    employee_qr("Jane Doe", "987654321")
    employee_qr("John Smith", "123456789")
    employee_qr("JHay 123123", "987654321")
    employee_qr("John Smith", "0")

    