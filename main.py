from asyncio import sleep
from itertools import count
import pyautogui as pag
import time


size_matrix_w, size_matrix_h = map(int, input("Введите размер марицы>> ").split())

pag.click(72, 110)  # нажатие по 1 чату в списке
pag.click(503, 1384) # нажатие по текстовой строке
time.sleep(3) # задаржка в 3 секнды


file = open(r"matrix_txt\ASCII-смайлик.txt", 'r')
data = file.read()
y = 1
x = 0
for i in data:
     if i == "0":
          x += 1
          pag.typewrite("/set " + str(x)  + " " + str(y))
          pag.hotkey('enter')  # нажатие на enter
          time.sleep(0)  # задержка в пол секунды
               
     else:
          x += 1
          pag.typewrite("/clr " + str(x) + " " + str(y))
          pag.hotkey('enter')  # нажатие на enter
          time.sleep(0)  # задержка в пол секунды
     if x == size_matrix_w:
          y += 1
          x = 0
 