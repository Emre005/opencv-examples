import cv2

# Görüntüyü yükle
img = cv2.imread('dosya_yolu/dosya_adi.jpg', cv2.IMREAD_COLOR)

# Dikdörtgen çiz: cv2.rectangle(img, (x1, y1), (x2, y2), (B, G, R), thickness)
# (x1, y1) -> dikdörtgenin sol üst köşesinin koordinatları
# (x2, y2) -> dikdörtgenin sağ alt köşesinin koordinatları
# (B, G, R) -> dikdörtgenin rengi (Blue, Green, Red)
# thickness -> çizgi kalınlığı. Eğer negatif bir değer girilirse (örn: -1), dikdörtgen dolu bir şekilde çizilir.
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)

# Çizilen dikdörtgenli görüntüyü göster
cv2.imshow('Image with rectangle', img)

# Bir tuşa basana kadar bekleyin
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
