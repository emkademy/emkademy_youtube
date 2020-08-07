import cv2


foto = cv2.imread("./foto.png")

# Dogru cizme:
# cv2.line(foto, baslangic_koordinatlari, bitis_koordinatlari, renk, kalinlik)
print(foto.shape)

x_baslangic = 250
y_baslangic = 250

x_bitis = 500
y_bitis = 500

renk = (0, 255, 0)
kalinlik = 4

# cv2.line(foto, baslangic_koordinatlari, bitis_koordinatlari, renk, kalinlik)
cv2.line(foto, (x_baslangic, y_baslangic), (x_bitis, y_bitis), renk, kalinlik)

# Dikdortgen cizme:
# cv2.rectangle(foto, sol_ust_kose, sag_alt_kose, renk, kalinlik)
cv2.rectangle(foto, (x_baslangic, y_baslangic), (x_bitis, y_bitis), (255, 0, 0), kalinlik)

# Ok cizme:
# cv2.arrowedLine(foto, baslangic_koordinatlari, bitis_koordinatlari, renk, kalinlik)
cv2.arrowedLine(foto, (0, 0), (240, 240), (0, 0, 255), kalinlik)

# Yuvarlak cizme:
# cv2.circle(foto, orto_noktasi, yaricap, renk, kalinlik)
# kalinlik = -1 --> ici boyali
cv2.circle(foto, (375, 375), 100, (255, 255, 0), -1)

# Yazi yazma:
# cv2.putText(foto, yazi, sol_alt_kosesi, font, font_buyuklugu, renk, kalinlik)
yazi = "Emkademy - Kivanc Yuksel"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(foto, yazi, (75, 800), font, 2, (0, 0, 255), 5)

cv2.imshow("fotograf", foto)
cv2.waitKey(0)
cv2.destroyAllWindows()






