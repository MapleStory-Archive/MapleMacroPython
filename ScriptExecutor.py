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
    #iniファイルから値を取得する
    ini = configparser.ConfigParser()
    ini.read('./Config/ScriptName.ini', 'UTF-8')

    #コマンドラインからJSON文字列を取得する
    #inputJson = args[1]
    #jsonDict = json.load('inputJson','r')
    print("ScriptExecutor.y in")
    if args[1] == "UWSC":
        print("exec UWSC Mode")
        exit()
    
    jsonDict = json.loads('{"MapleRequestBody":{"Job":"Luminous","Region":"Arcana","ScriptName":"CaveLoadAisleUp"}}')
    jsonJobValue = jsonDict[const.MAPLE_REQUEST_BODY][const.JOB]
    jsonScriptName = jsonDict[const.MAPLE_REQUEST_BODY][const.SCRIPT_NAME]
    execCmd = jsonJobValue + '.' + jsonScriptName + '.start()'
    print(execCmd)
    #eval(execCmd)
