import cv2
import numpy as np


cap = cv2.VideoCapture(0)


def blurring(img):
    blur=cv2.GaussianBlur(img, (51,51), 0)
    return blur


def pencil_sketch(img):
    pencil_img_gray,pencil_img=cv2.pencilSketch(img, sigma_s=65, sigma_r=0.05, shade_factor=0.03)
    pencil=cv2.bitwise_not(pencil_img_gray)
    pencil=cv2.cvtColor(pencil,cv2.COLOR_GRAY2BGR)
    return pencil   


def sepia_filter(img):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.filter2D(img, -1, kernel)


def cartoon(img):
    cartoon_image = cv2.stylization(img, sigma_s=160, sigma_r=0.25)  
    return cartoon_image


def green_overlay(img):
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
    img = overlay(img, 1) #(0 = blue, 1 = green and 2 = red)
    return img


def emboss_filter(img):
    kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
    return cv2.filter2D(img, -1, kernel*5)


def paint(frame):
    kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
    frame7 = cv2.erode(frame.copy(), kern)
    return frame7


while True:
    x,frame=cap.read()
    cv2.imshow('Frame',frame)
    f1=frame.copy()
    f2=frame.copy()
    f3=frame.copy()
    f4=frame.copy()
    f5=frame.copy()
    f6=frame.copy()
    mask_colour = (255,255,255)
    

    mask1 = np.zeros(f1.shape, dtype=np.uint8)
    roi1 = np.array([[(0,0), (276,0), (224,168)]], dtype=np.int32)
    cv2.fillPoly(mask1, roi1, mask_colour)
    masked_image1 = cv2.bitwise_and(f1,mask1)
    masked_image1 = pencil_sketch(masked_image1)

    
    mask2 = np.zeros(f2.shape, dtype=np.uint8)
    roi2 = np.array([[(276,0), (640,0), (340,255),(224,168)]], dtype=np.int32)
    cv2.fillPoly(mask2, roi2, mask_colour)
    masked_image2 = cv2.bitwise_and(f2,mask2)
    masked_image2=sepia_filter(masked_image2)


    mask3 = np.zeros(f3.shape, dtype=np.uint8)
    roi3 = np.array([[(640,0), (640,480),(340,255)]], dtype=np.int32)
    cv2.fillPoly(mask3, roi3, mask_colour)
    masked_image3 = cv2.bitwise_and(f3,mask3)
    masked_image3=paint(masked_image3)
    

    mask4 = np.zeros(f4.shape, dtype=np.uint8)
    roi4 = np.array([[(380,285), (640,480),(320,480)]], dtype=np.int32)
    cv2.fillPoly(mask4, roi4, mask_colour)
    masked_image4 = cv2.bitwise_and(f4,mask4)
    masked_image4=emboss_filter(masked_image4)
    

    mask5 = np.zeros(f5.shape, dtype=np.uint8)
    roi5 = np.array([[(284,213), (380,285),(320,480),(0,480),(0,290)]], dtype=np.int32)
    cv2.fillPoly(mask5, roi5, mask_colour)
    masked_image5 = cv2.bitwise_and(f5,mask5)
    masked_image5 = cartoon(masked_image5)
    

    mask6 = np.zeros(f6.shape, dtype=np.uint8)
    roi6 = np.array([[(0,0), (284,213),(0,290)]], dtype=np.int32)
    cv2.fillPoly(mask6, roi6, mask_colour)
    masked_image6 = cv2.bitwise_and(f6,mask6)
    masked_image6=green_overlay(masked_image6)
    


    final1=cv2.bitwise_or(masked_image1,masked_image2)
    final2=cv2.bitwise_or(final1,masked_image3)
    final3=cv2.bitwise_or(final2,masked_image4)
    final4=cv2.bitwise_or(final3,masked_image5)
    final5=cv2.bitwise_or(final4,masked_image6)
    
    cv2.imshow('Final',final5)
    

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
