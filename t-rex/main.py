import numpy as np
import cv2
from mss import mss
import time
import pyautogui as ptg
import keyboard

ptg.PAUSE = 0

time.sleep(2)

area_length = 75
time_speed_change = 8
rise = 6
sleep_down = 0.06
jump_was = False
count = 1

ptg.press('up')
start_time = time.time()

with mss() as sct:
    while True:
        diff_time = time.time() - start_time
        
        if diff_time >= time_speed_change:
            start_time = time.time()
            area_length += 15 + rise
            count += 1
        
        if count == 3:
            rise = 2
        elif count == 5:
            rise = 0
            sleep_down = 0.07

        screen = sct.monitors[0]
        screen['left'] = 605
        screen['top'] = 380
        screen['width'] = 750
        screen['height'] = 54

        img = np.array(sct.grab(screen))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        if not(jump_was) and not(np.all(img[:30, 60:area_length])):
            ptg.press('up')
            time.sleep(0.2)
            
            ptg.keyDown('down')  
            ptg.sleep(sleep_down)
            ptg.keyUp('down') 

            jump_was = True
        else:
            time.sleep(0.01)
            jump_was = False
        
        #cv2.imwrite("rex.png", img)
        
        #Если нажата клавиша 'q', завершаем программу
        if keyboard.is_pressed('q'):
            break
        
cv2.destroyAllWindows()