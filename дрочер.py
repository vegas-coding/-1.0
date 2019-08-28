from colorama import init
init()
from colorama import Fore, Back, Style
import time
import pyautogui
import progressbar
print(Fore.GREEN)
bar = progressbar.ProgressBar().start()

for t in range(0,101):
    bar.update(t)
    time.sleep(0.01)
bar.finish()

print(Fore.GREEN)
secs = int(input("Сколько надо мне работать ?:\n "))
secs = secs * 7


clicks = 1

print(Fore.GREEN)
print("Я начну работать через 5 секунд ! ")

print(Fore.GREEN)
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)
time.sleep(1)
print(4)
time.sleep(1)
print(5)
time.sleep(1)

print(Fore.GREEN)
print("Я работаю ! ")

for clicks in range(0, secs):
    pyautogui.tripleClick()
else:
    print("Я поработал ! ")
input()