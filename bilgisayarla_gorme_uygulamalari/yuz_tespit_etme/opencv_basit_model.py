import cv2

from src.video_okuyucu import VideoOkuyucu
from src.utils import fotoya_ciz


def main():
    video_okuyucu = VideoOkuyucu(0)

    model_path = "./modeller/haarcascade_frontalface_default.xml"
    model = cv2.CascadeClassifier(model_path)

    for frame in video_okuyucu:
        siyah_beyaz = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Siyah beyaza donustur
        siyah_beyaz = cv2.equalizeHist(siyah_beyaz)
        yuzler = model.detectMultiScale(siyah_beyaz) # [(xmin, ymin, genislik, yukseklik), ....]
        yuzler = [(xmin, ymin, xmin+genislik, ymin+yukseklik) for xmin, ymin, genislik, yukseklik in yuzler]

        for kutu in yuzler:
            fotoya_ciz(frame, kutu)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


if __name__ == "__main__":
    main()
