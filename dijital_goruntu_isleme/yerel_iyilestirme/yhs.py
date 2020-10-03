import cv2
import numpy as np
import matplotlib.pyplot as plt


def yerel_iyilestirme(foto, cerceve_buyuklugu, k0, k1, k2, k3, C):
    foto = foto.astype(float)
    foto_ortalamasi = np.mean(foto)
    ortalama_alt_sinir = k0 * foto_ortalamasi
    ortalama_ust_sinir = k1 * foto_ortalamasi

    foto_sts = np.std(foto)
    sts_alt_sinir = k2 * foto_sts
    sts_ust_sinir = k3 * foto_sts

    M, N = foto.shape[:2]

    sutun_indexleri = []
    satir_indexleri = []
    cerceve_buyuklugu = int(cerceve_buyuklugu/2)
    for sutun in range(M):
        alt = max(0, sutun-cerceve_buyuklugu)
        ust = min(N, sutun+cerceve_buyuklugu+1)
        for satir in range(N):
            sol = max(0, satir-cerceve_buyuklugu)
            sag = min(M, satir+cerceve_buyuklugu+1)

            pencere = foto[alt:ust, sol:sag]
            pencere_ortalamasi = np.mean(pencere)
            pencere_sts = np.std(pencere)

            ortalama_kosulu = ortalama_alt_sinir <= pencere_ortalamasi and pencere_ortalamasi <= ortalama_ust_sinir
            sts_kosulu = sts_alt_sinir <= pencere_sts and pencere_sts <= sts_ust_sinir
            if ortalama_kosulu and sts_kosulu:
                sutun_indexleri.extend(list(range(alt, ust)))
                satir_indexleri.extend(list(range(sol, sag)))

    sutun_indexleri = np.uint32(sutun_indexleri)
    satir_indexleri = np.uint32(satir_indexleri)
    foto[sutun_indexleri, satir_indexleri] *= C

    return foto.astype(np.uint8)


def main():
    foto = cv2.imread("./fotograflar/1.tif")
    cv2.imwrite("original.png", foto)

    cerceve_buyuklugu = 3
    foto = yerel_iyilestirme(foto, cerceve_buyuklugu, k0=0, k1=0.1, k2=0, k3=0.1, C=22.8)
    plt.imshow(foto)
    plt.show()
    cv2.imwrite("output.png", foto)


if __name__ == "__main__":
    main()
