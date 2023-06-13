
Açıklama
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*grayscale_image.py örneğinde, cv2.imread fonksiyonu ile bir görüntü dosyasını yüklüyoruz. Dosya yolunu ve dosya adını kendi görüntünüzün yerine koymanız gerekmektedir. cv2.cvtColor fonksiyonu ile görüntüyü gri tonlamaya çeviriyoruz. Sonra, cv2.imshow fonksiyonu ile gri tonlamalı görüntüyü gösteriyoruz. cv2.waitKey(0) satırı, bir tuşa basılıncaya kadar görüntünün ekranda kalmasını sağlar. Son olarak, cv2.destroyAllWindows() ile tüm pencereleri kapatıyoruz.

*grayscale_image.py, öncelikle bir görüntüyü yükler ve gri tonlamaya çevirir. Sonra, cv2.Canny fonksiyonunu kullanarak Canny kenar tespit algoritmasını uygular. threshold1 ve threshold2 değerleri, kenar tespitinde kullanılan eşik değerleridir ve bu değerler, belirli bir görüntüye veya uygulamaya bağlı olarak ayarlanabilir.
