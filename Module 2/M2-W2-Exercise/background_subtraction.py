import numpy as np
import cv2


bg1_image = cv2.imread(
    'Module 2\\M2-W2-Exercise\\Image data\\GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('Module 2\\M2-W2-Exercise\\Image data\\Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread(
    'Module 2\\M2-W2-Exercise\\Image data\\NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    difference = cv2.absdiff(bg_img, input_img)
    diff = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    return diff


def compute_binary_mask(difference_single_channel):
    _, difference_binary = cv2.threshold(
        difference_single_channel, 10, 255, cv2.THRESH_BINARY)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    binary_mask_3_chieu = cv2.merge([binary_mask, binary_mask, binary_mask])
    output = np.where(binary_mask_3_chieu == 255, ob_image, bg2_image)
    return output


result = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('Replaced art', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
