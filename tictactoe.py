#MIT License

#Copyright (c) 2020 Viswanadh Kothakota

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import pygame as pg,sys
from pygame.locals import *
import time
import random
from RespondListen import respond, listen

XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
line_color = (10,10,10)
TTT = [[None]*3, [None]*3, [None]*3]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
#global screen
#screen = pg.display.set_mode((width,height+100),0,32)
#pg.display.set_caption("Tic Tac Toe")

opening = pg.image.load('Images\TTT\cover_page.png')
x_img = pg.image.load('Images\TTT\X.png')
o_img = pg.image.load('Images\TTT\O.png')

x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width,height+100))

def game_opening():
    screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
    pg.draw.line(screen, line_color, (0,height/3), (width,height/3), 7)
    pg.draw.line(screen, line_color, (0,height/3*2), (width,height/3*2), 7)
    #draw_status()

def draw_status():
    global draw

    if winner is None:
        #message = XO.upper() + "'s Turn"
        if XO == "x":
            message = " It's your turn sir"
        else:
            time.sleep(1)
            message = " It's my turn sir"
    else:
        #message = winner.upper() + " won!"
        if winner == "x":
            message = "Your Won Sir!"
        else:
            message = "I won Sir!"
    if draw:
        message = 'Game Draw!'
    
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(1)
    respond(message)
    #time.sleep(1)

def check_win():
    global TTT, winner, draw

    for row in range(0,3):
        if ((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)):
            winner = TTT[row][0]
            pg.draw.line(screen, (255,0,0), (0, (row+1)*height/3 -height/6), \
                        (width, (row+1)*height/3 - height/6), 4)
            break
    for col in range(0,3):
        if ((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            pg.draw.line(screen, (255,0,0), ((col+1)*width/3 - width/6, 0), \
                         ((col+1)*width/3 - width/6, height), 4)
            break
    if ((TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None)):
        winner = TTT[0][0]
        pg.draw.line(screen, (255,0,0), (50,50), (350,350), 4)
    if ((TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None)):
        winner = TTT[0][2]
        pg.draw.line(screen, (255,0,0), (350,50), (50,350), 4)
    if (all([all(row) for row in TTT]) and winner is None):
        draw = True
    draw_status()

def drawXO (row,col):
    global TTT,XO
    if row == 0:
        posx = 30
    if row == 1:
        posx = width/3 + 30
    if row == 2:
        posx = width/3*2 + 30
    if col == 0:
        posy = 30
    if col == 1:
        posy = height/3 + 30
    if col == 2:
        posy = height/3*2 + 30
    
    TTT[row][col] = XO
    
    if (XO=='x'):
        screen.blit(x_img, (posy,posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy,posx))
        XO = 'x'
    pg.display.update()

def userClick():
    x,y = pg.mouse.get_pos()
    if (x<width/3):
        col = 0
    elif(x<width/3*2):
        col = 1
    elif(x<width):
        col = 2
    else:
        col = None

    if (y<height/3):
        row = 0
    elif(y<height/3*2):
        row = 1
    elif(y<height):
        row = 2
    else:
        row = None
    
    if (TTT[row][col] is None):
        global XO
        drawXO(row,col)
        check_win()

def sys_click():
    c,d = sys_move()
    drawXO(c,d)
    check_win()      

def sys_move():
    global TTT, XO
    a=[0,1,2]
    arr = ['o','x']
    for k in arr:
        #row-o
        for row in range(0,3):
            if (TTT[row][0] == TTT[row][1] == k) and (TTT[row][2] is None):
                return row,2
            elif (TTT[row][0] == TTT[row][2] == k) and (TTT[row][1] is None):
                return row,1
            elif (TTT[row][1] == TTT[row][2] == k) and (TTT[row][0] is None):
                return row,0
        #col-o
        for col in range(0,3):
            if(TTT[0][col] == TTT[1][col] == k) and (TTT[2][col] is None):
                return 2,col
            elif(TTT[0][col] == TTT[2][col] == k) and (TTT[1][col] is None):
                return 1,col
            elif(TTT[1][col] == TTT[2][col] == k) and (TTT[0][col] is None):
                return 0,col
        #diag-1-o
        if (TTT[0][0] == TTT[1][1] == k) and (TTT[2][2] is None):
            return 2,2
        elif(TTT[0][0] == TTT[2][2] == k) and (TTT[1][1] is None):
            return 1,1
        elif(TTT[1][1] == TTT[2][2] == k) and (TTT[0][0] is None):
            return 0,0
        #diag-2-o
        if (TTT[0][2] == TTT[1][1] == k) and (TTT[2][0] is None):
            return 2,0
        elif(TTT[0][2] == TTT[2][0] == k) and (TTT[1][1] is None):
            return 1,1
        elif(TTT[1][1] == TTT[2][0] == k) and (TTT[0][2] is None):
            return 0,2
        
    search = True
    while search:
        row = random.choice(a)
        col = random.choice(a)
        if TTT[row][col] is None:
            return row,col
            search =  False

def reset_game():
    global TTT,winner,XO,draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None]*3, [None]*3, [None]*3]


def tic_tac_toe():
    global screen
    screen = pg.display.set_mode((width,height+100),0,32)
    pg.display.set_caption("Tic Tac Toe")
    game_opening()
    draw_status()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                userClick()
                if(winner or draw):
                    reset_game()
                    draw_status()
                else:
                    time.sleep(2)
                    sys_click()
                    if(winner or draw):
                        reset_game()
                        draw_status()

        pg.display.update()
        CLOCK.tick(fps)
