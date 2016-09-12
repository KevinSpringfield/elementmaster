'''卡片對戰遊戲 ver2.0 完成浮動選牌,自動補牌'''

import pygame, sys
import os
from pygame.locals import *
from PIL import Image
from models import Cards
import random


title = "Element Master ver2.0" #遊戲名稱
property = ["Fire", "Water", "Wood"]


pygame.init()
#參數設定
screen = pygame.display.set_mode((1024, 700), 0, 32)
background = pygame.image.load('image/back4.jpg')
background = background.convert()
card_y = 600 #卡片的Y座標
dy = 40  #移動卡片的Y位移量
card_x = 100
dx = 120 # 兩張卡片的X距離

#設定FPS
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 120
deltat = clock.tick(FRAMES_PER_SECOND)
 
 #讀取圖片
fire = pygame.image.load(os.path.join( 'image/fire.bmp'))
water = pygame.image.load(os.path.join( 'image/water.bmp'))
wood = pygame.image.load(os.path.join( 'image/wood.bmp'))
light = pygame.image.load(os.path.join( 'image/light2_Fotor.jpg'))
monster = pygame.image.load(os.path.join( 'image/monster2.jpg'))
pygame.display.set_caption(title)



font = pygame.font.Font(None, 20)
text = font.render('Move your mouse !', True, (34, 252, 43))
global pointAt
pointAt = " "


def draw_card(cd):
    x = card_x
    global cardlist
    cardlist = []

    for item in cd:
        x = x+dx
        if item == "Fire":
            cardlist.append(screen.blit(fire,(x, card_y)))
        elif item  == "Water":
            cardlist.append(screen.blit(water,(x, card_y)))
        elif item == "Wood":
            cardlist.append(screen.blit(wood,(x, card_y)))
    return cardlist

def draw_card_up(cd, num):
    x = card_x
    global cardlist
    cardlist = []
    for item in cd:
        x = x+dx
        if item == "Fire" and item ==cd[num]:
            cardlist.append(screen.blit(light,(x-12, card_y -dy -12)))
            cardlist.append(screen.blit(fire,(x, card_y - dy)))
        elif item == "Fire":
            cardlist.append(screen.blit(fire,(x, card_y)))
        elif item  == "Water" and item ==cd[num]:
            cardlist.append(screen.blit(light,(x-12, card_y -dy -12)))
            cardlist.append(screen.blit(water,(x, card_y - dy)))
        elif item  == "Water":
            cardlist.append(screen.blit(water,(x, card_y)))
        elif item == "Wood" and item ==cd[num]:
            cardlist.append(screen.blit(light,(x-12, card_y -dy -12)))
            cardlist.append(screen.blit(wood,(x, card_y - dy)))
        elif item == "Wood":
            cardlist.append(screen.blit(wood,(x, card_y)))
    return cardlist

#作一個函式來顯示相同的卡片位置cd為手牌,num為地幾張
def get_card_index(cd, num):
    card_index =[]
    i = 0
    for item in cd :
        if item == cd[num]:
            card_index.append(i)            
        i = i+1
    return card_index

#作一個函式來判斷指到第幾張卡片
def touch_card(pos):
    global pointAt
    if pygame.Rect(280, 600, 96, 96).collidepoint(pos):
        pointAt = "card1"
    elif pygame.Rect(380, 600, 96, 96).collidepoint(pos):
        pointAt = "card2"

    elif pygame.Rect(480, 600, 96, 96).collidepoint(pos):
        pointAt = "card3"

    elif pygame.Rect(580, 600, 96, 96).collidepoint(pos):
        pointAt = "card4"

    elif pygame.Rect(680, 600, 96, 96).collidepoint(pos):
        pointAt = "card5"

    else:
        pointAt = " "

    return pointAt

#製作函式來出牌
def battle(cd, num):
    x = 0
    choose = cd[num]
    new_cd = []
    for item in cd:
        if item == choose:
            #new_cd.append(item)
            print("remove" + item)
            cd.remove(item)
            x += 1       
    for i in range(1,x+1):
        cd.append((random.choice(property)))

    return (cd, x)


