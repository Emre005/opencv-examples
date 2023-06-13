import cv2

# Görüntüyü yükle
img = cv2.imread('dosya_yolu/dosya_adi.jpg', cv2.IMREAD_COLOR)

# Görüntüyü gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny kenar tespit algoritmasını uygula
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Kenarları göster
cv2.imshow('Canny Edges', edges)

# Bir tuşa basana kadar bekleyin
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
