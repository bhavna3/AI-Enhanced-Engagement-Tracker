import cv2

img=cv2.imread(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image1.jpg")
blur=cv2.GaussianBlur(img,(15,15),0)

cv2.imshow("Blurred Image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()