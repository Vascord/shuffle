import pygame
from random import shuffle

 # Creation du tableau (couleurs)
def card_board():
    pos_card = [20,20]
    n = 0
    count = 0
    while count < len(cards):
        if n == 4:
            n = 0
            pos_card[0] = 20
            pos_card[1] += 100
        else:
            pygame.draw.rect(screen,(150,0,150), (pos_card[0], pos_card[1], 40, 70), 0)
            pos_card[0] += 80
            count += 1
            n += 1
    return 0

#refresh le tableau
def refresh_board():
    pos_card = [20,20]
    n = 0
    count = 0
    while count < len(cards):
        if n == 4:
            n = 0
            pos_card[0] = 20
            pos_card[1] += 100
        else:
            if ((pos_card[0], pos_card[1]) not in ban_list):
                pygame.draw.rect(screen,(150,0,150), (pos_card[0], pos_card[1], 40, 70), 0)
            pos_card[0] += 80
            count += 1
            n += 1
    return 0

def mouse_pos(pos, s, compare):
    pos_card = [20,20]
    for i in range(len(cards)):
        if ((pos_card[0]+40) > pos[0]> (pos_card[0]) and (pos_card[1]+70) > pos[1]> (pos_card[1])):
            if ((pos_card[0], pos_card[1]) not in ban_list):
                # pygame.draw.rect(screen,(0,0,0), (pos_card[0], pos_card[1], 40, 70), 1)
                if (s[0]):
                    pygame.draw.rect(screen,colors[cards[i]], (pos_card[0], pos_card[1], 40, 70), 0)
                    if ((pos_card[0], pos_card[1]) not in compare) :
                        compare.append(cards[i])
                        compare.append((pos_card[0], pos_card[1]))
                    pygame.time.wait(100)

        pos_card[0] += 80

        if pos_card[0] > 260:
            pos_card[0] = 20
            pos_card[1] += 100

    return compare


pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((0, 40, 0))

colors = [(255, 0 , 0), (0, 255, 0),(0, 0, 255)]

cards = [0,0,1,1,2,2]
shuffle(cards)

card_board()

compare = []
ban_list = []
clock = pygame.time.Clock()

while (True):

    pos = pygame.mouse.get_pos()
    s = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    compare = mouse_pos(pos, s, compare)

    pygame.display.flip()

    if (len(compare) == 4):
        if (compare[0] == compare[2]):
            pygame.draw.rect(screen,(0,40,0), (compare[1][0], compare[1][1], 40, 70), 0)
            ban_list.append((compare[1][0], compare[1][1]))
            pygame.draw.rect(screen,(0,40,0), (compare[3][0], compare[3][1], 40, 70), 0)
            ban_list.append((compare[3][0], compare[3][1]))
            compare = []
        else:
            refresh_board()
            compare = []

    pygame.time.wait(10)