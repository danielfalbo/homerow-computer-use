# /// script
# dependencies = [
#   "pyautogui",
# ]
# ///

import pyautogui

def trigger_homerow():
    pyautogui.hotkey('command', 'shift', 'space')

def main():
    trigger_homerow()

if __name__ == '__main__':
    main()
