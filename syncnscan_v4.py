import cv2
import numpy as np
import os
import random
import imutils
from playsound import playsound

def variance_of_laplacian(image):

    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian

    return cv2.Laplacian(image, cv2.CV_64F).var()


# inspired by https://github.com/nivedwho/Document-Scanner-Python
# function that adds effects to the cropped image

def addEffects(img):
    dilated_img = cv2.dilate(img, np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 15)
    diff_img = 255 - cv2.absdiff(img, bg_img)
    norm_img = diff_img.copy()
    cv2.normalize(
        diff_img,
        norm_img,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_8UC1,
        )
    (_, thr_img) = cv2.threshold(norm_img, 250, 0, cv2.THRESH_TRUNC)
    cv2.normalize(
        thr_img,
        thr_img,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_8UC1,
        )

    return thr_img


m = random.randint(100000, 999999)
x = 0

while True:
    baba = 0
    x += 1
    os.system('curl http://192.168.0.107:8080/photo.jpg -m 5 -O photo.jpg'
              )
    old_file_name = 'photo.jpg'
    new_file_name = str(x + m) + '.jpg'
    if os.path.exists('photo.jpg'):
        os.rename(old_file_name, new_file_name)
        image1 = cv2.imread(new_file_name)
        img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

        for maa in range(2):
            os.system('curl http://192.168.0.107:8080/photo.jpg -m 5 -O photo.jpg'
                  )
            checker1 = cv2.GaussianBlur(img, (21, 21), 0)
            img2 = cv2.imread('photo.jpg')
            checker2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            checker2 = cv2.GaussianBlur(checker2, (21, 21), 0)
            frameDelta = cv2.absdiff(checker2, checker1)
            thresh = cv2.threshold(frameDelta, 25, 255,
                                   cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            n = 0

    # loop over the contours

            for c in cnts:
                print(cv2.contourArea(c))
        # if the contour is too small, ignore it        
                if cv2.contourArea(c) > 500:
                    n += 1
                    print(cv2.contourArea(c))
                    break
            if n <= 10:
                baba += 1
        fm = variance_of_laplacian(img)
        print(fm)
        
        if fm < 200.0 or baba < 2:
            os.remove(new_file_name)
            continue
        thresh1 = addEffects(img)
        b = 'scanned/a' + str(x + m) + '.jpg'
        cv2.imwrite(b, thresh1)
        playsound("a.mp3")
