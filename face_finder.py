# Program to detect faces in images
# Modify original image at line 7
import cv2


# Image to use
image_to_use = "images/face1.jpg"

# Load pre-trained data on frontal faces from OpenCV (Haar Cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "algos/haarcascade_frontalface_default.xml")

# Choose an image to use to detect faces from, and convert it to grayscale
img = cv2.imread(image_to_use)
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coords = trained_face_data.detectMultiScale(grayscale_img)

# Draw a rectangle around each detected face
for x, y, w, h in face_coords:
    #cv2.rectangle({IMAGE}, (x, y), (width, heigth), BGR(), THICKNESS)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the images
num_faces = len(face_coords)
print("{x} faces detected.".format(x=num_faces) if num_faces >
      1 else "{x} face detected.".format(x=num_faces))
img = cv2.resize(img, (960, 540))
cv2.imshow("Face Detector", img)

# Wait for keyboard input before closing the image
cv2.waitKey()


# Confirm program is up and running
print("Program successfully exited...")
