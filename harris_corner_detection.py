import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('dosya_yolu/dosya_adi.jpg')

# Gri tonlamaya çevir (Harris fonksiyonu gri tonlamalı görüntüler üzerinde çalışır)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Float türüne dönüştür (Harris fonksiyonu float görüntüler üzerinde çalışır)
gray = np.float32(gray)

# Harris köşe tespiti
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Sonuçları genişlet (köşeler daha belirgin hale gelir)
dst = cv2.dilate(dst, None)

# Eşik değeri belirle ve köşeleri görüntü üzerinde işaretle
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Köşeleri tespit edilmiş görüntüyü göster
cv2.imshow('Harris Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
