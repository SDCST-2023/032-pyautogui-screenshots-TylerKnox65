#!python3
import pyautogui
import time

"""
locateOnScreen :
find the location of your image and gives the location of the box as a tuple:
(left,top,width,height) 
"""
location = pyautogui.locateOnScreen('assets/winIcon.png')
print("locateOnScreen:", location)

"""
locateCenterOnScreen :
find the location of your image and gives the location of the center coordinate as a tuple:
(x,y) 
when it is a coordinate, you can move the mouse there
"""

location = pyautogui.locateCenterOnScreen('assets/winIcon.png')
print("locateCenterOnScreen:",location)

"""
locateAllOnScreen :
finds all the occurrences of the image and creates a list of tuples that are (left,top,width,height)
It's actually not a list, but something called a generator that we can convert to a list
"""
mylist = location = pyautogui.locateAllOnScreen('assets/winIcon.png')
print("locate all found (as generator):",mylist)
converted = list(mylist)
print("locate all found (as list):",converted)




