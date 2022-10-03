# Program to detect faces in images
# Modify original image at line 7
import cv2


# Video source to use - cv2.VideoCapture(0) for default webcam
# To use a camera: - set use_camera to True (line 11)
#                  - set cv2.VideoCapture() to the right value (default camera is 0) (line 12)
# To use a video : - set use_camera to False (line 11)
#                  - set video_to_use to the right video filename (line 13)
use_camera = False
source_to_use = cv2.VideoCapture(0)
video_to_use = cv2.VideoCapture("videos/normal_clip.mp4")

# Load pre-trained data on frontal faces from OpenCV (Haar Cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "algos/haarcascade_frontalface_default.xml")

# Iterate through the frames
while True:
    # Read the current frame
    successful_frame, frame = source_to_use.read() if use_camera else video_to_use.read()

    # Make sure that the frame was captured
    if use_camera and not successful_frame:
        print("Error: could not capture frame")
        break

    # Convert the image to a grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coords = trained_face_data.detectMultiScale(grayscale_img)

    # Draw a rectangle around each detected face
    for x, y, w, h in face_coords:
        #cv2.rectangle({IMAGE}, (x, y), (width, heigth), BGR(), THICKNESS)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the images
    frame = cv2.resize(frame, (960, 540))
    cv2.imshow("Face Detector (Escape to exit)", frame)

    # Wait for keyboard input before closing the image for a millisecond only
    key = cv2.waitKey(1)

    # Check if user pressed on the escape key, or q/Q (quit program)
    if key == 27 or key == 81 or key == 113:
        print("Exiting program...")
        break

# Release the camera if required
if use_camera:
    source_to_use.release()

# Confirm program is up and running
print("Program successfully exited...")
