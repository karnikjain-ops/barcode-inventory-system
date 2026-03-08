import cv2
from pyzbar.pyzbar import decode

video = cv2.VideoCapture(0)
bit =0
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

while True:
    ret, frame = video.read()

    if not ret:
        print("Camera frame not received")
        break

    cv2.imshow("frame", frame)

    numer = decode(frame)

    if numer:
        first_barcode_data = numer[0].data.decode("utf-8")
        print(first_barcode_data)
        bit=bit+1
        print(bit)



    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

video.release()
cv2.destroyAllWindows()