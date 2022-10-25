import cv2 
from skimage.filters import sobel, gaussian, threshold_local, try_all_threshold, threshold_isodata
from skimage.color import rgb2gray, rgba2rgb
import numpy as np

def read_image(path):
    img = cv2.imread(path)

    return img


def make_mask(img):
    img_blur = gaussian(img, sigma=1.5, channel_axis=2)
    img_blur_gray = rgb2gray(img_blur)
    thresh_isodata = threshold_isodata(img_blur_gray)
    res_isodata = img_blur_gray <= thresh_isodata

    return res_isodata


def contours(img):
    contours, tmp = cv2.findContours(image=img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    return contours  