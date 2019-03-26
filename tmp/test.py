import cv2
from PIL import ImageGrab
import time
import numpy as np
import pylab as plt

ImageGrab.grab(bbox=(0, 0, 1000, 350)).save("CVMaple.png")

#coding:utf-8
import cv2
import numpy as np
#画像をグレースケールで読み込む
img = cv2.imread("CVMaple.png", 0)
temp = cv2.imread("down.png", 0)
#マッチングテンプレートを実行
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
#類似度の設定(0~1)
threshold = 0.3
#検出結果から検出領域の位置を取得
loc = np.where(result >= threshold)
#検出領域を四角で囲んで保存
result = cv2.imread("CVMaple.png")
w, h = temp.shape[::-1]
for top_left in zip(*loc[::-1]):
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
    cv2.imwrite("downss.png", result)
"""
temp = cv2.imread("up.png", 0)
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
for top_left in zip(*loc[::-1]):
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(result,top_left, bottom_right, (100, 0, 0), 2)
    cv2.imwrite("upss.png", result)

temp = cv2.imread("right.png", 0)
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
for top_left in zip(*loc[::-1]):
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(result,top_left, bottom_right, (100, 100, 0), 2)
    cv2.imwrite("rightss.png", result)

temp = cv2.imread("left.png", 0)
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
for top_left in zip(*loc[::-1]):
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(result,top_left, bottom_right, (100, 100, 0), 2)
    cv2.imwrite("legtss.png", result)
"""
"""
#画像をグレースケールで読み込む
img = cv2.imread("CVMaple.png", 0)
temp = cv2.imread("down.png", 0)
#マッチングテンプレートを実行
#比較方法はcv2.TM_CCOEFF_NORMEDを選択
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
#検出結果から検出領域の位置を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
w, h = temp.shape[::-1]
bottom_right = (top_left[0] + w, top_left[1] + h)
#検出領域を四角で囲んで保存
result = cv2.imread("CVMaple.png")
cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
cv2.imwrite("result.png", result)
"""

"""
def main():

    t=127
    matchImg = cv2.imread("./Picture/arrow_d_gray.png")
    inputImg = cv2.imread("./Picture/arrow2.png")
    gray = cv2.cvtColor(inputImg, cv2.COLOR_RGB2GRAY)
    th3 = cv2.Canny(gray, 50, 150)
    #ret,th3 = cv2.threshold(gray, 200, 255, cv2.THRESH_TOZERO_INV)
    #th3 = cv2.bitwise_not(gray)
    #ret,th3 = cv2.threshold(gray, 250, 255, cv2.THRESH_OTSU)
    cv2.imshow('windowname', th3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.bitwise_not(gray, gray)


    return 0
    # グレースケール変換
    #gray1 = cv2.cvtColor(matchImg, cv2.COLOR_RGB2GRAY)
    gray = cv2.cvtColor(inputImg, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("./Picture/arrow.png", gray)
    #マッチングテンプレートを実行
    #w, h = matchImg.shape[::-1]
    w=30
    h=30
    inputImg = cv2.imread("./Picture/arrow.png")
    result = cv2.matchTemplate(inputImg, matchImg, cv2.TM_CCOEFF_NORMED)
    #類似度の設定(0~1)
    threshold = 0.4
    #検出結果から検出領域の位置を取得
    loc = np.where(result >= threshold)
    #検出領域を四角で囲んで保存
    result = cv2.imread("./Picture/arrow.png")
    
    for top_left in zip(*loc[::-1]):
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
        cv2.imwrite("result2.png", result)

main()
"""