import sys
import configparser
import json
import Luminous
import Common.const
import pyautogui
import Library.MapleLibrary as lib
import cv2
import Public.UWSCParser as parser

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
    uwsc = parser.Uwsc()
    uwsc.BTN('left',400,300,500)
    uwsc.KBD('a',0,1000)
    if uwsc.chkimg('./Picture/test.png',0,0,0,2000,1000):
        print (1)
    else:
        print (2)
