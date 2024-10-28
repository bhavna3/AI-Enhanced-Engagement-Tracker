import cv2

img=cv2.imread(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image1.jpg")
crop=img[50:200,100:300]  #img[strt_y:end_y, strt_x:end_x]


cv2.imshow("cropped Image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()