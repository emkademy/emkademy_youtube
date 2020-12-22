import cv2
import numpy as np

from src.video_okuyucu import VideoOkuyucu
from src.utils import fotoya_ciz


def main():
    video_okuyucu = VideoOkuyucu(0)

    model_path = "./modeller/opencv_dnn_model.caffemodel"
    model_config = "./modeller/opencv_dnn_model.prototxt"
    model = cv2.dnn.readNetFromCaffe(model_config, model_path)
    esik_degeri = 0.7

    foto_boyutu = (300, 300)
    for frame in video_okuyucu:
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, foto_boyutu), 1.0, foto_boyutu, [104.0, 117.0, 123.0])
        model.setInput(blob)
        yuzler = model.forward().squeeze()[:, 2:] # array.shape = [1, ?, 7] -> squeeze -> [15, 7]
        # [(olasilik, xmin, ymin, xmax, ymax), (olasilik, xmin, ymin, xmax, ymax), ...]
        yuzler = yuzler[yuzler[:, 0] > esik_degeri]

        olasiliklar, yuzler = yuzler[:, 0], yuzler[:, 1:]
        # yuzler =  [(xmin, ymin, xmax, ymax), ....] -> 0-1
        frame_boy, frame_en = frame.shape[:2]
        yuzler *= np.array([frame_en, frame_boy, frame_en, frame_boy])

        for kutu, olasilik in zip(yuzler, olasiliklar):
            fotoya_ciz(frame, kutu, f"{olasilik:.2f}")

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


if __name__ == "__main__":
    main()
