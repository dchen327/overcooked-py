import pyautogui
from time import sleep


def alt_tab():
    """ Switch to recent window """
    sleep(.5)
    pyautogui.keyDown('alt')
    sleep(.3)
    pyautogui.press('tab')
    sleep(.3)
    pyautogui.keyUp('alt')


def move(direction, dash=False):
    if dash:
        pyautogui.keyDown(direction)
        sleep(0.2)
        pyautogui.keyDown('shift')
        pyautogui.keyUp(direction)
        pyautogui.keyUp('shift')
    else:
        pyautogui.press(direction)


def dash(direction):
    pyautogui.keyDown(direction)
    sleep(0.2)
    pyautogui.keyDown('shift')
    pyautogui.keyUp(direction)
    pyautogui.keyUp('shift')

if __name__ == '__main__':
    alt_tab()
    sleep(1)
    dash('up')
    sleep(1)
    dash('down')
    alt_tab()