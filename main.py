# /// script
# dependencies = [
#   "pyautogui",
#   "pillow",
#   "google-genai",
# ]
# ///

import os
import pyautogui
from google import genai

def trigger_homerow():
    pyautogui.hotkey('command', 'shift', 'space')

def take_screenshot():
    return pyautogui.screenshot()

def get_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-3-flash')

def ai_gen(client, contents):
    return client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents
    ).text

def main():
    gemini = genai.Client()

    trigger_homerow()
    screenshot = take_screenshot()
    print(ai_gen(gemini, ["what do you see?", screenshot]))

if __name__ == '__main__':
    main()
