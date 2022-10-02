import cv2


# Load pre-trained data on frontal faces from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

# Choose an image to use to detect faces from, and convert it to grayscale
img = cv2.imread("images/face1.jpg")
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coords = trained_face_data.detectMultiScale(grayscale_img)

# Draw a rectangle around the face
for x1, y1, x2, y2 in face_coords:
    #cv2.rectangle({IMAGE}, (x1, y1), (x2, y2), BGR(), THICKNESS)
    cv2.rectangle(img, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 2)

# Display the images
cv2.imshow("Face Detector", img)
cv2.waitKey()  # Wait for keyboard input before closing the image


# Confirm program is up and running
print("Program successfully exited...")
