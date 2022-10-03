# Face-Detection-App

<p align="center">
  <img src="images/face_finder.JPG">
</p>

The [face_finder.py](https://github.com/z1chh/Face-Detection-App/blob/master/face_finder.py) and [face_detector.py](https://github.com/z1chh/Face-Detection-App/blob/master/face_detector.py) use OpenCV's Haar Cascade algorithm, which uses Haar features (chained) that match a frontal face. The image goes through the classifier and a face is detected if it passes through all of the Haar cascades. This is done for every type, size and location in the image (to detect the faces). This algorithm is pre-trained by OpenCV.

## Face Finder

[face_finder.py](https://github.com/z1chh/Face-Detection-App/blob/master/face_finder.py) takes an image as input, and detects frontal faces in that image.
Detected faces have a green rectangle around them.

### Setup

To change the image used for the face detection algorithm, modify the source image (path) at line 7.

## Face Detector

[face_detector.py](https://github.com/z1chh/Face-Detection-App/blob/master/face_detector.py) detects frontal faces in videos.
Program that detects faces in real-time, for example with a live video.
Detected faces have a green rectangle around them.

### Setup

To change the video source:

- Set the use_camera boolean to True if using a camera (line 11)
- Set the use_camera boolean to False if using a video file (line 11)
- Set the webcam to use (default camera corresponds to 0) (line 12)
- Set the video_to_use variable (update path) (line 13)
