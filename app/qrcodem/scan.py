import cv2
# from pyzbar.pyzbar import decode
from openpyxl import Workbook, load_workbook
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise Exception("Could not open camera")


while True:
    ret, frame = cam.read()
    # frame.resize(600, 600)
    if not ret:
        print("failed to grab frame")
    middle = (frame.shape[1] // 2, frame.shape[0] // 2)
    
    # rect = cv2.rectangle(frame, (frame.shape[1] // 2, frame.shape[0] // 2), ((frame.shape[1] // 2 ) , (frame.shape[0] // 2) ), (0, 0, 0), 2)
    rect = cv2.flip(cv2.rectangle(frame, (frame.shape[1] // 2  , frame.shape[0] // 2 ), (middle[0] + 150, middle[1] + 150), (0, 255, 0), 2), 1)
    cv2.imshow("QR Code Scanner", rect)
    if cv2.waitKey(1) & 0xFF == ord('q')  or cv2.waitKey(1) & 0xFF == ord('Q'):
        break
cv2.waitKey(0)