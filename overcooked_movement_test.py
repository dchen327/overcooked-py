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
    """ Moves in the direction (up, down, left, right), total movement is 1 tile """
    pyautogui.keyDown(direction)
    sleep(0.15)
    pyautogui.keyUp(direction)


def dash(direction):
    """ Dashes in the direction (up, down, left, right), total movement is 3 tiles """
    pyautogui.keyDown(direction)
    sleep(0.05)
    pyautogui.keyDown('shift')
    pyautogui.keyUp(direction)
    pyautogui.keyUp('shift')

def pickup_drop():
    """ Pick up/drop item """
    pyautogui.press('space')


def chop_throw():
    """ Chop/throw """
    pyautogui.press('j')


if __name__ == '__main__':
    alt_tab()
    for _ in range(10):
        pickup_drop()
        dash('left')
        chop_throw()
        dash('right')
    alt_tab()