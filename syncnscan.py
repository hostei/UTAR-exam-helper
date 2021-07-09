import cv2 
import numpy as np 
import os
import random

m = random.randint(100000,999999)

for x in range(10):
    x+=1
    os.system("pause")
    os.system("curl http://192.168.0.10:8080/photo.jpg -m 5 -O photo.jpg")
    old_file_name = "photo.jpg"
    new_file_name = str(x + m) + ".jpg"
    if os.path.exists('photo.jpg'):
        os.rename(old_file_name, new_file_name)
        image1 = cv2.imread(new_file_name)
        img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                              cv2.THRESH_BINARY, 199, 5)
        b = "scanned/a" + str(x + m) + ".jpg"
        cv2.imwrite(b, thresh1)
