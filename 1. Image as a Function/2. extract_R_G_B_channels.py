#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Code to extract R,G,B channel values from an image.

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


def extract_values(img_array, y_cord, x_cord, channel_index):
    '''
        Function to extract values at given co-ordinates or get different channel image such as R channel, G channel, or B channel.

        Arguments:
        img_array -- numpy.ndarray, Numpy n-dimensional array matrix of a read image.
        y_cord -- int for a single point or for multiple points use slice operator with start point and end point,
                        It is the row co-ordinates of an image along y axis.
        x_cord -- int for a single point or multiple points use slice operator with start point and end point,
                        It is the column co-ordinates of an image along x axis.
        channel_index -- int , It is the index value for your color.
                         OpenCV read image in BGR format, hence index values are as follows:
                        B = 0
                        G = 1
                        R = 2

        Returns:
        numpy ndarray channel image in case of sliced image or color value in case of Y and X co-ordinates  are given.
    '''

    return img_array[y_cord, x_cord, channel_index]


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


def SliceMaker():
    '''
        Function to create slice object to use it as a slicing operator.
        We can not pass slicing operator directly as argument to the function.

        Returns:
        Instance of slice object make_slice, can be used as slicing operator.
    '''

    class SliceMaker(object):
        '''
            Class of a SliceMaker
        '''

        def __getitem__(self, item):
            '''
               __getitem__ method of class SliceMaker

               Arguments:
               item -- int, takes passed item as a input

               Returns:
               item -- int
           '''
            return item

    # Created a object instance of SliceMaker class
    make_slice = SliceMaker()

    return make_slice


# For color image
img_color = read("messi.jpg", 1)

# sliced image with [:] all rows and [:] all columns, sliced image function is used to get sliced image from original image.
B_channel_ = extract_values(img_color, SliceMaker()[:], SliceMaker()[:], 0)


# For particular Region of Interest in image, sliced using different start and end points.
# B_channel_ = extract_values(img_color, SliceMaker()[
#     100: 200], SliceMaker()[200: 300], 0)

# Y and X co-ordinates given
B_channel = extract_values(img_color, 187, 332, 0)  # 71
G_channel = extract_values(img_color, 187, 332, 1)
R_channel = extract_values(img_color, 187, 332, 2)
print(B_channel)

display("Color", B_channel_)


# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
