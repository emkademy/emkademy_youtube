import cv2
import dlib

from src.video_okuyucu import VideoOkuyucu
from src.utils import fotoya_ciz


def main():
    video_okuyucu = VideoOkuyucu(0)

    model = dlib.get_frontal_face_detector()

    for frame in video_okuyucu:
        yuzler = model(frame, 1)
        yuzler = [(yuz.left(), yuz.top(), yuz.right(), yuz.bottom()) for yuz in yuzler]

        for kutu in yuzler:
            fotoya_ciz(frame, kutu)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


if __name__ == "__main__":
    main()
