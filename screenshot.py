import pyautogui
import time
import keyboard
import win32api
import os
from PIL import ImageGrab

win32api.MessageBox(0, 'Press "ctrl+s" to take screenshot, "ctrl+q" to exit', 'Instruction')

"""
def main() -> None:
    count: int = 0
    while(True):
        if keyboard.is_pressed('s'):
            count+=1
            print(f'Took screenshot {count} {'time' if count == 1 else 'times'}')
            
            active_window_screenshot()
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
"""

def timer(amount: int) -> None:
     while amount > 0:
          print(f'Task will be performed in {amount} {"second" if amount == 1  else "seconds"}')
          time.sleep(1)
          amount-= 1
"""
     
         

def delete_all():
    win32api.MessageBox(0, 'Press "y" to delete all or "n" to terminate', 'Confirmation')
    keyboard.add_hotkey('ctrl+y', delete)
    keyboard.add_hotkey('ctrl+n', quit)
    timer(4)
    # keyboard.remove_hotkey('ctrl+y')
    # keyboard.remove_hotkey('ctrl+n')
"""    

def active_window_screenshot() -> None:
    # active_window.topleft = (0,0) // moves window to the left corner
    active: object = pyautogui.getActiveWindow()
    t: object = time.localtime()
    # Getting active region and adjusting it
    active_window_region = (active.left+7, active.top, active.right-7, active.bottom-7)
    print(f'Window: {active.title}, Bbox: {active_window_region}')
    screenshot: object = ImageGrab.grab(bbox=active_window_region)
    # screen = pyautogui.screenshot(region = active_window_region)
    path_name: str = fr'images/screenshot{t.tm_hour}{t.tm_min}{t.tm_sec}.png'
    # Saving screenshot
    try:
        screenshot.save(path_name)
    except FileNotFoundError:
        os.mkdir('images')
        print('Created directory images')
        screenshot.save(path_name)

"""
def delete():
        print('delete pressed')
        dir_list = os.listdir('./images')
        for each in dir_list:
            os.remove(fr'./images/{each}')
        win32api.MessageBox(0, 'Deleted all screenshots', 'Notification')
"""
def exiting() -> None:
    print('Exit was pressed')
    timer(3)
    print('Bye-Bye')
    os._exit(0)

def main() -> None:
    keyboard.add_hotkey('ctrl+s', active_window_screenshot)
    # keyboard.add_hotkey('ctrl+d', delete)
    keyboard.add_hotkey('ctrl+q', exiting)
    keyboard.wait()

if __name__ == "__main__":
    main()



