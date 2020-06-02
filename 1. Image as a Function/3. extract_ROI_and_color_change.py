#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Code to extract ROI  from an image, Paste ROI to an image, change color spaces of an image.

    @author: AatishLanghee

"""

# Import necessary libraries and packages
import cv2


def read(img, flag):
    '''
        Function to read an image.

        Arguments:
        img -- str, image path.
        flag -- int or str, specifies the way in which image should be read.
                It’s default value is cv2.IMREAD_COLOR.

                All three types of flags are described below:

                cv2.IMREAD_COLOR: It specifies to load a color image.
                                  It is the default flag. Alternatively, we can pass integer value 1 for this flag.

                cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode.
                                      Alternatively, we can pass integer value 0 for this flag.

                cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha (transparency) channel.
                                      Mainly for ".png" images with transparency background.
                                      Alternatively, we can pass integer value -1 for this flag.

        Returns:
        numpy.ndarray, Numpy n-dimensional array matrix for read image.
    '''

    # opencv function to read an image
    img_array = cv2.imread(img, flag)

    return img_array


def extract_roi(img_array, y_cord_start, y_cord_end, x_cord_start, x_cord_end):
    '''
        Function to extract Region of Interest (ROI) from an image.
        Here we are using slicing operator to crop a ROI image.

        Arguments:
        img_array -- numpy.ndarray, Numpy n-dimensional array matrix of a read image.
        y_cord_start -- int, starting co-ordinate value along Y axis (Ymin)
        y_cord_end -- int, ending co-ordinate value along Y axis (Ymax)
        x_cord_start -- int, starting co-ordinate value along X axis (Xmin)
        x_cord_end -- int, ending co-ordinate value along X axis (Xmax)

        Returns:
        numpy ndarray of cropped image based on passed co-ordinates (ROI image).
    '''

    return img_array[y_cord_start:y_cord_end, x_cord_start:x_cord_end]


def paste_roi(img_array, y_cord_start, y_cord_end, x_cord_start, x_cord_end, roi_img):
    '''
        Function to paste cropped Region of Interest (ROI) on an image.
        Here we are using slicing operator to paste a ROI on image.

        Note:  Dimensions( of rectangle) of ROI (cropped) image and location where
             we are pasting our ROI image should be same.

        Arguments:
        img_array -- numpy.ndarray, Numpy n-dimensional array matrix of a read image.
        y_cord_start -- int, starting co-ordinate value along Y axis (Ymin)
        y_cord_end -- int, ending co-ordinate value along Y axis (Ymax)
        x_cord_start -- int, starting co-ordinate value along X axis (Xmin)
        x_cord_end -- int, ending co-ordinate value along X axis (Xmax)

        Returns:
        numpy ndarray, ROI is paste on image at given co-ordinates.
    '''

    img_array[y_cord_start:y_cord_end, x_cord_start:x_cord_end] = roi_img

    return img_array


def convt_color(img_array, flag):
    '''
        Function to convert an image from one color space to different color space.

        Arguments:
        img_array -- numpy.ndarray, Numpy n-dimensional array matrix of a read image.
        flag -- str, Color space conversion code. By default opencv read color image in BGR format.
                1) BGR2RGB = to change from BGR to RGB color space image.
                2) BGR2GRAY = to change from BGR to Gray scale image.
                3) BGR2HSV = to change from BGR to HSV color space image.

        Returns:
        numpy ndarray of changed color space image.
    '''
    # Change color space conversion code to required code.
    code = None

    if flag == "BGR2RGB":
        code = cv2.COLOR_BGR2RGB
    elif flag == "BGR2GRAY":
        code = cv2.COLOR_BGR2GRAY
    elif flag == "BGR2HSV":
        code = cv2.COLOR_BGR2HSV

    # openCV function to change color space
    convt_img = cv2.cvtColor(img_array, code)

    return convt_img


def display(window_name, img_array):
    '''
        Function to display an image.

        Arguments:
        img_array -- numpy.ndarray, Numpy n-dimensional array matrix of a read image.
        window_name -- str, Name of the window in which image to be displayed.

        Returns:
        <None>
    '''

    # opencv function to display an image
    cv2.imshow(window_name, img_array)


# For color image
img_color = read("messi.jpg", 1)

display("color", img_color)

# For BGR to GRAY image
bgr2gray = convt_color(img_color, "BGR2GRAY")

display("gray", bgr2gray)

# To extract ROI from an Image
roi_img = extract_roi(img_color, 100, 300, 200, 400)

display("roi_img", roi_img)

paste_img = paste_roi(img_color, 50, 250, 150, 350, roi_img)

display("paste_img", paste_img)


# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
