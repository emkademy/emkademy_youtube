import cv2


# cv2.imread(fotografin_konumu)
fotograf = cv2.imread("./foto.png")

print(type(fotograf))
print(fotograf.shape)

cv2.imshow("Python opencv dersleri", fotograf)
cv2.waitKey(0)
cv2.destroyAllWindows()
