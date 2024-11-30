# README

## **Image Processing**

### **Libraries/Frameworks Used:**  
- OpenCV: 4.10.0.84

### **Developed Features:**

1. **Image Blurring**
 Reduces noise and smoothens details in an image by averaging pixel values within a specified radius, enhancing visual clarity in high-noise scenarios.

Input & Output
   
![image](https://github.com/user-attachments/assets/8ab3c8ae-40f0-47ef-8033-5bdaff22bffd)![image](https://github.com/user-attachments/assets/6d3c51db-ac9f-4a3b-a0ce-d72f430039cd)

2. **Contour Detection**
 Identifies and highlights the boundaries of objects within an image, useful for shape analysis and object detection tasks.

   Input & Output
   
    ![image](https://github.com/user-attachments/assets/86cd4778-86af-4da8-bf63-b7a3e63d6c3c)![image](https://github.com/user-attachments/assets/7e0161ea-454d-4bcf-b80d-e4ae2173047a)

3. **Cropping**
   Selects and isolates a specific region of interest from an image, allowing focus on a particular area without modifying the original image dimensions.

   Input & Output
   
![image](https://github.com/user-attachments/assets/057034e2-c4b0-42b4-95ef-aa4944b6fdc6)![image](https://github.com/user-attachments/assets/0384fe08-6433-4a7f-9cbb-e19e14e214a9)

   
4. **Dilation and Erosion**
   Morphological transformations that expand (dilation) or shrink (erosion) object boundaries in an image, enhancing or reducing specific features for analysis.

    Input
   
    ![image](https://github.com/user-attachments/assets/e6cbe036-1117-43b1-b556-0838283b7b6d)

   Output

![image](https://github.com/user-attachments/assets/d36d9985-a992-478a-8ea9-1ad0c8510e9a)
![image](https://github.com/user-attachments/assets/69cd7e1f-6b3b-434c-ac13-f8e045cff17a)

5. **Edge Detection**
   Highlights the edges within an image, emphasizing significant transitions between colors or intensities, often used for feature extraction.
   Input & Output
   
    ![image](https://github.com/user-attachments/assets/14363781-5576-400c-908c-3870fb83b96a)![image](https://github.com/user-attachments/assets/e31e0912-75fe-43d4-b2bb-a93284e3bb7e)

6. **Histogram Equalization**
    Adjusts the intensity distribution across an image to improve contrast, revealing finer details in images with poor lighting or low contrast.
   Input & Output
   
    ![image](https://github.com/user-attachments/assets/bf0ebd0d-66f7-4068-8ed6-6eaf42951550)![image](https://github.com/user-attachments/assets/7e17e582-3eeb-41b9-8fbd-42bc1bc3e1e6)



7. **HSV Conversion**
   Converts an image from RGB to HSV (Hue, Saturation, Value) color space, separating color information for more flexible color analysis and filtering.

   Input & Output
   
    ![image](https://github.com/user-attachments/assets/51e28532-7062-47c3-81a4-5acf96d53f27)![image](https://github.com/user-attachments/assets/084bb20f-926c-4b72-b49b-2ed183e06d7a)


8. **Image Stacking**
Combines multiple images in either horizontal or vertical layouts, useful for comparison and visualization of variations between images.

    Input 
   
   ![image](https://github.com/user-attachments/assets/01b79806-8937-4ed4-9146-e42093cedb5b)![image](https://github.com/user-attachments/assets/d972de8f-9fd1-4add-8c9d-6cda61d911ba)

   
   Output
   
   ![image](https://github.com/user-attachments/assets/2d7c5c38-593e-4bfa-97da-a2da6a223a73)![image](https://github.com/user-attachments/assets/2fd50f51-ac94-4bdd-9e9f-f17e497793a0)


9. **Noise Addition**
Introduces random variations in pixel intensity, simulating real-world conditions for testing robustness in image processing algorithms.

   Input 
   
![image](https://github.com/user-attachments/assets/284643a3-ef12-419c-8126-e666a26bb300)

 Output
 
![image](https://github.com/user-attachments/assets/d1f69427-0e78-4e8a-a676-413c112cc985)

10. **Morphological Transformations**
 Applies operations like opening, closing, or morphological gradients to enhance structures or filter out noise in binary images.

    Input 
   
 ![image](https://github.com/user-attachments/assets/b3ed00c2-6f86-4afe-a077-b2bec33fa6c1)
 
 Output
 
 ![image](https://github.com/user-attachments/assets/de74299e-3394-4a2d-a370-0c110b5a6614)

11. **Resizing**
Alters the dimensions of an image, scaling it up or down while preserving its aspect ratio, important for consistent input size in model training.

    Input & Output
   
 ![image](https://github.com/user-attachments/assets/58ad238e-a261-48d4-8a5e-08e05092f126)![image](https://github.com/user-attachments/assets/83e69e6d-44f8-4d85-88a1-32ff1a9e54e9)

12. **RGB to Grayscale Conversion**
Converts a colored image to grayscale by removing color information, simplifying analysis by reducing it to intensity variations.

    Input & Output
   
  ![image](https://github.com/user-attachments/assets/bf431c70-3056-4620-9b18-b01631069ace)![image](https://github.com/user-attachments/assets/bc6bd0ff-7969-462f-87c0-31864da368e4)

13. **Rotation**
Rotates an image by a specified angle, useful for adjusting orientation or performing geometric transformations.
    Input & Output
   
   ![image](https://github.com/user-attachments/assets/d79d1c1a-babd-4789-8d74-332252a7b295)![image](https://github.com/user-attachments/assets/15ab6397-9b87-4229-b69e-7e1154a8f7ef)


14. **Template Matching**
Searches for a specific pattern or template within an image, useful for object recognition and locating areas of interest.

    Input & Output
   
    ![image](https://github.com/user-attachments/assets/423b4960-f7c9-4854-ab93-a0cb163392af)![image](https://github.com/user-attachments/assets/aebe2567-4621-4f2f-8196-0bdc71295908)


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

![image](https://github.com/user-attachments/assets/6605f8ad-f6d3-4538-8770-2c4b50e98150)![image](https://github.com/user-attachments/assets/6674e986-a218-4614-9f7f-90f04538d7b7)

4. **Video Saving**

This function captures live video and saves it to a specified output file.

![image](https://github.com/user-attachments/assets/dd50cd6b-bf80-4355-9c1b-48cdd0d95757)

5. **Video Streaming**
   
This function captures live video from the webcam and displays it in real-time.

![image](https://github.com/user-attachments/assets/222dd0c3-06c5-4319-9280-58fb1e01846b)

---

## **Annotations**

### **Libraries/Frameworks Used:**  
- OpenCV: 4.10.0.84  
- LabelImg: 1.8.6

### **Developed Features:**

1. **Labeling**

Used to draw bounding boxes on images based on annotations in the label files.

![image](https://github.com/user-attachments/assets/37278f85-bc6f-4b60-88e1-f854a8c924c3)

2. **Data Segregation**

It organizes images and their label files into matched and unmatched directories.

![image](https://github.com/user-attachments/assets/5f6d85ca-b347-4803-9751-7a741b41bc8b)

3. **Label Manipulation**

It updates class numbers in label files for object detection tasks.

![image](https://github.com/user-attachments/assets/530e6bfa-1f2a-45cb-9503-621b53dd4511)

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

Face detection using the face_recognition library.

![image](https://github.com/user-attachments/assets/a5f8ac69-c191-4ebd-9854-f20cc6b5d8bc)![image](https://github.com/user-attachments/assets/5424afa0-aeab-4196-a40a-879781328f5b)


2. **Attendance Save**

When the face is recognized, the event is logged with the date and time in an Excel file.

![image](https://github.com/user-attachments/assets/a5f8ac69-c191-4ebd-9854-f20cc6b5d8bc)![image](https://github.com/user-attachments/assets/a3043b08-9b67-40f8-8bbe-e4cd27032ede)


3. **Facial Landmarks**

Uses dlib's landmark predictor to monitor attentiveness based on head pose, logging scores and saving annotated screenshots, the event is logged in an Excel file.

![image](https://github.com/user-attachments/assets/aad7ac9a-66f0-47ab-ad38-5680cf5a25f3)![image](https://github.com/user-attachments/assets/92cd9d54-a05b-4758-85db-b11d242088be)


4. **Attention Score**

Calculates attention scores using face recognition and screenshots are saved for analysis.

![image](https://github.com/user-attachments/assets/1e095512-6861-40de-800e-738aabfd6209)![image](https://github.com/user-attachments/assets/0a670cc0-f8d9-4986-86fe-961c148c1036)

5. **Average Attention Score**

Calculates average attention scores using face recognition and screenshots are saved for analysis.

![image](https://github.com/user-attachments/assets/1e095512-6861-40de-800e-738aabfd6209)![image](https://github.com/user-attachments/assets/a40b3e02-f501-428d-bc6b-9ee6aee2fd06)


6. **Excel_sc_dt**

Captures video, logs attendance, and saves screenshots and tracks attention.

![image](https://github.com/user-attachments/assets/a5f8ac69-c191-4ebd-9854-f20cc6b5d8bc)![image](https://github.com/user-attachments/assets/7e611658-9421-4e11-93ce-27d862d25fad)

7. **excel_sc**

An alternative configuration for logging and capturing screenshots.

![image](https://github.com/user-attachments/assets/a5f8ac69-c191-4ebd-9854-f20cc6b5d8bc)![image](https://github.com/user-attachments/assets/58282cb3-07d6-41cc-9fa3-e393f7fbd66f)

8. **Tools**

Additional tools and utilities for face recognition, the events are logged in an Excel file.

![image](https://github.com/user-attachments/assets/a5f8ac69-c191-4ebd-9854-f20cc6b5d8bc)![image](https://github.com/user-attachments/assets/eb4ecba8-8d1b-430f-a31d-9ee566a919eb)

9. **Test**

Testing helper functions and utilities for face recognition, the events are logged in an Excel file.

![image](https://github.com/user-attachments/assets/a5f8ac69-c191-4ebd-9854-f20cc6b5d8bc)![image](https://github.com/user-attachments/assets/6317f1c7-70b0-435b-bc7b-385c275f7c60)

---

## **Additional Features**

### **Detect Emotions**

This code implements a facial emotion detection system using DeepFace and OpenCV libraries. It takes an image input, detects faces using OpenCV, and analyzes emotions (like happy, sad, angry, etc.) using the DeepFace framework. The program draws bounding boxes around detected faces and displays the dominant emotion with its probability. Results are visualized using matplotlib, showing both the original and annotated images side by side, along with a breakdown of emotion probabilities. The code is structured with separate functions for image loading, result visualization, and main processing, making it modular and easy to maintain.

1. **Anger Detection**

![image](https://github.com/user-attachments/assets/1792b2be-1dcd-40bf-9349-d0c842648ec8)

2. **Happiness Detection**

![image](https://github.com/user-attachments/assets/461ce1b2-fbb7-46bb-ad8f-07e5290fa0d1)

3. **Suprise Detection**

![image](https://github.com/user-attachments/assets/5e49134e-784a-4e5e-b641-d4d811d032a0)



