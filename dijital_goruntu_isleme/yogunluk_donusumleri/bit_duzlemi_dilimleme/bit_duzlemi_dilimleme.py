import cv2
import matplotlib.pyplot as plt
import numpy as np


def stack(*args):
    return np.hstack(args)


def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)


# 0 <= bit_duzlemi <= 7
def bit_duzlemi_dilimleme(foto, bit_duzlemi):
    bit_foto = np.full_like(foto, 2**bit_duzlemi)
    return np.bitwise_and(foto, bit_foto)


def foto_sikistirma(foto, bit_duzlemleri):
    sikistirilmis_foto = np.zeros_like(foto)
    for bit_duzlemi in bit_duzlemleri:
        sikistirilmis_foto += bit_duzlemi_dilimleme(foto, bit_duzlemi)
    return sikistirilmis_foto


def main():
    foto = cv2.imread("./fotograflar/1.png", 0)

    bit_duzlemleri = []
    for bit_duzlemi in range(8):
        bit_foto = bit_duzlemi_dilimleme(foto, bit_duzlemi)
        print("bit duzlemi: ", bit_duzlemi+1, "essiz degerler: ", np.unique(bit_foto))
        bit_foto = rescale(bit_foto)
        bit_duzlemleri.append(bit_foto)

    bit_duzlemleri = bit_duzlemleri[::-1]

    satir1 = stack(foto, bit_duzlemleri[0], bit_duzlemleri[1])
    satir2 = stack(bit_duzlemleri[2], bit_duzlemleri[3], bit_duzlemleri[4])
    satir3 = stack(bit_duzlemleri[5], bit_duzlemleri[6], bit_duzlemleri[7])


    grid = np.vstack((satir1, satir2, satir3))

    # plt.imshow(grid, cmap="gray")
    # plt.show()

    sfoto1 = foto_sikistirma(foto, [7, 6])
    sfoto2 = foto_sikistirma(foto, [7, 6, 5, 4])
    sfoto3 = foto_sikistirma(foto, [7, 6, 5, 4, 3, 2])
    sfoto4 = foto_sikistirma(foto, [7, 6, 5, 4, 3, 2, 1, 0])


    cv2.imwrite("./fotograflar/bit_8_7.png", sfoto1)
    cv2.imwrite("./fotograflar/bit_8_7_6_5.png", sfoto2)
    cv2.imwrite("./fotograflar/bit_8_7___3.png", sfoto3)
    cv2.imwrite("./fotograflar/bit_8_7____1.png", sfoto4)

    print("sfoto4 == foto: ", np.array_equal(foto, sfoto4))

    satir1 = stack(sfoto1, sfoto2)
    satir2 = stack(sfoto3, sfoto4)

    grid = np.vstack((satir1, satir2))

    plt.imshow(grid, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()











