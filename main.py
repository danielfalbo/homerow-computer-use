# /// script
# dependencies = [
#   "pyautogui",
#   "pillow",
# ]
# ///

import pyautogui

def trigger_homerow():
    pyautogui.hotkey('command', 'shift', 'space')

def take_screenshot():
    return pyautogui.screenshot()


def main():
    trigger_homerow()
    take_screenshot().save("my_screenshot.png")

if __name__ == '__main__':
    main()
