import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import rescale, stack


def kuvvet_donusumu(r, c, gamma):
    r = r.astype(float)
    s = c*r**gamma
    s = rescale(s)
    return s


# foto = cv2.imread("./fotograflar/mri.tif", 0)
# c = 1
# gamma_degerler = [0.6, 0.4, 0.3]
# kuvvet_fotograflari = []
# for gamma in gamma_degerler:
#     kuvvet_foto = kuvvet_donusumu(foto, c=c, gamma=gamma)
#     kuvvet_fotograflari.append(kuvvet_foto)
# 
# satir1 = stack(foto, kuvvet_fotograflari[0])
# satir2 = stack(*kuvvet_fotograflari[1:])
# 
# grid = np.vstack((satir1, satir2))
# 
# plt.imshow(grid, cmap="gray")
# plt.show()

foto = cv2.imread("./fotograflar/sehir.tif")
c = 1
gamma_degerleri = [3, 4, 5]
kuvvet_fotolari = []
for gamma in gamma_degerleri:
    kuvvet_foto = kuvvet_donusumu(foto, c=c, gamma=gamma)
    kuvvet_fotolari.append(kuvvet_foto)


satir1 = stack(foto, kuvvet_fotolari[0])
satir2 = stack(*kuvvet_fotolari[1:])

grid = np.vstack((satir1, satir2))


plt.imshow(grid, cmap="gray")
plt.show()