#繪製怪物
def draw_monster(mon_name, mon_hp, mon_property):
    font = pygame.font.Font(None, 50)
    name = font.render(mon_name, True, ( 255, 255, 255))
    hp = font.render(mon_hp, True, ( 255, 0, 0))
    mon_property = font.render(mon_property, True, ( 72, 58, 54))

    screen.blit(monster, (362,50)) #繪出怪物
    screen.blit(name, (362,377)) #繪出怪物資料
    screen.blit(hp, (550,377)) #繪出怪物血量
    screen.blit(mon_property, (700,250))



class monster():
    def __init__(self, name, level):
        self.name = name
        self.hp = level**2 *2 + 20
        self.level = level
        self.atk = level*2
        self.property = random.choice(property)


    def draw(self):
        font = pygame.font.Font(None, 50)
        name = font.render(self.name, True, ( 255, 255, 255))
        hp = font.render(str(self.hp), True, ( 255, 0, 0))
        mon_property = font.render(self.property, True, ( 255, 255, 255))
        monster = pygame.image.load(os.path.join( 'image/monster2.jpg'))
        screen.blit(monster, (362,50)) #繪出怪物
        screen.blit(name, (362,377)) #繪出怪物資料
        screen.blit(hp, (550,377)) #繪出怪物血量
        screen.blit(mon_property, (700,250))

class player():
    def __init__(self, level):
        self.hp = level**2 *3 + 40
        self.level = level
        self.atk = level *2
    def draw(self):
        font = pygame.font.Font(None, 50)
        lv = font.render(str(self.level), True, ( 255, 0, 0))
        hp = font.render(str(self.hp), True, ( 255, 0, 0))
        screen.blit(font.render("Lv :", True, ( 255, 255, 255)), (20,500)) 
        screen.blit(font.render("Hp :", True, ( 255, 255, 255)), (20,550))
        screen.blit(lv, (100,500)) 
        screen.blit(hp, (100,550)) 





card = Cards()
cd_in_hand = card.deal()
print("your cards are" + str(cd_in_hand))
screen.blit(background, (0,0))


monsterAppear = monster("GiBaNyan", 1)
braver = player(1) 

while True: # main game loop

    screen.blit(background, (0,0))
    #draw_monster("GiBaNyan", str(100), "Fire")

    monsterAppear.draw()   
    braver.draw()
    
    if pointAt == "card1":
        draw_card_up(cd_in_hand, 0)
    elif pointAt == "card2":
        draw_card_up(cd_in_hand, 1)
    elif pointAt == "card3":
        draw_card_up(cd_in_hand, 2)
    elif pointAt == "card4":
        draw_card_up(cd_in_hand, 3)
    elif pointAt == "card5":
        draw_card_up(cd_in_hand, 4)
    else: 
        draw_card(cd_in_hand)

    for event in pygame.event.get():
        #draw_card(cd_in_hand)


        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION:
            #return the X and Y position of the mouse cursor
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            #print("x y is " + str(mouse_x) +" "+ str(mouse_y))
 
            touch_card(pos)

            pygame.display.update(cardlist)
            continue
     
        if event.type ==  MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
 
        
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    #點選指到的卡片會做出的callback

                    if index == 0 and pointAt == "card1":
                        print('Pressed CARD1')
                        print(battle(cd_in_hand, 0))
                    elif index == 0 and pointAt == "card2":
                        print('Pressed CARD2')
                        print(battle(cd_in_hand, 1))
                    elif index == 0 and pointAt == "card3":
                        print('Pressed CARD3')
                        print(battle(cd_in_hand, 2))
                    elif index == 0 and pointAt == "card4":
                        print('Pressed CARD4')
                        print(battle(cd_in_hand, 3))
                    elif index == 0 and pointAt == "card5":
                        print('Pressed CARD5')
                        print(battle(cd_in_hand, 4))


    
    pygame.display.update(cardlist)
    #card_num = input("輸入1~5 選擇卡牌 : ")


