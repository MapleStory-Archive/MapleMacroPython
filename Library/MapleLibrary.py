 # comment    : MapleStory Library Class
# param       : None
# return      : None
# ========================================
# Copy Right (C) 2018 All Right Reserved.
#   @author k.kawabata @kawaken1025
#     Create Date : 2018/06/09
#=========================================

import configparser
import cv2
from PIL import ImageGrab
 
def getKeySetting(iniFilePath):
    ini = configparser.ConfigParser()
    ini.read('./config.ini', 'UTF-8')

def chkimgXY(picPath,transFlag,x1,y1,x2,y2):
    #Screen Shot
    ImageGrab.grab((x1, y1, x2, y2)).save('./tmp/ss.png')

    #ImagePicture
    img = cv2.imread("./tmp/ss.png")
    temp = cv2.imread(picPath)

    #TemplateMatching
    match = cv2.matchTemplate(img, temp, cv2.TM_SQDIFF)

    #Get Degree of similarity
    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)

    return min_pt

def chkimg(picPath,transFlag,x1,y1,x2,y2):
#Screen Shot
    ImageGrab.grab((x1, y1, x2, y2)).save('./tmp/ss.png')

    #ImagePicture
    img = cv2.imread("./tmp/ss.png")
    temp = cv2.imread(picPath)

    #TemplateMatching
    match = cv2.matchTemplate(img, temp, cv2.TM_SQDIFF)

    #Get Degree of similarity
    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    x,y = min_pt

    if x1 < x and x < x2 and y1 < y and y < y2:
        return True

    return False