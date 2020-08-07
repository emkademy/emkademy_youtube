import cv2


# cv2.VideoCapture(video konumu ve ya camera id)
cap = cv2.VideoCapture("./videolar/ordered_dict.mp4")


while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("frameler", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

