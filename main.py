import time
import pyautogui

st = time.time()
#############################################

x, y = pyautogui.position()  # get initial cursor position
time1 = 1 # delay time

while True:
    time.sleep(time1)
    p, q = pyautogui.position() # get cursor position
    if x != p and q != y:
        print(p,q)
        x = p
        y = q
  

#############################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')



