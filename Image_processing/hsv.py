import cv2

img=cv2.imread(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image1.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("hsv Image", hsv)  #hue - 0 to 179 deg, saturation - 0 or 255, value - brightness 
cv2.waitKey(0)
cv2.destroyAllWindows()