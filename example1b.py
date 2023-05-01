#!python3
import pyautogui
"""
confidence: sometimes you want to allow for inexact matches due to pixelation
You can specify how much of a match from 0-100% (0-1.0) you want.
90% match is 0.9
It does not speed up the search but might allow you to find matches that are sometimes not caught
"""

x = pyautogui.locateCenterOnScreen('assets/winIcon.png',region=(0,800,100,100), confidence=0.9)
print("found at",x)
