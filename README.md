# README

## **Image Processing**

### **Libraries/Frameworks Used:**  
- OpenCV: 4.10.0.84

### **Developed Features:**

1. **Image Blurring**
 Reduces noise and smoothens details in an image by averaging pixel values within a specified radius, enhancing visual clarity in high-noise scenarios.

   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

   Output
   
   ![image](https://github.com/user-attachments/assets/a57947b1-34ac-4032-8b8f-34ea209e37ef)

2. **Contour Detection**
 Identifies and highlights the boundaries of objects within an image, useful for shape analysis and object detection tasks.

   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

   Output

   ![image](https://github.com/user-attachments/assets/ee2fd89c-4dbb-41f9-8683-5e3ed0db437c)
   
   
3. **Cropping**
   Selects and isolates a specific region of interest from an image, allowing focus on a particular area without modifying the original image dimensions.

   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

   Output

   ![image](https://github.com/user-attachments/assets/0384fe08-6433-4a7f-9cbb-e19e14e214a9)

   
4. **Dilation and Erosion**
   Morphological transformations that expand (dilation) or shrink (erosion) object boundaries in an image, enhancing or reducing specific features for analysis.
   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

   Output

   ![image](https://github.com/user-attachments/assets/ab4228bd-8227-480b-b8ce-d0606ea8601e)                          ![image](https://github.com/user-attachments/assets/2ddbde52-cfe6-41ab-80bc-23d260bf31ac)


5. **Edge Detection**
   Highlights the edges within an image, emphasizing significant transitions between colors or intensities, often used for feature extraction.
   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

   Output

   ![image](https://github.com/user-attachments/assets/77f66c0a-b0e2-4180-b55c-b026e415e564)

6. **Histogram Equalization**
    Adjusts the intensity distribution across an image to improve contrast, revealing finer details in images with poor lighting or low contrast.
   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/d7da974e-3855-4501-935a-b8c826b45627)

7. **HSV Conversion**
   Converts an image from RGB to HSV (Hue, Saturation, Value) color space, separating color information for more flexible color analysis and filtering.


   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/f13a78fd-5fa3-4dc3-a137-83534409417f)

8. **Image Stacking**
Combines multiple images in either horizontal or vertical layouts, useful for comparison and visualization of variations between images.
   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)
   ![image](https://github.com/user-attachments/assets/ae466150-0368-47f5-9f36-266609e451ed)

    Output

   ![image](https://github.com/user-attachments/assets/2fd50f51-ac94-4bdd-9e9f-f17e497793a0)

   ![image](https://github.com/user-attachments/assets/2d7c5c38-593e-4bfa-97da-a2da6a223a73)


10. **Noise Addition**
Introduces random variations in pixel intensity, simulating real-world conditions for testing robustness in image processing algorithms.
   Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

   ![image](https://github.com/user-attachments/assets/d1f69427-0e78-4e8a-a676-413c112cc985)

11. **Morphological Transformations**
 Applies operations like opening, closing, or morphological gradients to enhance structures or filter out noise in binary images.
    Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/de74299e-3394-4a2d-a370-0c110b5a6614)

12. **Resizing**
Alters the dimensions of an image, scaling it up or down while preserving its aspect ratio, important for consistent input size in model training.
    Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/f747821f-efe6-4ffa-bd96-b035751af3d4)

13. **RGB to Grayscale Conversion**
Converts a colored image to grayscale by removing color information, simplifying analysis by reducing it to intensity variations.


    Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/15b74d50-ab28-41b9-a326-d21097b5f53e)

14. **Rotation**
Rotates an image by a specified angle, useful for adjusting orientation or performing geometric transformations.
    Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/e2b99a6f-1406-4be3-af55-469f1bbda024)

15. **Template Matching**
Searches for a specific pattern or template within an image, useful for object recognition and locating areas of interest.

    Input
   
    ![image](https://github.com/user-attachments/assets/30432e70-a8da-48a3-b718-b59ae54caa12)

    Output

    ![image](https://github.com/user-attachments/assets/949d51b2-6677-4ec6-990c-e4b5fefc57d6)

---

## **Video Processing**

### **Libraries/Frameworks Used:**  
- OpenCV: 4.10.0.84

### **Developed Features:**
1. **Multi-video Processing**

This function reads and displays images from a specified folder, printing the dimensions of each image.

![image](https://github.com/user-attachments/assets/84c836a1-b012-4d39-86f8-67d589bd2ccf)

![image](https://github.com/user-attachments/assets/1f157d55-3698-45d6-a860-eb4a2484e623)

2. **Video Stacking**

This function reads and resizes two video files, concatenating them horizontally.

![image](https://github.com/user-attachments/assets/24882f64-aecf-47c5-bf63-c0aa21fee2a8)

3. **Frame Rate Adjustment**

This function captures video from the webcam, displays it in real-time, and calculates the FPS.

4. **Video Saving**

This function captures live video and saves it to a specified output file.

5. **Video Streaming**
This function captures live video from the webcam and displays it in real-time.
---

## **Annotations**

### **Libraries/Frameworks Used:**  
- OpenCV: 4.10.0.84  
- LabelImg: 1.8.6

### **Developed Features:**
1. **Labeling**
2. **Data Segregation**
3. **Label Manipulation**

---

## **Face Recognition**

### **Libraries/Frameworks Used:**  
- opencv-python: 4.10.0.84  
- face_recognition: 1.3.0  
- dlib: 19.24.6  
- pandas: 2.0.2  
- numpy: 1.23.3  
- datetime: 5.5  
- imutils: 0.5.4  
- os (standard library)

### **Developed Features:**
1. **Face Recognition**
2. **Attendance System**
3. **Facial Landmarks**
4. **Attention Score**
5. **Excel Score Tracking**
6. **Average Attention Score**
7. **Tools for Testing and Evaluation**
