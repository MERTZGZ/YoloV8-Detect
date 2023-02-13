# YOLOv8, girdi olarak görüntülerin belirli bir boyutta olmasını bekler.
# Bu boyut, ağın arka planda yapılandırılmasına bağlıdır.
# Genellikle, YOLOv8 girdi görüntülerinin 448 x 448 piksel boyutunda olması beklenir.
# Ancak, bu değer değişebilir ve başka bir değer de kullanılabilir.
# Her resmin boyutu farklı olduğu için, resimleri ortak bir boyuta dönüştürmeniz gerekir.

import cv2
import os

# Resimlerin bulunduğu dizin
input_path = 'DataSet Original/Kedi'
# Dönüştürülmüş resimlerin kaydedileceği dizin
output_path = 'Boyutlandirilmis DataSet/Kedi'

# Resim boyutları
width = 640
height = 640

# Tüm resimleri dönüştür
for filename in os.listdir(input_path):
    # Resmi oku
    img = cv2.imread(os.path.join(input_path, filename))
    # Resmi boyutlarını değiştir
    img = cv2.resize(img, (width, height))
    # Dönüştürülmüş resmi kaydet
    cv2.imwrite(os.path.join(output_path, filename), img)
