import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import kernel_olustur, konvolusyon, median_filtreleme


if __name__ == "__main__":
    foto = cv2.imread("./fotograflar/salt_and_pepper.tif", 0)

    gauss_kernel_sigmalari = [1, 3, 5]

    gauss_cikis_konvolusyon = []
    for sigma in gauss_kernel_sigmalari:
        gauss_kernel = kernel_olustur("gauss", 6*sigma+1, 6*sigma+1, sigma=sigma, K=1)
        gauss_cikis_konvolusyon.append(konvolusyon(foto, gauss_kernel))


    median_filtre_boyutlari = [3, 5, 7]
    median_cikis = []
    for m in median_filtre_boyutlari:
        median_cikis.append(median_filtreleme(foto, m, m))


    gauss_konvolusyon_yanyana = np.hstack([cv2.resize(cikis, (448, 448)) for cikis in [foto, *gauss_cikis_konvolusyon]])
    median_yanyana = np.hstack([cv2.resize(cikis, (448, 448)) for cikis in [foto, *median_cikis]])
    
    altalta = np.vstack((gauss_konvolusyon_yanyana, median_yanyana))
    plt.imshow(altalta, cmap="gray")
    plt.show()

