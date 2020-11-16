import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import kernel_olustur, konvolusyon


def main():
    esik_degeri = 125
    foto = cv2.imread("./fotograflar/space.tif", 0)
    orjinal_maske = 255*(foto > esik_degeri).astype(np.uint8)

    sigma = 5
    gauss_kernel = kernel_olustur("gauss", 6*sigma+1, 6*sigma+1, sigma=sigma, K=1)

    cikis_foto = konvolusyon(foto, gauss_kernel)
    cikis_maske = 255*(cikis_foto > esik_degeri).astype(np.uint8)

    foto = cv2.resize(foto, cikis_foto.shape[::-1])
    orjinal_maske = cv2.resize(orjinal_maske, cikis_foto.shape[::-1])
    satir1 = np.hstack((foto, orjinal_maske))
    satir2 = np.hstack((cikis_foto, cikis_maske))

    alt_alta = np.vstack((satir1, satir2))

    plt.imshow(alt_alta, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()

