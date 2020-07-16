import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import stack, rescale


def fotograf_negatifi(foto):
    L = np.max(foto) # 255
    negatif_foto = L - foto
    return negatif_foto


def log_donusumu(r, c):
    r = r.astype(float)
    s = c*np.log(1 + r)
    s = rescale(s)
    return s


foto = cv2.imread("./fotograflar/fourier_spectrum.tif", 0)
negatif_foto = fotograf_negatifi(foto)
log_foto = log_donusumu(foto, c=1)

yan_yana_negatif = stack(foto, negatif_foto)
yan_yana_log = stack(foto, log_foto)

print("log min: ", np.min(log_foto))
print("log max: ", np.max(log_foto))


plt.imshow(yan_yana_log, cmap="gray")
plt.show()
