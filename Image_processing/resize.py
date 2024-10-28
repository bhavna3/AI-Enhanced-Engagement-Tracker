import cv2

img=cv2.imread(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image2.jpg")
resized=cv2.resize(img,(400,300))

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()