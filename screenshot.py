import pyautogui
import time
import keyboard
import win32api
import os

win32api.MessageBox(0, 'Press "s" to take screenshot, "d" to delete all, "q" to exit', 'Instruction')

def active_window_screenshot(active_window: object) -> None:
    # active_window.topleft = (0,0) // moves window to the left corner
    active_window_region = (active_window.left, active_window.top, active_window.right, active_window.bottom)
    active_window.activate()
    t = time.localtime()
    pyautogui.screenshot(fr'images/screenshot{t.tm_hour}{t.tm_min}{t.tm_sec}.png',region = active_window_region)


def main() -> None:
    count = 0
    while(True):
        if keyboard.is_pressed('s'):
            count+=1
            print(f'Took screenshot {count} {'time' if count == 1 else 'times'}')
            active = pyautogui.getActiveWindow()
            active_window_screenshot(active_window=active)
            time.sleep(1)
        if keyboard.is_pressed('d'):
            cur_time = time.localtime()
            win32api.MessageBox(0, 'Press "y" to delete all or "n" to terminate', 'Confirmation')
            while(True):
                if keyboard.is_pressed('y'):
                    dir_list = os.listdir('./images')
                    for each in dir_list:
                        os.remove(fr'./images/{each}')
                    win32api.MessageBox(0, 'Deleted all screenshots', 'Notification')    
                    break    
                if keyboard.is_pressed('n'): 
                    break       
                if ((time.localtime().tm_sec - cur_time.tm_sec) > 5):
                    print('Terminated task due to inactivity')
                    break
        if keyboard.is_pressed('q'):
            win32api.MessageBox(0, 'Application Closed', 'Notification')
            print('Application terminated')
            return
        

        continue

main()



