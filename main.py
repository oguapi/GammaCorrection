#Reference: https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html

import os

import cv2
import numpy as np

def gammaCorrection(img_original):
    ##Changing contrast brightnees with gamma correction  https://github.com/opencv/opencv/blob/3.4/samples/python/tutorial_code/imgProc/changing_contrast_brightness_image/changing_contrast_brightness_image.py

    #Look-up table is used to improve the performance of the computation
    # as only 256 values needs to be calculated once.
    lookUpTable= np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i]= np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

    res= cv2.LUT(img_original, lookUpTable) #image with gamma correction

    img_gammaCorrected= cv2.hconcat([img_original, res]) #if you want to concantenar the original a the gamma correction
    return img_gammaCorrected

gamma= 0.9      #img2=0.6   img3=0.8
gamma_max= 200

imgPath= os.path.join('.','data', 'img1.jpg')
imgOutputPath= os.path.join('.','assest', 'output1.jpg')


img= cv2.imread(imgPath)
imgGammaCorrected= gammaCorrection(img)

cv2.imwrite(imgOutputPath, imgGammaCorrected)

#cv2.imshow("Image original", img)
cv2.imshow("Gamma Correction", imgGammaCorrected)

cv2.waitKey(0)
cv2.destroyAllWindows