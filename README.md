# opencv-examples
import cv2

# Görüntüyü yükleyin
img = cv2.imread('dosya_adi.jpg', cv2.IMREAD_COLOR)

# Görüntüyü gri tonlamaya çevirin
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüyü gösterin
cv2.imshow('Gri Görüntü', gray)

# Bir tuşa basana kadar bekleyin
cv2.waitKey(0)

# Tüm pencereleri kapatın
cv2.destroyAllWindows()
