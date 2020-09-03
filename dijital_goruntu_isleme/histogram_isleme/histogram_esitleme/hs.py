import io

import cv2
import numpy as np
import matplotlib.pyplot as plt


def from_figure_to_image(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def get_histogram_image(img, L):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.hist(img, density=True, range=(0, L))
    hist_image = from_figure_to_image(fig).mean(axis=2)
    hist_image = cv2.resize(hist_image, img.shape)
    fig.clf()
    plt.close(fig)
    return hist_image


def get_normalized_histogram(img, L):
    histogram, bins = np.histogram(img, bins=L, range=(0, L))
    return histogram / img.size


def get_cumulative_dist(img, L):
    normalized_histogram = get_normalized_histogram(img, L)
    return np.cumsum(normalized_histogram, axis=0)


def histeq(img, L):
    shape = img.shape
    ravel = img.ravel()
    cumsum = get_cumulative_dist(ravel, L)
    values = (L-1) * cumsum
    eq_img = np.zeros_like(ravel)
    for i, pixel in enumerate(ravel):
        eq_img[i] = values[pixel]
    return eq_img.reshape(shape).astype(np.uint8)


# eq2 = cv2.equalizeHist(img)
def main():
    L = 256
    fotograf_konumlari = [
        "./fotograflar/acik.tif",
        "./fotograflar/grimsi.tif",
        "./fotograflar/koyu.tif",
        "./fotograflar/normal.tif"
    ]
    fotograflar = []
    orjinal_histogramlar = []

    hist_es_fotograflar = []
    hist_es_histogramlar = []

    for fotograf_konumu in fotograf_konumlari:
        fotograf = cv2.imread(fotograf_konumu, 0)
        fotograflar.append(fotograf)
        orjinal_histogramlar.append(get_histogram_image(fotograf, L))

        hist_es_fotograf = histeq(fotograf, L)
        hist_es_fotograflar.append(hist_es_fotograf)
        hist_es_histogramlar.append(get_histogram_image(hist_es_fotograf, L))

    grid = np.vstack([np.hstack((fotograf, orjinal_histogram, hist_es_fotograf, hist_es_histogram)) 
                                for fotograf, orjinal_histogram, hist_es_fotograf, hist_es_histogram in zip(fotograflar, 
                                                                                                            orjinal_histogramlar, 
                                                                                                            hist_es_fotograflar, 
                                                                                                            hist_es_histogramlar)])

    plt.imshow(grid, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()

