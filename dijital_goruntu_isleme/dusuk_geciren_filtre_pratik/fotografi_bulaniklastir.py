
import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import korelasyon, konvolusyon, kutu_kernel_olustur, gauss_kernel_olustur


def main():
    foto = cv2.imread("./fotograflar/celeba.jpg", 0)

    kutu_filtre_boyutlari = [11, 21, 31]
    kutu_cikis_korelasyon = []
    kutu_cikis_konvolusyon = []
    for kutu_filtre_boyutu in kutu_filtre_boyutlari:
        kutu_filtre = kutu_kernel_olustur(kutu_filtre_boyutu, kutu_filtre_boyutu, deger=1)

        kutu_cikis_korelasyon.append(korelasyon(foto, kutu_filtre))
        kutu_cikis_konvolusyon.append(konvolusyon(foto, kutu_filtre))

    gauss_kernel_sigmalari = [3, 6, 9]
    gauss_cikis_korelasyon = []
    gauss_cikis_konvolusyon = []
    for sigma in gauss_kernel_sigmalari:
        m = n = 6 * sigma + 1
        gauss_kernel = gauss_kernel_olustur(m, n, K=1, sigma=sigma)

        gauss_cikis_korelasyon.append(korelasyon(foto, gauss_kernel))
        gauss_cikis_konvolusyon.append(konvolusyon(foto, gauss_kernel))


    foto_boyutu = (448, 448)

    ilk_sira = np.hstack([cv2.resize(cikis, foto_boyutu) for cikis in [foto, *kutu_cikis_korelasyon]])
    ikinci_sira = np.hstack([cv2.resize(cikis, foto_boyutu) for cikis in [foto, *kutu_cikis_konvolusyon]])

    ucuncu_sira = np.hstack([cv2.resize(cikis, foto_boyutu) for cikis in [foto, *gauss_cikis_korelasyon]])
    dorduncu_sira = np.hstack([cv2.resize(cikis, foto_boyutu) for cikis in [foto, *gauss_cikis_konvolusyon]])

    altalta = np.vstack((ilk_sira, ikinci_sira, ucuncu_sira, dorduncu_sira))

    plt.imshow(altalta, cmap="gray")
    plt.show()




if __name__ == "__main__":
    main()
