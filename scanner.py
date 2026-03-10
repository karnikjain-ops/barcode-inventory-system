import cv2
from pyzbar.pyzbar import decode
def scanner():
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

    while True:
        ret, frame = video.read()

        if not ret:
            print("Camera frame not received")
            break

        cv2.imshow("frame", frame)

        number = decode(frame)

        if number:
            first_barcode_data = number[0].data.decode("utf-8")
            video.release()
            cv2.destroyAllWindows()
            return first_barcode_data




        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    video.release()
    cv2.destroyAllWindows()