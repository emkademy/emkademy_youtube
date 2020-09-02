import cv2
import matplotlib.pyplot as plt
import numpy as np



def cv2_main():
    foto = cv2.imread("./fotograflar/acik.tif", 0)
    hist_es_foto = cv2.equalizeHist(foto)

    yanyana = np.hstack((foto, hist_es_foto))

    plt.imshow(yanyana, cmap="gray")
    plt.show()


def fotografin_histogramini_olustur(foto, L):
    histogram, bins = np.histogram(foto, bins=L, range=(0, L))
    return histogram


def normallestirilmis_histogram_olustur(foto, L):
    histogram = fotografin_histogramini_olustur(foto, L)
    return histogram / foto.size # foto.size = M*N


def kumulatif_dagilimi_olustur(p_r_r):
    return np.cumsum(p_r_r)


def histogram_esitleme(foto, L):
    p_r_r = normallestirilmis_histogram_olustur(foto, L)
    kumulatif_dagilim = kumulatif_dagilimi_olustur(p_r_r)
    donusum_fonksiyonu = (L-1) * kumulatif_dagilim
    shape = foto.shape
    ravel = foto.ravel() # (800x600) -> 480000
    hist_es_foto = np.zeros_like(ravel)
    for i, pixel in enumerate(ravel):
        hist_es_foto[i] = donusum_fonksiyonu[pixel]
    return hist_es_foto.reshape(shape).astype(np.uint8)


def main():
    L = 2**8
    acik = cv2.imread("./fotograflar/acik.tif", 0)
    koyu = cv2.imread("./fotograflar/koyu.tif", 0)
    grimsi = cv2.imread("./fotograflar/grimsi.tif", 0)

    hist_es_acik = histogram_esitleme(acik, L)
    hist_es_koyu = histogram_esitleme(koyu, L)
    hist_es_grimsi = histogram_esitleme(grimsi, L)

    yanyana_acik = np.hstack((acik, hist_es_acik))
    yanyana_koyu = np.hstack((koyu, hist_es_koyu))
    yanyana_grimsi = np.hstack((grimsi, hist_es_grimsi))

    grid = np.vstack((yanyana_acik, yanyana_koyu, yanyana_grimsi))

    plt.imshow(grid, cmap="gray")
    plt.show()


if __name__ == "__main__":
    # cv2_main()
    main()
