#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Code to read, write, display an image.

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
                                      Mainly for ".png" images with transparency background 
                                      Alternatively, we can pass integer value -1 for this flag.

        Returns:
        numpy.ndarray, Numpy n-dimensional array matrix for read image.
    '''

    # opencv function to read an image
    img_array = cv2.imread(img, flag)

    return img_array


def write(output_image, img_array):
    '''
        Function to write an image.

        Arguments:
        img_array -- numpy.ndarray, Numpy n-dimensional array matrix of a read image.
        output_image -- str, output image name to be stored. 
                        The filename must include image format like ".jpg", ".png", etc. 

        Returns:
        <None>
    '''

    # opencv function to write an image
    cv2.imwrite(output_image, img_array)


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

display("Color", img_color)

write("color.jpg", img_color)

# For gray scale image
img_gray = read("messi.jpg", 0)

display("Gray Scale", img_gray)

write("gray_scale.jpg", img_gray)

# For alpha channel image
img_alpha = read("messi.jpg", -1)

display("Aplha", img_alpha)

write("alpha.jpg", img_alpha)


# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
