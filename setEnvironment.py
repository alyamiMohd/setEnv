import os,pyautogui,time
arr = ['code','chromeServer','gitbash','gitbashServer','gitBashCMD','chromeUdemy','spotify']

def organizeMe(name='',press='',press2='',press3='',press4='',press5='',write=''):
    if name!='':
        os.system(name)
    time.sleep(1)
    pyautogui.keyDown('win')
    pyautogui.press(press)
    if press2 !='':
        pyautogui.press(press2)
    if press3 !='':
        pyautogui.press(press3)
    if press4 !='':
        pyautogui.press(press4)
    if press5 !='':
        pyautogui.press(press5)
    if write !='':
        time.sleep(1)
        pyautogui.keyUp('win')
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.write(write, interval=0.01)
        time.sleep(1)
        pyautogui.press('enter')
    time.sleep(1)
    pyautogui.keyUp('win')
    pyautogui.press('esc')
    time.sleep(1)

def hideMe(write='',name=''):
    if name!='':
        os.system(name)
    time.sleep(1)
    pyautogui.write(str(write), interval=0.01)
    time.sleep(1)
    pyautogui.keyDown('win')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.keyUp('win')

for i in range(len(arr)):
    if arr[i] == 'code':
        organizeMe(name='code',press='left')
    elif arr[i] =='chromeServer':
        organizeMe('chrome','right', 'up', write='localhost:3000')
    elif arr[i] =='gitbash':
        os.startfile(r"C:\Users\aa\Desktop\Git Bash.lnk")
        organizeMe(press='right',press2='down',write="pwd")
    elif arr[i] =='gitbashCMD':
        os.startfile(r"C:\Users\aa\Desktop\Git Bash.lnk")
        hideMe(write='mongod')
    elif arr[i] =='spotify':
        hideMe(name='spotify')
    elif arr[i]=='chromeUdemy':
        organizeMe('chrome', 'right', 'right', write='browserhome')
    elif arr[i]=='gitbashServer':
        os.startfile(r"C:\Users\aa\Desktop\Git Bash.lnk")
        time.sleep(1)
        organizeMe(press='right',press2='up',press3='right', press4='right',press5='down',write="mongosh")





















