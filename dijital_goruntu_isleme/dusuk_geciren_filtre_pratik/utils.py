import numpy as np


def kutu_kernel_olustur(m, n, deger):
    kutu_filtre = np.full((m, n), deger)
    return kutu_filtre / kutu_filtre.sum()


def gauss_kernel_olustur(m, n, K, sigma):
    yarim_m = m // 2
    yarim_n = n // 2

    gauss_filtre = np.empty((m, n))
    for s in range(-yarim_m, yarim_m+1):
        for t in range(-yarim_n, yarim_n+1):
            r_kare = s**2 + t**2
            payda = 2 * sigma**2
            kuvvet = -(r_kare / payda)
            deger = K * np.exp(kuvvet)

            python_s = yarim_m + s
            python_t = yarim_n + t

            gauss_filtre[python_s, python_t] = deger
    return gauss_filtre / gauss_filtre.sum()


def filtrele(giris, kernel_yada_filtre, yapilacak_islem):
    m, n = kernel_yada_filtre.shape 

    yarim_m = m // 2
    yarim_n = n // 2

    sifir_eklenmis_giris = np.pad(
        giris, 
        ((yarim_m, yarim_m), (yarim_n, yarim_n)),
        constant_values=((0, 0), (0, 0))
    )
    
    sifir_eklenmis_giris = sifir_eklenmis_giris.astype(float)
    M, N = sifir_eklenmis_giris.shape[:2]

    cikis_foto = np.zeros_like(sifir_eklenmis_giris)

    for satir in range(yarim_m, M-yarim_m):
        for sutun in range(yarim_n, N-yarim_n):
            giris_pencere = sifir_eklenmis_giris[satir-yarim_m:satir+yarim_m+1, sutun-yarim_n:sutun+yarim_n+1]
            cikis_foto[satir, sutun] = yapilacak_islem(giris_pencere, kernel_yada_filtre)
    return cikis_foto.astype(np.uint8)
    

def korelasyon(giris, kernel):
    yapilacak_islem = lambda giris_pencere, kernel: (giris_pencere * kernel).sum()
    return filtrele(giris, kernel, yapilacak_islem)


def konvolusyon(giris, kernel):
    kernel = np.fliplr(kernel)
    kernel = np.flipud(kernel)
    return korelasyon(giris, kernel)


def medyan_filtre(giris, m, n):
    bos_filtre = np.empty((m, n))
    yapilacak_islem = lambda giris_pencere, kernel: np.median(giris_pencere)
    return filtrele(giris, bos_filtre, yapilacak_islem)
    
