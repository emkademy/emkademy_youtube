import cv2
from facenet_pytorch import MTCNN

from src.video_okuyucu import VideoOkuyucu
from src.utils import fotoya_ciz


def main():
    video_okuyucu = VideoOkuyucu(0)

    model = MTCNN(image_size=300, margin=0, min_face_size=40,
                  thresholds=[0.6, 0.7, 0.7], factor=0.709,
                  post_process=True)

    for frame in video_okuyucu:
        yuzler, olasiliklar, butun_yuz_noktalari = model.detect(frame, landmarks=True)
        if yuzler is not None:
            for kutu, olasilik, yuz_noktalari in zip(yuzler, olasiliklar, butun_yuz_noktalari):
                fotoya_ciz(frame, kutu, f"{olasilik:.2f}", yuz_noktalari)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


if __name__ == "__main__":
    main()
