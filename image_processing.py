from google.colab.patches import cv2_imshow

import cv2 # importing opencv library packages

image = cv2.imread("puppy.jpg")

cv2_imshow(img) # Displaying the original image

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Original image ------>> Grayscale

cv2_imshow(img_gray)# Displaying the grayscale  image

img_invert=cv2.bitwise_not(img_gray) # Grayscale ------>> Negative

cv2_imshow(img_invert) # Displaying the  Negative  image

img_smooth=cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0) # Negative ------>> Blur image

cv2_imshow(img_smooth) # Displaying the  blur image

def dodgeV2(x,y):
  return cv2.divide(x,255-y,scale=256)

final_img=dodgeV2(img_gray,img_smooth) #Dividing the grayscale image by the inverted blurry image since images are just arrays

cv2_imshow(final_img) # Displaying the  final sketch image

cv2_imshow(img)

cv2_imshow(final_img) # Displaying the original and the final sketch image
