import cv2
import dlib

from src.video_okuyucu import VideoOkuyucu
from src.utils import fotoya_ciz


def main():
    video_okuyucu = VideoOkuyucu(0)

    model_path = "./modeller/mmod_human_face_detector.dat"
    model = dlib.cnn_face_detection_model_v1(model_path)

    for frame in video_okuyucu:
        yuzler = model(frame, 1)
        guven_skorlari = [yuz.confidence for yuz in yuzler]
        yuzler = [(yuz.rect.left(), yuz.rect.top(), yuz.rect.right(), yuz.rect.bottom()) for yuz in yuzler]

        for kutu, guven_skoru in zip(yuzler, guven_skorlari):
            fotoya_ciz(frame, kutu, f"{guven_skoru:.2f}")

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


if __name__ == "__main__":
    main()
