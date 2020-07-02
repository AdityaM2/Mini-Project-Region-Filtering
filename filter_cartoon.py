import cv2
img=cv2.imread('alpha.jpg')
resized=cv2.resize(img,(600,600))
# 1) Edges
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7,9)

# 2) Color
color = cv2.edgePreservingFilter(resized,9,300,300)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", gray)
cv2.imshow("Cartoon", cartoon)
cv2.imshow("color", color)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()