"""
=========================================
 Comment     : UWSCの関数をなるべくそのまま
 　　　　　　　 使えるようにしたクラス
=========================================
 Display Dpl : 800x600 or 1366x768
=========================================
 Copy Right (C) 2019 All Right Reserved.
   @author k.kawabata @kawaken1025
     Create Date : 2019/03/28
=========================================
"""
import pyautogui
import cv2
import win32gui

class Uwsc:

    """
    Comment : UWSC準拠のKBD関数
    Param   : $1 : self
              $2 : 押すキー文字列
              $3 : キーを押すタイプ 0 = 1回 , 1 = 押しっぱなし, 2 = 離す
              $4 : 前回命令から何ミリ秒に押すか
    Return  : None
    備考    :
    """
    def KBD(self, key, type, time):
        _time = time / 1000 # ミリ秒から秒へ変換
        if type == 0:
            pyautogui.press(  key, interval = _time)
        elif type == 1:
            pyautogui.keyDown(key, interval = _time)
        elif type == 2:
            pyautogui.keyUp(  key, interval = _time)

    """
    Comment : UWSC準拠のBTN関数
    Param   : $1 : self
              $2 : 押すマウスの方向文字列(right or left)
              $3 : キーを押すタイプ 0 = 1回 , 1 = 押しっぱなし, 2 = 離す
              $4 : 押すx座標
              $5 : 押すy座標
              $6 : 前回命令から何ミリ秒に押すか
    Return  : None
    備考    :
    """
    def BTN(self, key, type, xs, ys, time):
        _time = time / 1000 # ミリ秒から秒へ変換
        pyautogui.click(x=xs, y=ys, button=key, interval=_time)

    """
    Comment : UWSC準拠の1回クリック専用BTN関数
    Param   : $1 : self
              $2 : 押すマウスの方向文字列(right or left)
              $3 : 押すx座標
              $4 : 押すy座標
              $5 : 前回命令から何ミリ秒に押すか
    Return  : None
    備考    :
    """
    def BTN(self, key, xs, ys, time):
        _time = time / 1000 # ミリ秒から秒へ変換
        pyautogui.click(x=xs, y=ys, button=key, interval=_time)

    """
    Comment : UWSC準拠の画像認識関数(完全一致)
    Param   : $1 : self
              $2 : 認識対象となる画像のパス
              $3 : 使ってない
              $4 : 開始x座標
              $5 : 開始y座標
              $6 : 終了x座標
              $7 : 終了y座標
    Return  : 完全一致する画像があった   : True
              完全一致する画像がなかった : False
    備考    :
    """
    def chkimg(self, picPath, transFlag, x1, y1, x2, y2):
        im = pyautogui.locateOnScreen(picPath, region=(x1 , y1, x2, y2))
        if im is None:
            return False

        return True

    """
    Comment : UWSC準拠の画像認識関数(テンプレートマッチング)
    Param   : $1 : self
              $2 : 認識対象となる画像のパス
              $3 : 使ってない
              $4 : 開始x座標
              $5 : 開始y座標
              $6 : 終了x座標
              $7 : 終了y座標
              $8 : あいまいさ 0.0 ~ 1.0
    Return  : 完全一致する画像があった   : True
              完全一致する画像がなかった : False
    備考    :
    """
    def chkimg(self, picPath, transFlag, x1, y1, x2, y2, threshold):
        im = pyautogui.locateOnScreen(picPath, region=(x1 , y1, x2, y2), confidence=threshold)
        if im is None:
            return False

        return True

    """
    Comment : ウィンドウ位置の変更
    Param   : $1 : self
              $2 : ウィンドウクラス名
              $3 : ウィンドウ名
              $4 : ウィンドウを置きたい開始x座標
              $5 : ウィンドウを置きたい開始y座標
    Return  : 正常 : 0
              異常 : 1
    備考    :
    """
    def ACW(self, windowClassName ,windowName , xs , ys):
        hWnd = win32gui.FindWindow(windowClassName , None)
        if hWnd is not 0:
            win32gui.SetForegroundWindow(hWnd)
        else:
            return 1;
        cv2.moveWindow(windowName, xs, ys)
        return 0;

