"""
 comment     : ルミナス メイプルユニオン
 param       : None
 return      : None
 ========================================
 Display Dpl : 1366x768 only
=========================================
 Copy Right (C) 2018 All Right Reserved.
   @author k.kawabata @kawaken1025
     Create Date : 2018/05/27
=========================================
"""

import pyautogui
from time import sleep
import Luminous.KeySetting as key

def main():
    print("main")
    print(key.TELEPORT_KEY)

def initPoint():
    pyautogui.keyDown('right')
    for i in range(2):
        pyautogui.press(key.TELEPORT_KEY)
        sleep(0.5)
    pyautogui.keyUp('right')