import sys
import configparser
import json
import Luminous
import Common.ConstDefine as const
import pyautogui
import Library.MapleLibrary as lib
import cv2

class ScriptExecutor():

    #コマンドライン引数の取得
    args = sys.argv

    

    #コマンドラインからJSON文字列を取得する
    #inputJson = args[1]
    #jsonDict = json.load('inputJson','r')
    # print("ScriptExecutor.y in")
    # if args[1] == "UWSC":
    #     print("exec UWSC Mode")
    #     exit()
    
    # jsonDict = json.loads('{"MapleRequestBody":{"Job":"Luminous","Region":"Arcana","ScriptName":"CaveLoadAisleUp"}}')
    # jsonJobValue = jsonDict[const.MAPLE_REQUEST_BODY][const.JOB]
    # jsonScriptName = jsonDict[const.MAPLE_REQUEST_BODY][const.SCRIPT_NAME]
    # execCmd = jsonJobValue + '.' + jsonScriptName + '.start()'
    # print(execCmd)
    #eval(execCmd)
    def KBD(key, type, time):
        _time = time / 1000 
        if type == 0:
            pyautogui.press(key, interval = _time)
        elif type == 1:
            pyautogui.keyDown(key, interval = _time)
        elif type == 2:
            pyautogui.keyUp(key, interval = _time)

    KBD('a',0,100)
    KBD('a',0,100)
    KBD('a',0,100)
    KBD('a',0,100)
    KBD('a',0,100)
    KBD('a',0,100)