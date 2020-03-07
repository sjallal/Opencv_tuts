# Importing Images...
import cv2

img = cv2.imread('lena.png')
cv2.imshow('Output Image',img)
# cv2.imwrite('Output Image.png',img)
print(img.shape)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray_img)

# img1 = cv2.imread('F:/Camera/1.jpeg')
# cv2.imshow('Output1 Image',img1)
# print(img1.shape)

cv2.waitKey(0);
cv2.destroyAllWindows()
