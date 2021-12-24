import mouse
import time
import keyboard

class AutoClick():

    def AutoClickDef():
        while True:
            if keyboard.is_pressed('b'):
                mouse.click('left')
                print("Pressed")
            time.sleep(0.01)
