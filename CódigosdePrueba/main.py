import cv2
import numpy as np


def sobreponer():
    img1 = cv2.imread('ralph.jpg')
    img2 = cv2.imread('logo.png')

    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    # cv2.imshow("ROI", roi)

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # color of image 2 converted to gray
    # cv2.imshow("Escala grises", img2gray)
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("threshold inverted", mask)

    mask_inv = cv2.bitwise_not(mask)
    #cv2.imshow("mask_inv", mask_inv)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    cv2.imshow("img1_bg", img1_bg)

    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    #cv2.imshow("img2_fg", img2_fg)

    dst = cv2.add(img1_bg, img2_fg)
    #cv2.imshow("dst", dst)

    img1[0:rows, 0:cols] = img1_bg
    cv2.imshow('res', img1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sobreponer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
