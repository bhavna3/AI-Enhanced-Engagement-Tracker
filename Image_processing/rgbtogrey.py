import cv2
image = cv2.imread(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image2.jpg" , gray_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
