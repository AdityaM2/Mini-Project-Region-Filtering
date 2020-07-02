import cv2

def negative_image(img):
    img_not=cv2.bitwise_not(img)
    cv2.imshow("Inverted",img_not)

def pencil_sketch(img):
    pencil_img=cv2.pencilSketch(img, sigma_s=65, sigma_r=0.5, shade_factor=0.03)
    cv2.imshow("Pencil Sketch",pencil_img)
