# Gamma Correction
Changing the constrast and brightness of an image!

## Requirements
  * Python 3.9
  * requirements.txt

## Gamma
This can be used to correct the brightness of an image by a non linear transformation between the value:

![Non linear transformation][lil-transformation-url]

 When γ< 1, the original dark regions will be brighter and the histogram will be shifted to the right whereas it will be the opposite with γ>1. The gamma correction should tend to add less saturation effect as the mapping is non linear.

This process is implemented python, and the following libraries:
  * OpenCV (For testing)
  * Numpy (Matrix application)
  *  (F)

## Output

Below are the original images with their respective gamma correction:

![Image 1][lil-img1-url]

For this the gamma value (γ) is 0.9

![Image 2][lil-img2-url]

In this case, the gamma value is 0.6.

![Image 3][lil-img3-url]

For the last one, the gamma value 0.8


[lil-img1-url]: https://raw.githubusercontent.com/oguapi/GammaCorrection/master/assest/output1.jpg
[lil-img2-url]: https://raw.githubusercontent.com/oguapi/GammaCorrection/master/assest/output2.jpg
[lil-img3-url]: https://raw.githubusercontent.com/oguapi/GammaCorrection/master/assest/output3.jpg
[lil-transformation-url]: https://raw.githubusercontent.com/oguapi/GammaCorrection/master/assest/transformation.jpg