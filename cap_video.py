import cv2
import os
import sys

# Check if the file exists and delete it
if os.path.exists('video.mp4'):
    os.remove('video.mp4')

# Flag to start/stop recording
recording = False

# Open the webcam
# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Get the frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Frame dimensions: {frame_width}x{frame_height}")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter('video.mp4', fourcc, 30.0, (frame_width, frame_height))

if not cap.isOpened():
    print("Error: Could not open webcam.")
    sys.exit(0)

print("Press 'q' to stop recording.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    key = cv2.waitKey(1)
    if key == ord('r'):
        recording = not recording
        if recording:
            print("Recording started.")

    if recording:
        if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) >= 1:
            cv2.destroyWindow('frame')
        out.write(frame)

        # Display the frame
        cv2.imshow('Recording', frame)

    # Press 'q' to quit
    if key & 0xFF == ord('q'):
        break

    if not recording:
        # Display the frame
        cv2.imshow('frame', frame)

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()