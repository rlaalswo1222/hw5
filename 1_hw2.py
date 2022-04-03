import turtle

import random

import math

from tkinter.simpledialog import * 

##2021041070 김민재

inStr = ''

swidth, sheight = 500, 500

tX, tY, txtSize,save,angle,rad,a = [0] * 7

 

 

turtle.title('거북 글자쓰기')

turtle.shape('turtle')

turtle.setup(width = swidth + 50, height = sheight + 50)

turtle.screensize(swidth, sheight)	 

turtle.penup()

 

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

a = (len(inStr)//32) + 1 ## 회전할 바퀴 수

save = (360*a/len(inStr)) 

rad = 200

for ch in inStr :

     if (rad<0) :

          rad = 0

 

     tX = rad*math.cos(3.14 * angle/180)

     tY = rad*math.sin(3.14 * angle/180)

     angle += save

     rad -= 3

     

     r = random.random(); g = random.random(); b = random.random()

     txtSize = 20

     turtle.goto(tX, tY)

	 

     turtle.pencolor((r, g, b))

     turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

     

 

turtle.done()
