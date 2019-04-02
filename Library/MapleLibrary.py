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
import pyautogui
import Public.UWSCParser as parser
import time
import Config.Common.KeySetting as commonKey
 
class MapleLibrary:
    testS = 0

    # コンストラクタ
    def __init__(self):
        # インスタンス間で共通のUWSC移行クラスのuwscインスタンスを生成
        self.uwsc = parser.UWSCFunction()
        self.comKey = commonKey.CommonKeySetting()
    
    def checkFamiliarPower(self):
        self.uwsc.KBD(self.comKey.OPEN_FAM_KEY, 0, 300)
        time.sleep(1)
        if self.uwsc.chkimg("../picture/fam500_or_less.bmp",0,0,0,1368,800):
            self.uwsc.KBD(self.comKey.RECV_FAM_KEY,0,10)
            #logger.logWriter(LogLevel.LOG_INFO,Messages.RECOVERY_FAMILIAR_POWER);

        return

