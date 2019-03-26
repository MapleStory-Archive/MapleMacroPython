"""
 comment     : コアジェムストーンを分解する
 param       : None
 return      : None
 ========================================
 Display Dpl : 1366x768[only]
=========================================
 Copy Right (C) 2018 All Right Reserved.
   @author k.kawabata @kawaken1025
     Create Date : 2018/05/26
=========================================
"""
import pyautogui
from time import sleep

def breakCore(x,y,rangeNum,plusX,plusY):
	# V_MATRIX [page2] select
	NEXT_PAGE_X = 790
	NEXT_PAGE_Y = 612
	pyautogui.click(NEXT_PAGE_X,NEXT_PAGE_Y,0,1,'left')

	clickX = x
	clickY = y
	#Select all cores in [page2]
	for i in range(rangeNum):
		for RowClick in range(rangeNum):
			pyautogui.click(clickX,clickY,0,1,'left')
			sleep(0.3)
			clickX = clickX + plusX
		clickX = x
		clickY = clickY + plusY
	
def start():
	#1,3,5,7行目
	breakCore(400,220,4,125,135)
	#2,4,6行目
	breakCore(470,280,3,100,120)