import cv2 as cv
import face_recognition
import pandas as pd
from datetime import datetime, timedelta
import os

# Load the known image and encode it
try:
    known_image_path = r"C:\Users\saikeerthana\OneDrive\Desktop\Neha\shit\DP.jpg"
    known_image = face_recognition.load_image_file(known_image_path)
    known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')
    if not known_faces:
        raise ValueError("No faces found in the reference image.")
    known_face_encoding = known_faces[0]
except Exception as e:
    print(f"Error loading or encoding the image: {e}")
    exit()

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time']
df = pd.DataFrame(columns=columns)

# Launch the live camera
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

# Parameters
confidence_threshold = 0.6
frame_skip = 2
frame_count = 0

# Time tracking
last_recognition_time = None
entry_duration = timedelta(minutes=2)
gap_time = timedelta(minutes=5)

output_path = r'C:\Users\saikeerthana\OneDrive\Desktop\attendancetest.xlsx'

print(f"Saving attendance to: {output_path}")
print("Press 'q' to exit the video stream.")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Can't receive the frame")
        break

    frame = cv.resize(frame, (640, 480))
    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    face_locations = face_recognition.face_locations(frame)
    if not face_locations:
        continue

    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        distance = face_recognition.face_distance([known_face_encoding], face_encoding)[0]
        print(f"Distance: {distance}, Threshold: {confidence_threshold}")

        if distance < confidence_threshold:
            now = datetime.now()

            if last_recognition_time is None or (now - last_recognition_time) >= gap_time:
                # Add new entry to DataFrame
                new_entry = pd.DataFrame({
                    'Name': ['Bhavana'],
                    'Date': [now.strftime("%Y-%m-%d")],
                    'Time': [now.strftime("%H:%M:%S")]
                })
                df = pd.concat([df, new_entry], ignore_index=True)
                last_recognition_time = now
                print(f"Face recognized: Bhavana at {now.strftime('%H:%M:%S')}")

            # Draw rectangle and label on frame
            for (top, right, bottom, left) in face_locations:
                cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv.putText(frame, 'Bhavana', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        else:
            for (top, right, bottom, left) in face_locations:
                cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv.putText(frame, 'Not Bhavana', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show the frame
    cv.imshow('Video Stream', frame)

    if cv.waitKey(1) == ord('q'):
        break

# Save DataFrame to Excel if it contains data
if not df.empty:
    try:
        df.to_excel(output_path, index=False)
        print(f"Attendance saved successfully to: {output_path}")
    except Exception as e:
        print(f"Error saving the Excel file: {e}")
else:
    print("No attendance data to save.")

# Release resources
cam.release()
cv.destroyAllWindows()
