import cv2


class VideoOkuyucu:
    def __init__(self, video_konumu): # 0, 1 
        self.cap = cv2.VideoCapture(video_konumu)

    def __next__(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.release()
            raise StopIteration
        return frame

    def __iter__(self):
        return self

