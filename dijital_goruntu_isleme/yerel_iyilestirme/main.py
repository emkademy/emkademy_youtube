import cv2
import numpy as np
import matplotlib.pyplot as plt


def yerel_histogram_istatistikleri(foto, pencere_boyutu, k0, k1, k2, k3, C):
    foto = foto.astype(float)
    ortalama_global = np.mean(foto)
    ortalama_alt_sinir = k0 * ortalama_global
    ortalama_ust_sinir = k1 * ortalama_global
    # 1. yontem
    standart_sapma_global = np.std(foto) # Standart sapma
    ss_alt_sinir = k2 * standart_sapma_global
    ss_ust_sinir = k3 * standart_sapma_global
    # 2. yontem
    # varyans_global = np.var(foto) # Varyans
    # standart_sapma_global = np.sqrt(varyans_global)
    pencere_boyutu = int(pencere_boyutu / 2)
    M, N = foto.shape[:2] # (800, 600, 3)

    satir_indeksleri = []
    sutun_indeksleri = []
    for satir in range(M):
        ust = max(0, satir - pencere_boyutu)
        alt = min(M, satir + pencere_boyutu + 1)
        for sutun in range(N):
            sol = max(0, sutun - pencere_boyutu)
            sag = min(N, sutun + pencere_boyutu + 1)

            pencere_pixelleri = foto[ust:alt, sol:sag]
            ortalama_pencere = np.mean(pencere_pixelleri)
            standart_sapma_pencere = np.std(pencere_pixelleri)
            # print(f"SATIR: {satir}, SUTUN: {sutun}")
            # print(pencere_pixelleri)
            # print(60*"-")

            ortalama_kosulu = ortalama_alt_sinir <= ortalama_pencere and ortalama_pencere <= ortalama_ust_sinir
            ss_kosulu = ss_alt_sinir <= standart_sapma_pencere and standart_sapma_pencere <= ss_ust_sinir
            kosul = ortalama_kosulu and ss_kosulu

            if kosul:
                satir_indeksleri.extend(list(range(sol, sag)))
                sutun_indeksleri.extend(list(range(ust, alt)))

    satir_indeksleri = np.uint32(satir_indeksleri)
    sutun_indeksleri = np.uint32(sutun_indeksleri)

    foto[sutun_indeksleri, satir_indeksleri] *= C
    return foto.astype(np.uint8)


def main():
    foto = cv2.imread("./fotograflar/1.tif", 0)

    # ornek = np.uint8([[10, 20, 30, 40, 50],
    #                   [ 5, 15, 25, 35, 45],
    #                   [20, 30, 40, 50, 60],
    #                   [15, 25, 35, 45, 55],
    #                   [ 0, 10, 20, 30, 40]])

    # print(ornek)
    # print(ornek.shape)

    pencere_boyutu = 3
    k0 = 0
    k1 = 0.1
    k2 = 0
    k3 = 0.1
    C = 23
    foto2 = yerel_histogram_istatistikleri(foto, pencere_boyutu, k0, k1, k2, k3, C)

    yan_yana = np.hstack((foto, foto2))

    plt.imshow(yan_yana, cmap="gray")
    plt.show()




if __name__ == "__main__":
    main()
