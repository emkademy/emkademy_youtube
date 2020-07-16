import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import stack, rescale


def binary_dilimleme(foto, A, B, alt_deger, ust_deger):
    foto_cikis = np.full_like(foto, alt_deger)
    index = np.logical_and(foto>A, foto<B)
    foto_cikis[index] = ust_deger
    return foto_cikis


def linear_dilimleme(foto, A, B, deger):
    foto_cikis = foto.copy()
    index = np.logical_and(foto>A, foto<B)
    foto_cikis[index] = deger
    return foto_cikis


foto = cv2.imread("./fotograflar/aortic_angiogram.tif")

A = 150
B = 200
alt_deger = 10
ust_deger = 255

binary_foto = binary_dilimleme(foto, A, B, alt_deger, ust_deger)
linear_foto = linear_dilimleme(foto, A, B, ust_deger)


yan_yana = stack(foto, binary_foto, linear_foto)


plt.imshow(yan_yana, cmap="gray")
plt.show()

