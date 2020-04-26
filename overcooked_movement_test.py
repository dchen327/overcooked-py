import pyautogui
from time import sleep

pyautogui.PAUSE = 0  # no delay between clicks

directions = {
    'N': 'up',
    'E': 'right',
    'S': 'down',
    'W': 'left',
    'NE': 'up,right',
    'SE': 'down,right',
    'SW': 'down,left',
    'NW': 'up,left',
}


def alt_tab():
    """ Switch to recent window """
    sleep(.5)
    pyautogui.keyDown('alt')
    sleep(.3)
    pyautogui.press('tab')
    sleep(.3)
    pyautogui.keyUp('alt')


def move(direction):
    """ Moves in the direction (up, down, left, right), total movement is 1 tile """
    pyautogui.keyDown(direction)
    sleep(0.14)
    pyautogui.keyUp(direction)


def dash(direction):
    """ Dashes in the direction (up, down, left, right), total movement is 3 tiles """
    if len(direction) == 1:  # N, S, E, W
        pyautogui.keyDown(directions[direction])
        sleep(0.15)
        # pyautogui.keyDown('shift')
        pyautogui.press('shift')
        pyautogui.keyUp(directions[direction])
        # pyautogui.keyUp('shift')
    else:  # NE, SE, SW, NW
        d1, d2 = directions[direction].split(',')
        pyautogui.keyDown(d1)
        pyautogui.keyDown(d2)
        sleep(0.2)
        pyautogui.press('shift')
        pyautogui.keyUp(d2)
        pyautogui.keyUp(d1)
        pyautogui.keyUp('shift')


def pickup_drop():
    """ Pick up/drop item """
    pyautogui.press('space')


def chop_throw():
    """ Chop/throw """
    pyautogui.press('j')


if __name__ == '__main__':
    alt_tab()
    sleep(1)
    for _ in range(5):
        dash('NW')
        sleep(1)
        dash('SE')
        sleep(1)
    alt_tab()