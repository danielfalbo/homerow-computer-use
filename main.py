# /// script
# dependencies = [
#   "pyautogui",
#   "pillow",
#   "google-genai",
# ]
# ///

import os
import time
import pyautogui
from google import genai

def trigger_homerow():
    pyautogui.hotkey('command', 'shift', 'space')

def take_screenshot():
    return pyautogui.screenshot()

def get_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-3-flash')

def ai_gen(contents, client=genai.Client()):
    return client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents
    ).text

def press(keys):
    pyautogui.write(keys, interval=0.1)
    pyautogui.press('enter')

CTX_PROMPT = """
You got an image attachment.
The image is a macOS screenshot.
The screenshot comes with keyboard shortcuts hintg
on top of buttons.
"""

is_homerow_trigger = lambda r: len(r) < 5

ACTION_LOOP = [
("""
You should be seeing the "public pages" pane
of notion.so settings.

Your job is to return the shortcut hint characters combination
for the three dots which are settings of the first published page
listed.

Return the character combination and nothing more.

Example: "AK".
""", is_homerow_trigger),

("""
We are in the "public pages" sections of notion.so settings.
We just clicked on the 3 dots of an entry, you should now see options
"copy link", "view", "settings". We want to click on "settings".

Return the character combination and nothing more.

Example: "AK".
""", is_homerow_trigger),

("""
We are in the "public pages" sections of notion.so settings.
We just opened the floating modal panel of an entry's settings.
We want to unpublish this setting.

We want to click on "unpublish".

Return the character combination and nothing more.

Example: "AK".
""", is_homerow_trigger),

("""
We are in the "public pages" sections of notion.so settings.
We just opened the floating modal panel of an entry's settings.
We want to confirm unpublishing.

We want to click on "unpublish".

Return the character combination and nothing more.

Example: "AK".
""", is_homerow_trigger)
]

MAX_ATTEMPTS=3

def act(prompt, is_output_valid):
    print(f'Triggering homerow')
    trigger_homerow()
    print(f'Taking screenshot')
    screenshot = take_screenshot()

    for i in range(MAX_ATTEMPTS):
        print(f'Querying AI: attempt {i}/{MAX_ATTEMPTS}')
        res = ai_gen([f"{CTX_PROMPT} {prompt}", screenshot])
        if is_output_valid(res):
            print(f'Pressing "{res}".')
            press(res)
            time.sleep(1) # pause for 1 second
            return
        else:
            print(f'Invalid response: "{res}".')

def main():
    while True:
        for prompt, is_output_valid in ACTION_LOOP:
            act(prompt, is_output_valid)

if __name__ == '__main__':
    main()
