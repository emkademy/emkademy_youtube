import matplotlib.pyplot as plt
import numpy as np


def kutu_kernel_olustur(m, n, deger):
    kernel = np.full((m, n), deger)
    return kernel / kernel.sum()


def gauss_kernel_olustur(m, n, sigma, K):
    kernel = np.empty((m, n))

    yarim_m = m // 2
    yarim_n = n // 2
    for s in range(-yarim_m, yarim_m+1):
        for t in range(-yarim_n, yarim_n+1):
            r_kare = s**2 + t**2
            kernel[yarim_m+s, yarim_n+t] = K*np.exp(-(r_kare/(2*sigma**2)))
    return kernel / kernel.sum()


def kernel_olustur(tip, m, n, **kwargs):
    if tip == "kutu":
        return kutu_kernel_olustur(m, n, **kwargs)
    elif tip == "gauss":
        return gauss_kernel_olustur(m, n, **kwargs)
    else:
        raise RuntimeError("Bilinmeyen filtre tipi: {tip}. 'kutu' veya 'gauss' olmali.")


def filtrele(giris, kernel_yada_pencere, yapilacak_islem):
    m, n = kernel_yada_pencere.shape
    yarim_m = m // 2
    yarim_n = n // 2
    
    sifir_kaplanmis_giris = np.pad(giris, ((yarim_m, yarim_m), (yarim_n, yarim_n)), constant_values=((0, 0), (0, 0)))
    sifir_kaplanmis_giris = sifir_kaplanmis_giris.astype(float)
    M, N = sifir_kaplanmis_giris.shape

    cikis = np.zeros_like(sifir_kaplanmis_giris)
    for satir in range(yarim_m, M-yarim_m):
        for sutun in range(yarim_n, N-yarim_n):
            giris_pencere = sifir_kaplanmis_giris[satir-yarim_m:satir+yarim_m+1, sutun-yarim_n:sutun+yarim_n+1]
            cikis[satir, sutun] = yapilacak_islem(giris_pencere, kernel_yada_pencere)
    return cikis.astype(np.uint8)


def korelasyon(giris, kernel):
    yapilacak_islem = lambda giris_pencere, kernel_pencere: (giris_pencere * kernel_pencere).sum()
    return filtrele(giris, kernel, yapilacak_islem)


def konvolusyon(giris, kernel):
    kernel = np.fliplr(kernel)
    kernel = np.flipud(kernel)
    return korelasyon(giris, kernel)


def median_filtreleme(giris, m, n):
    bos_pencere = np.empty((m, n))
    yapilacak_islem = lambda giris_pencere, _: np.median(giris_pencere)
    return filtrele(giris, bos_pencere, yapilacak_islem)


