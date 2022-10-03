# Program to detect faces in images
# Modify original image at line 11
import cv2


# Load pre-trained data on frontal faces from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

# Choose an image to use to detect faces from, and convert it to grayscale
img = cv2.imread("images/faces1.jpg")
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coords = trained_face_data.detectMultiScale(grayscale_img)

# Draw a rectangle around each detected face
for x, y, w, h in face_coords:
    #cv2.rectangle({IMAGE}, (x, y), (width, heigth), BGR(), THICKNESS)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the images
img = cv2.resize(img, (960, 540))
cv2.imshow("Face Detector", img)
cv2.waitKey()  # Wait for keyboard input before closing the image


# Confirm program is up and running
print("Program successfully exited...")
