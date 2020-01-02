import pygame
from random import randint

 
def card_board(cards):
    pos_card = [20,20]
    n = 0
    count = 0
    verify = [0,0,0]
    global refresh
    global colors
    global screen
    while count < cards:
        if n == 4:
            n = 0
            pos_card[0] = 20
            pos_card[1] += 100
        rn = randint(0,2)
        if verify[rn] != 2:
            verify[rn] += 1
            pygame.draw.rect(screen,colors[rn], (pos_card[0], pos_card[1], 40, 70), 0)
            refresh.append(colors[rn])
            pos_card[0] += 80
            count += 1
            n += 1
    return 0

def refresh_board(cards):
    pos_card = [20,20]
    n = 0
    count = 0
    global refresh
    global colors
    global screen
    while count < cards:
        if n == 4:
            n = 0
            pos_card[0] = 20
            pos_card[1] += 100
        if n < 4:
            pygame.draw.rect(screen,(150,0,150), (pos_card[0], pos_card[1], 40, 70), 0)
            pos_card[0] += 80
            count += 1
            n += 1
    return 0

pygame.init()
screen = pygame.display.set_mode((640,480))
colors = [(255, 0 , 0), (0, 255, 0),(0, 0, 255)]
momento = 0
cards = 6
compare = []
pos_card = [20,20]
screen.fill((0, 40, 0))
refresh = []
card_board(cards)
n = 0
clock = pygame.time.Clock()

while (True):

    pos = pygame.mouse.get_pos()
    s = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
        elif (event.type == s[0]):
            mouse_clicked = True

    if momento < 1:
        refresh_board(cards)
    
    if ((60) > pos[0]> (20) and (90) > pos[1]> (20)):
        pygame.draw.rect(screen,(0,0,0), (20, 20, 40, 70), 1)
        if (s[0]):
            pygame.draw.rect(screen,refresh[0], (20, 20, 40, 70), 0)
            if momento== 1:
                if compare[0] == 0:
                    compare.append(0)
                    momento = 2
            else :
                compare.append(0)
                momento = 1
                pygame.time.wait(100)

    if ((140) > pos[0]> (100) and (90) > pos[1]> (20)):
        pygame.draw.rect(screen,(0,0,0), (100, 20, 40, 70), 1)
        if (s[0]):
            pygame.draw.rect(screen,refresh[1], (100, 20, 40, 70), 0)
            if momento == 1:
                if compare[0] == 1:
                    compare.append(1)
                    momento = 2
            else :
                compare.append(1)
                momento = 1
                pygame.time.wait(100)

    if ((220) > pos[0]> (180) and (90) > pos[1]> (20)):
        pygame.draw.rect(screen,(0,0,0), (180, 20, 40, 70), 1)
        if (s[0]):
            pygame.draw.rect(screen,refresh[2], (180, 20, 40, 70), 0)
            if momento == 1:
                if compare[0] == 2:
                    compare.append(2)
                    momento = 2
            else :
                compare.append(2)
                momento = 1
                pygame.time.wait(100)

    if ((300) > pos[0]> (260) and (90) > pos[1]> (20)):
        pygame.draw.rect(screen,(0,0,0), (260, 20, 40, 70), 1)
        if (s[0]):
            pygame.draw.rect(screen,refresh[3], (260, 20, 40, 70), 0)
            if momento == 1:
                if compare[0] == 3:
                    compare.append(3)
                    momento = 2
            else :
                compare.append(3)
                momento = 1
                pygame.time.wait(100)

    if ((60) > pos[0]> (20) and (190) > pos[1]> (120)):
        pygame.draw.rect(screen,(0,0,0), (20, 120, 40, 70), 1)
        if (s[0]):
            pygame.draw.rect(screen,refresh[4], (20, 120, 40, 70), 0)
            if momento == 1:
                if compare[0] == 4:
                    compare.append(4)
                    momento = 2
            else :
                compare.append(4)
                momento = 1
                pygame.time.wait(100)

    if ((140) > pos[0]> (100) and (190) > pos[1]> (120)):
        pygame.draw.rect(screen,(0,0,0), (100, 120, 40, 70), 1)
        if (s[0]):
            pygame.draw.rect(screen,refresh[5], (100, 120, 40, 70), 0)
            if momento == 1:
                if compare[0] == 5:
                    compare.append(5)
                    momento = 2
            else :
                compare.append(5)
                momento = 1
                pygame.time.wait(1000)
        
    if momento == 2:
        if len(compare) == 2:
            if refresh[compare[0]] == refresh[compare[1]] :
                pygame.draw.rect(screen,(0,40,0), (20, 20, 40, 70), 0)
                print (refresh[compare[0]], refresh[compare[1]])
                compare = []
    

    pygame.display.flip()