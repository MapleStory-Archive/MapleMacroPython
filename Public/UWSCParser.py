def KBD(key, type, time):
    _time = time / 1000
    if type == 0:
        pyautogui.press(key, interval = _time)
    elif type == 1:
        pyautogui.keyDown(key, interval = _time)
    elif type == 2:
        pyautogui.keyUp(key, interval = _time)


def BTN(key, type, xs, ys, time):
	_time = time / 1000
	pyautogui.click(x = xs , y = ys , button = key, interval = _time)


def chkimg(picPath, no_value, x1, y1, x2, y2):
    im = pyautogui.locateOnScreen(picPath, region=(x1 , y1, x2, y2))
    if im is None:
        return False

    return True