import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened(): 
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    if not ret: 
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output video file
    out.write(frame)

    # Display the frame in a window named 'Webcam'
    cv2.imshow('Webcam', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
