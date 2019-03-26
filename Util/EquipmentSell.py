"""
 comment     : 装備を売却する
 param       : None
 return      : None
 ========================================
 Display Dpl : 1366x768[only]
=========================================
 Copy Right (C) 2018 All Right Reserved.
   @author k.kawabata @kawaken1025
     Create Date : 2018/06/11
=========================================
"""
import pyautogui
from time import sleep

def start():
	sellX = 762
	sellY = 307
	pyautogui.click(sellX,sellY,0,200,'right')

