import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def blurring(img):
    blur=cv2.GaussianBlur(img, (51,51), 0)
    return blur
    
    
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

    
    mask2 = np.zeros(f2.shape, dtype=np.uint8)
    roi2 = np.array([[(276,0), (640,0), (340,255),(224,168)]], dtype=np.int32)
    cv2.fillPoly(mask2, roi2, mask_colour)
    masked_image2 = cv2.bitwise_and(f2,mask2)
    

    mask3 = np.zeros(f3.shape, dtype=np.uint8)
    roi3 = np.array([[(640,0), (640,480),(340,255)]], dtype=np.int32)
    cv2.fillPoly(mask3, roi3, mask_colour)
    masked_image3 = cv2.bitwise_and(f3,mask3)


    mask4 = np.zeros(f4.shape, dtype=np.uint8)
    roi4 = np.array([[(380,285), (640,480),(320,480)]], dtype=np.int32)
    cv2.fillPoly(mask4, roi4, mask_colour)
    masked_image4 = cv2.bitwise_and(f4,mask4)
    

    mask5 = np.zeros(f5.shape, dtype=np.uint8)
    roi5 = np.array([[(284,213), (380,285),(320,480),(0,480),(0,290)]], dtype=np.int32)
    cv2.fillPoly(mask5, roi5, mask_colour)
    masked_image5 = cv2.bitwise_and(f5,mask5)
    masked_image5 = blurring(masked_image5)


    mask6 = np.zeros(f6.shape, dtype=np.uint8)
    roi6 = np.array([[(0,0), (284,213),(0,290)]], dtype=np.int32)
    cv2.fillPoly(mask6, roi6, mask_colour)
    masked_image6 = cv2.bitwise_and(f6,mask6)

    
    
    final1=cv2.bitwise_or(masked_image1,masked_image2)
    final2=cv2.bitwise_or(final1,masked_image3)
    final3=cv2.bitwise_or(final2,masked_image4)
    final4=cv2.bitwise_or(final3,masked_image5)
    final5=cv2.bitwise_or(final4,masked_image6)
    
    cv2.imshow('Final',final5)
    

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
