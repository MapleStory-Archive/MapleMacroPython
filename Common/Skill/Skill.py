"""
 comment     : ルミナス スキル使用
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
import pyautogui
from time import sleep

SKILL_MACRO1 = 'g'
SKILL_MACRO2 = 'h'

def useSkill():
    pyautogui.press(SKILL_MACRO1)
    sleep(0.3)
    pyautogui.press(SKILL_MACRO2)
    sleep(0.3)
