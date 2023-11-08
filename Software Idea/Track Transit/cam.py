import cv2

# Define the line (y-coordinate) where people will cross
crossing_line = 300

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)  # Use 0 for default webcam, or replace with video file path

passenger_count = 0
direction = None  # Variable to keep track of direction (0 for up, 1 for down)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect pedestrians
    boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw bounding boxes around detected pedestrians
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Check if the center of the detected person is near the crossing line
        center = (x + w//2, y + h)
        if abs(center[1] - crossing_line) < 10:
            if center[1] < crossing_line and direction != 0:
                direction = 0  # Person is moving up
                passenger_count += 1
            elif center[1] > crossing_line and direction != 1:
                direction = 1  # Person is moving down
                passenger_count += 1

    # Draw the crossing line
    cv2.line(frame, (0, crossing_line), (frame.shape[1], crossing_line), (0, 0, 255), 2)

    # Display the frame with bounding boxes and crossing line
    cv2.imshow('Passenger Count', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Total Passenger Count: {passenger_count}")
