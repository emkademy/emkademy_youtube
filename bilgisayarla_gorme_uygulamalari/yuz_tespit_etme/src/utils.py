import cv2


def fotoya_ciz(frame, kutu, text=None, yuz_noktalari=None): # (xmin, ymin, xmax, ymax) -> (12.13, 20.15,...)
    xmin, ymin, xmax, ymax = list(map(int, kutu))
    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    if text is not None:
        cv2.putText(frame, text, (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if yuz_noktalari is not None:
        for n in yuz_noktalari:
            nx, ny = list(map(int, n))
            cv2.circle(frame, (nx, ny), 2, (0, 255, 0), -1)
