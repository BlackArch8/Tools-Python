import pyautogui, time

time.sleep(5)
f = open ("C:\\Users\donia\Desktop\output.txt", 'r')
for word in f:
    pyautogui.typewrite("618026" + word)
    #pyautogui.press("enter")
    
    