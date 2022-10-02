import cv2


# Load pre-trained data on frontal faces from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

# Choose an image to use to detect faces from
img1 = cv2.imread("images/faces1.jpg")

# Display the image
cv2.imshow("Face Detector", img1)

# Wait for keyboard input before closing the image
cv2.waitKey()

# Confirm program is up and running
print("Program successfully exited...")
