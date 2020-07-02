import cv2
import numpy as np

def exponential_function(channel, exp):
    table = np.array([min((i**exp), 255) for i in np.arange(0, 256)]).astype("uint8")
    channel = cv2.LUT(channel, table)
    return channel
def overlay(img, number):
    for i in range(3):
        if i == number:
            img[:, :, i] = exponential_function(img[:, :, i], 1.02) 
        else:
            img[:, :, i] = 0 
    return img
img = cv2.imread('alpha.jpg')
resized=cv2.resize(img,(600,600))
original = resized.copy()
img = overlay(resized, 1) #(0 = blue, 1 = green and 2 = red)
cv2.imshow('original', original)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()