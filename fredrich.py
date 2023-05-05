from numpy import true_divide
import pyautogui as p
import time
from threading import Thread,Lock
from pynput.keyboard import Key, Listener
import os
p.confirm("Run?")
p.hotkey('alt', 'tab')
time.sleep(2)
p.PAUSE = 0.0001


class globalVars():
    pass

G = globalVars() #empty
G.lock = Lock() 
G.value = 0
G.kill = False
#p.FAILSAFE = False


def on_press(key):
    print('{0} pressed'.format(key))
def on_release(key):
    print('{0} release'.format(key))
    if key == Key.shift:
       
        G.kill = True
        os._exit(1)
        






def main():
   
    tree = p.locateCenterOnScreen('assets/greenTree.png', confidence = 0.7)
    money = p.locateCenterOnScreen('assets/yellowMoney.png', confidence = 0.7)
    '''
    if tree != None and money == None:
        x = 0
        while x < 5000:
            p.click(tree)
           
        money = p.locateCenterOnScreen('assets/yellowMoney.png', confidence = 0.7)
    '''

    if tree != None and money != None:
        base = 0
        while True:
            if G.kill:
                G.kill = False
                return
            x = 0
            
            p.moveTo(money)
            while x < 10:
               
                for i in range(100):
                    p.leftClick(tree)
                for i in range(100):
                    p.leftClick(money)
                x += 1
            
            if base == 0:
                
                flor = p.locateCenterOnScreen('assets/florist.png', confidence = 0.7)
            base = 1
            print(flor)
            florList = list(flor)
            print(florList)
           
            for i in range(10):
               
                xcoord = florList[0]
                ycoord = florList[1]
                for i in range(7):
                    for i in range(6):
                      
                        p.click(xcoord, ycoord)
                        xcoord += 250
                
                    p.moveTo(xcoord + 250, ycoord + 30)
                    ycoord += 35
                    for i in range(6):
                    
                        p.click(xcoord, ycoord)
                        xcoord -= 250 


def listenerFunc():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

t = Thread(target=main, args=())
d = Thread(target=listenerFunc, args=())

d.start()
t.start()

def listenerFunc():
    while True:
        with Listener(on_press=on_press,on_release=on_release) as listener:
            listener.join()






