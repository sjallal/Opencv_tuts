# Capturing web cam
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    print(frame)

else:
    ret = False

# plt.imshow(frame)
# plt.show()

# The above 2 lines will show the raw image taken from the web cam.
# If you wish to convert them into RGB use the following code.

img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title("Image-1")
plt.xticks()
plt.yticks()
plt.show()

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
