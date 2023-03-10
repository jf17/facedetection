import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Fliping(mirroring) the image
    img = cv2.flip(img, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    key = cv2.waitKey(30) & 0xff

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# Release the VideoCapture object
cap.release()
