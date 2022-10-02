import cv2


# Load pre-trained data on frontal faces from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

# Choose an image to use to detect faces from, and convert it to grayscale
img1 = cv2.imread("images/faces1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coords = trained_face_data.detectMultiScale(img1)
print(face_coords)

# Display the images
#cv2.imshow("Face Detector", img1)
cv2.waitKey()  # Wait for keyboard input before closing the image


# Confirm program is up and running
print("Program successfully exited...")
