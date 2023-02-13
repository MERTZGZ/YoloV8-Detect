#Bu, görüntü verilerinin artırılması için bir Python betiğidir. 
#Betik, JPG görüntülerinden oluşan bir dizin alır, her görüntü üzerinde birkaç veri artırma tekniği uygular ve artırılmış görüntüleri ayrı bir dizinde kaydeder. 
#Bu betikte uygulanan veri artırma teknikleri, döndürme, çevirme, ölçeklendirme, Gauss gürültüsü ekleme ve renk değiştirmeyi içermektedir.
#Görüntü işleme için OpenCV kütüphanesi kullanılır ve sayısal işlemler için Numpy kütüphanesi kullanılır.

import os
import cv2
import numpy as np

# Dosya yolunu belirtin
file_path = 'Boyutlandirilmis DataSet/Laptop'


# Veri çoğaltma teknikleri
def augment_data(img):
    # Döndürme
    angle = np.random.uniform(-45, 45)
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(img, rot_matrix, (w, h))

    # Ayna görüntü
    flip_img = cv2.flip(img, 1)

    # Daraltma/Genişletme
    scale_img = cv2.resize(img, None, fx=0.5, fy=0.5)
    scale_img = cv2.resize(scale_img, (img.shape[1], img.shape[0]))

    # Gauss Gürültüsü
    gauss = np.random.randn(*img.shape) * 0.1
    gauss_img = img + gauss

    # Renk Değiştirme
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hsv[..., 0] = img_hsv[..., 0] * np.random.uniform(0.5, 1.5)
    img_hsv[..., 1] = img_hsv[..., 1] * np.random.uniform(0.5, 1.5)
    img_hsv[..., 2] = img_hsv[..., 2] * np.random.uniform(0.5, 1.5)
    color_jittered_image = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    return [rotated_image, flip_img, scale_img, gauss_img, color_jittered_image]


# Klasör yolunu belirtin
output_path = 'Boyutlandirilimis ve Cogaltilmis DataSet/Laptop'

# Tüm JPG dosyalarını tarama
for filename in os.listdir(file_path):
    if filename.endswith('.jpg'):
        # Dosyayı okuma
        img = cv2.imread(os.path.join(file_path, filename))

        # Veri çoğaltma tekniklerini uygulama
        augmented_images = augment_data(img)

        # Çıktıları kaydetme
        for i, augmented_image in enumerate(augmented_images):
            output_file = os.path.join(output_path, '{}_{}.jpg'.format(os.path.splitext(filename)[0], i))
            cv2.imwrite(output_file, augmented_image)
