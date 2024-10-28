import cv2

# Open the default webcam (usually camera index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured correctly
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Press 'q' to exit the webcam window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
