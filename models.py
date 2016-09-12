"""模組"""
import pygame, sys
import os
from pygame.locals import *
from PIL import Image
from models import *
import random
import random
property = ["Fire", "Water", "Wood"]

screen = pygame.display.set_mode((1024, 700), 0, 32)


class Cards():
    def __init__(self):
        pass

    def deal(self): #亂數產生五張手牌
        cd_in_hand = []
        for i in range(1, 6):
            cd_in_hand.append(random.choice(property))
        
        return(cd_in_hand)

    def print_cd(self):

        print(cd_in_hand)

    #def cd_reload(self):


    def choose(self, num):
        return(cd_in_hand.pop(int(num) - 1))


def draw_card_up(cd, num, posx, posy, dis_x, dis_y):
    #cd is cardInHand list, num is pointAtNum
    x = posx
    dx = dis_x
    dy = dis_y
    cardlist = []
    for item in cd:
        x = x+dx
        if item == "Fire" and item ==cd[num]:
            cardlist.append(screen.blit(light,(x-12, card_y -dy -12)))
            cardlist.append(screen.blit(fire,(x, card_y - dy)))
        elif item == "Fire":
            cardlist.append(screen.blit(fire,(x, card_y)))
        elif item  == "Water" and item ==cd[num]:
            #cardlist.append(screen.blit(light,(x-12, card_y -dy -12)))
            cardlist.append(screen.blit(water,(x, card_y - dy)))
        elif item  == "Water":
            cardlist.append(screen.blit(water,(x, card_y)))
        elif item == "Wood" and item ==cd[num]:
            #cardlist.append(screen.blit(light,(x-12, card_y -dy -12)))
            cardlist.append(screen.blit(wood,(x, card_y - dy)))
        elif item == "Wood":
            cardlist.append(screen.blit(wood,(x, card_y)))
    return cardlist

def draw_card(cd, posx, posy, dis_x, dis_y):
    x = posx
    dx = dis_x
    dy = dis_y
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

    return(pointAt)

    

        
