from enum import auto
from re import DEBUG
import mouse
import time
import keyboard
from threading import Thread

class AutoClick():

    Speed = float(0)
    Clicking = True
    key = ""
    def Start():
        AutoClick.key = input("Choose a keyboard key to activate: ")
        AutoClick.ChooseSpeed()

    def AutoClickDef():
        while AutoClick.Clicking:
            if AutoClick.Clicking & keyboard.is_pressed(AutoClick.key):
                mouse.click('left')
            time.sleep(1/AutoClick.Speed)

    def ChooseSpeed():
        try:
            AutoClick.Speed = float(input("clicks per second: "))
        except:
            print("Only numbers are acceptable")
            AutoClick.ChooseSpeed()

    def Close():
        print("Press F to Pause and Unpause")
        while True:
            if keyboard.is_pressed("f"):
                if AutoClick.Clicking == False:
                    print("UnPaused")
                    AutoClick.Start()
                    AutoClick.Clicking = True
                    time.sleep(1)
                elif AutoClick.Clicking == True:
                    print("Paused")
                    AutoClick.Clicking = False
                    time.sleep(1)
            time.sleep(1/15)