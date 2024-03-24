import webbrowser as wb
import pyautogui as pag
import pyperclip
from keyboard import press_and_release
from time import sleep

def paste(text: str):    
    pyperclip.copy(text)
    #press_and_release('ctrl + v')

def spamer():
    pag.typewrite(pyperclip.paste())
    pag.press("enter")
    sleep(1)

#wb.open('https://www.youtube.com/watch?v=BfJFvrxhTDw')
#time.sleep(10)
while True:
    paste('ТЕСТ')
    spamer()