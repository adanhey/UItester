import os
import time
import numpy
import cv2
from PIL import Image


def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree += 1
    degree /= len(hist1)
    return degree


def picture_similarity(image1, image2, size=(256, 256)):
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    image1 = cv2.cvtColor(numpy.asarray(image1), cv2.COLOR_RGB2BGR)
    image2 = cv2.cvtColor(numpy.asarray(image2), cv2.COLOR_RGB2BGR)
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data /= len(sub_image1)
    return int(sub_data * 100)


def result_compare(caseNO, picName, picPath):
    result = 100
    for root, dirs, files in os.walk("E://interface_tool/picResult"):
        for dice in dirs:
            if caseNO == str(dice):
                for root2, dirs2, pic in os.walk(f"E://interface_tool/picResult/{dice}"):
                    if pic[0] == picName:
                        result = picture_similarity(f"E://interface_tool/picResult/{dice}/{picName}", picPath)
    return result


if __name__ == "__main__":
    # img1_path = "4.jpeg"
    # img2_path = "6.jpeg"
    # result = picture_similarity(img1_path, img2_path)
    # print(f"相似度为：{result}")
    print(result_compare("createAppeal", '4.jpeg', f"E://interface_tool/pic_compare/4.jpeg"))
