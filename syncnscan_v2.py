import cv2 
import numpy as np 
import os
import random
#inspired by https://github.com/nivedwho/Document-Scanner-Python
#function that adds effects to the cropped image
def addEffects(img):
    dilated_img = cv2.dilate(img, np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 15)
    diff_img = 255 - cv2.absdiff(img, bg_img)
    norm_img = diff_img.copy() 
    cv2.normalize(diff_img, norm_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    _, thr_img = cv2.threshold(norm_img, 250, 0, cv2.THRESH_TRUNC)
    cv2.normalize(thr_img, thr_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    
    return thr_img

m = random.randint(100000,999999)
x = 0
while True:
    x+=1
    os.system("pause")
    os.system("curl http://192.168.0.107:8080/photo.jpg -m 5 -O photo.jpg")
    old_file_name = "photo.jpg"
    new_file_name = str(x + m) + ".jpg"
    if os.path.exists('photo.jpg'):
        os.rename(old_file_name, new_file_name)
        image1 = cv2.imread(new_file_name)
        img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        thresh1 = addEffects(img)
        b = "scanned/a" + str(x + m) + ".jpg"
        cv2.imwrite(b, thresh1)
