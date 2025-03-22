OPENCV1 project analysis and methods used in code.
Report on Libraries and Techniques Used in the Provided OpenCV Code


Introduction

This document provides a detailed analysis of the OpenCV-based image processing code. The script performs color-based object detection by filtering specific color ranges in an image using the HSV color model. It then applies morphological transformations, contour detection, and object labeling to highlight and classify detected objects. The following sections discuss the libraries used, key functions, and techniques implemented in the script.

image given for the assignment - to identify the red and purple fruits

![image](https://github.com/user-attachments/assets/b2514eac-aa74-4bf9-a3cc-bf422c593fd4)

(I hope you can see this in the final doc cause it is not visible in this preview mode)

1. Libraries Used
   
1.1 OpenCV (cv2)

Purpose: OpenCV is used for image processing tasks such as reading images, resizing, converting color spaces, applying masks, morphological operations, contour detection, and drawing bounding boxes.
Functions Used:

cv2.imread() → Reads an image from the specified path.

cv2.resize() → Resizes the image to a specified dimension.

cv2.cvtColor() → Converts an image from BGR to HSV.

cv2.inRange() → Applies thresholding to filter specific color ranges.

cv2.dilate() → Expands white areas in a binary image to fill gaps.

cv2.erode() → Shrinks white areas to remove small noise.

cv2.bitwise_and() → Applies a mask to an image.

cv2.findContours() → Finds contours (object boundaries) in an image.

cv2.boundingRect() → Computes a bounding rectangle around a detected object.

cv2.putText() → Writes text on an image.

cv2.rectangle() → Draws a rectangle around detected objects.

cv2.imshow() → Displays images in windows.

cv2.waitKey() → Waits for user interaction before closing the window.

cv2.destroyAllWindows() → Closes all OpenCV windows.

1.2 NumPy (numpy)

Purpose: NumPy is used for array manipulations and defining color thresholds.
Functions Used:
np.array() → Defines arrays for HSV color range boundaries.

np.ones() → Creates a kernel (structuring element) for morphological operations.


3. Techniques Used

2.1 HSV Color Filtering
The image is converted from BGR to HSV (Hue, Saturation, Value) using cv2.cvtColor().
cv2.inRange() is used to apply color thresholding, creating a binary mask.
Two sets of HSV thresholds are used to detect red and purple objects.

2.2 Morphological Operations

Dilation (cv2.dilate) → Expands detected objects to fill small holes.
Erosion (cv2.erode) → Removes small white noise by shrinking white areas.
These operations help improve the accuracy of contour detection.

2.3 Contour Detection (cv2.findContours)

Extracts the outer edges of detected objects in the thresholded image.
Uses cv2.RETR_EXTERNAL to retrieve only the external contours.
Uses cv2.CHAIN_APPROX_SIMPLE to remove unnecessary points and optimize memory usage.

2.4 Object Bounding and Labeling

Bounding rectangles are drawn around detected objects using cv2.boundingRect().
Text labels ('RED' and 'PURPLE') are placed above objects using cv2.putText().

2.5 Image Masking (cv2.bitwise_and)

The detected objects are extracted using bitwise operations to remove background pixels.
Ensures that only objects within the color threshold appear in the final image.

2.6 Multiple Image Processing Pipelines

The code processes two separate HSV color filters:

First HSV filter → Detects red objects.

Second HSV filter → Detects purple objects.

Each pipeline performs thresholding, morphological operations, contour detection, and object labeling separately.

4. Process

3.1 Finding the HSV ranges and applying the thresholds

Using the trackbar to change the HSV values in order to find the ranges for the colours we need to detect in the image.
After which we use those HSV values in order to create a mask for both of the images to only get the colours that we need to detect

3.2 Applying different morphological processes 

After which we applied the erosion and dilation operation in that order to reduce the noise as much as possible and to get clear regions within the image for easier process

3.3 Getting rid of the red blob in the image

By applying the findContour() function to find the edges of the regions created in the mask and then applying the area function on them in order to find the area of the regions for the purposes of separating it from the object that we are trying to find i,e the fruits in the image.

3.4 Putting the rectangles around the shape and writing the names

By using the .rectangle and .putText functions to then put the rectangles as well as the text on top of the images for best 
identification

final result

![image](https://github.com/user-attachments/assets/2bff2e5a-2eb8-4749-a673-e56199f6b249)


