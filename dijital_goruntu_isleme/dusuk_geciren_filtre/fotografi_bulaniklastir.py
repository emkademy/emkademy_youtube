import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import kernel_olustur, korelasyon, konvolusyon


def main():
    foto = cv2.imread("./fotograflar/celeba.jpg", 0)

    kutu_kernel_boyutlari = [11, 21, 31]

    kutu_cikis_korelasyon = []
    kutu_cikis_konvolusyon = []
    for m in kutu_kernel_boyutlari:
        kutu_kernel = kernel_olustur("kutu", m, m, deger=1)
        kutu_cikis_korelasyon.append(korelasyon(foto, kutu_kernel))
        kutu_cikis_konvolusyon.append(konvolusyon(foto, kutu_kernel))

    gauss_kernel_sigmalari = [3, 6, 9]

    gauss_cikis_korelasyon = []
    gauss_cikis_konvolusyon = []
    for sigma in gauss_kernel_sigmalari:
        gauss_kernel = kernel_olustur("gauss", 6*sigma+1, 6*sigma+1, sigma=sigma, K=1)
        gauss_cikis_korelasyon.append(korelasyon(foto, gauss_kernel))
        gauss_cikis_konvolusyon.append(konvolusyon(foto, gauss_kernel))


    kutu_korelasyon_yanyana = np.hstack([cv2.resize(cikis, (448, 448)) for cikis in [foto, *kutu_cikis_korelasyon]])
    kutu_konvolusyon_yanyana = np.hstack([cv2.resize(cikis, (448, 448)) for cikis in [foto, *kutu_cikis_konvolusyon]])

    gauss_korelasyon_yanyana = np.hstack([cv2.resize(cikis, (448, 448)) for cikis in [foto, *gauss_cikis_korelasyon]])
    gauss_konvolusyon_yanyana = np.hstack([cv2.resize(cikis, (448, 448)) for cikis in [foto, *gauss_cikis_konvolusyon]])
    
    altalta = np.vstack((kutu_korelasyon_yanyana, kutu_konvolusyon_yanyana, gauss_korelasyon_yanyana, gauss_konvolusyon_yanyana))
    plt.imshow(altalta, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()

