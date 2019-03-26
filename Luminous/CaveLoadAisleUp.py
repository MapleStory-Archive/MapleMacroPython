"""
 Map Name    : アルカナ ケーヴロードの通路(上)
=========================================
 Mob Name    : 悲嘆の精霊
 Mob Level   : 239
 Mob HP      : 312,451,200
 Mob Exp     : 462,670
=========================================
 Mob Name    : 不調和の精霊
 Mob Level   : 240
 Mob HP      : 318,873,600
 Mob Exp     : 470,824
=========================================
 comment     : None
 param       : None
 return      : None
 ========================================
 Display Dpl : 800x600 or 1366x768
=========================================
 Copy Right (C) 2018 All Right Reserved.
   @author k.kawabata @kawaken1025
     Create Date : 2018/05/26
=========================================
"""
import os, sys
import pyautogui
from time import sleep
import Common.Skill.Skill as skill
import configparser
import Common.ConstDefine as const
import Library.MapleLibrary as lib

LUMINOUS_INI_PATH = './Config/Luminous/KeySetting.ini'

ini = configparser.ConfigParser()
ini.read(LUMINOUS_INI_PATH, 'UTF-8')

#Skill key Setting
TELEPORT_KEY        = ini.get('Skill', 'TELEPORT_KEY')
REFLECTION_KEY      = ini.get('Skill', 'REFLECTION_KEY')
PSYCHOLOGY_DOOR_KEY = ini.get('Skill', 'PSYCHOLOGY_DOOR_KEY')
PANISHING_KEY       = ini.get('Skill', 'PANISHING_KEY')
ROPE_CONNECT_KEY    = ini.get('Skill', 'ROPE_CONNECT_KEY')
RECOVERY_FAM_KEY    = ini.get('Skill', 'RECOVERY_FAM_KEY')
SKILL_MACRO1_KEY    = ini.get('SkillMacro', 'SKILL_MACRO1_KEY')
SKILL_MACRO2_KEY    = ini.get('SkillMacro', 'SKILL_MACRO1_KEY')

"""
testcode

pyautogui.click(1366, 500, 0, 1, 'left')
info = pyautogui.locateOnScreen('test.png')
if info is not None:
    x,y = pyautogui.center(info)
    print("画像認識に成功しました。座標(x,y)=")
    print(type(x))
else:
    print("画像認識に失敗しました。")
"""

def Attack( flapX_Min , flapX_Max , flapY_Min, flapY_Max, moveKey ):
    _equlibrium = False
    flag = True
    #pyautogui.keyDown(moveKey)
    while flag:
        #TODO: lib.urgentCheck()
        yellowPointInfo = lib.chkimgXY('./Picture/yellowPoint.png',0,0,0,800,600)
        print(yellowPointInfo)
        if (yellowPointInfo):
            #x,y = yellowPointInfo
            #if(flapX_Min <= x and x <= flapX_Max and flapY_Min <= y and y <= flapY_Max):
            if(yellowPointInfo):
                print("画像認識に成功しました。座標(x,y)=")
                #print(type(x))

                #pyautogui.keyUp(moveKey)
                return const.flapSuccess
            else:
                print("範囲外")
        if yellowPointInfo is None:
            print("Not Yellow Point.")
            flag = False

        pyautogui.press(REFLECTION_KEY)
        sleep(0.2)
        pyautogui.press(REFLECTION_KEY)
        sleep(0.2)
        pyautogui.press(TELEPORT_KEY)
        sleep(0.2)
        pyautogui.press(TELEPORT_KEY)

def start():
    print("CaveLoadAisleUp in")

    returnCode = Attack(const.CAVELOAD_LEFT_X_MIN,const.CAVELOAD_LEFT_X_MAX,const.CAVELOAD_LEFT_Y_MIN,const.CAVELOAD_LEFT_Y_MAX,'left')
    if returnCode != 0:
        return const.MAPLE_ERROR

    returnCode = Attack(const.CAVELOAD_RIGHT_X_MIN,const.CAVELOAD_RIGHT_X_MAX,const.CAVELOAD_RIGHT_Y_MIN,const.CAVELOAD_RIGHT_Y_MAX,'right')
    if returnCode != 0:
        return const.MAPLE_ERROR

    #return const.MAPLE_SUCCESS