import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('dosya_yolu/dosya_adi.jpg')

# BGR renk uzayından HSV renk uzayına dönüştür
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Mavi rengin HSV değer aralığını belirle
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Bu HSV aralığına uygun pikselleri seç
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Maskeleme işlemi ile sadece mavi renkleri vurgula
result = cv2.bitwise_and(img, img, mask=mask)

# Sonucu göster
cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Filtered Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
