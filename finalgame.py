import pygame
from random import shuffle
import pygame.freetype

 # Creation du tableau (couleurs)
def card_board():
    pos_card = [20,20]
    count = 0
    while count < len(cards):
        if pos_card[0] > 420:
            pos_card[0] = 20
            pos_card[1] += 80
        else:
            pygame.draw.rect(screen,(150,0,150), (pos_card[0], pos_card[1], 40, 70), 0)
            pos_card[0] += 60
            count += 1
    return 0

#refresh le tableau
def refresh_board():
    pos_card = [20,20]
    count = 0
    while count < len(cards):
        if pos_card[0] > 420:
            pos_card[0] = 20
            pos_card[1] += 80
        else:
            if ((pos_card[0], pos_card[1]) not in ban_list):
                pygame.draw.rect(screen,(150,0,150), (pos_card[0], pos_card[1], 40, 70), 0)
            pos_card[0] += 60
            count += 1
    return 0

def mouse_in_box_game(compare):
    pos_card = [20,20]
    for i in range(len(cards)):
        if ((pos_card[0]+40) > mouse_pos[0]> (pos_card[0]) and (pos_card[1]+70) > mouse_pos[1]> (pos_card[1])):
            if ((pos_card[0], pos_card[1]) not in ban_list):
                if (mouse_click[0]):
                    pygame.draw.rect(screen,colors[cards[i]], (pos_card[0], pos_card[1], 40, 70), 0)
                    pygame.display.flip()
                    if ((pos_card[0], pos_card[1]) not in compare) :
                        compare.append(cards[i])
                        compare.append((pos_card[0], pos_card[1]))
                    pygame.time.wait(100)

        pos_card[0] += 60

        if pos_card[0] > 420:
            pos_card[0] = 20
            pos_card[1] += 80

    return compare

def menu_creation():
    menu_numbers = [4,3]
    x = 1
    while x < 7:
                 
        pygame.draw.rect(screen,(0,0,0), (pos_button[0], pos_button[1], 100, 20), 1)
        my_font.render_to(screen, (pos_button[0] + 33,pos_button[1] + 5), ("%s x %s" % (menu_numbers[0], menu_numbers[1])), (200,50,0))
        pos_button[1] += 40
        
        if menu_numbers[0] < menu_numbers[1]:
            menu_numbers[0] += 1
        else:
            menu_numbers[1] += 1
        
        if (menu_numbers[0] * menu_numbers[1]) %2 != 0:
            menu_numbers[0] -= 1
            menu_numbers[1] += 1

        x+= 1
    
    image = pygame.image.load("shuffle.png")
    screen.blit(image,(-100,0))

    pos_button[1] -= 40
    pygame.draw.rect(screen,(0,0,0), (20, pos_button[1], 100, 20), 1)
    my_font.render_to(screen, (53,pos_button[1] + 5), ("Exit"), (150,0,150))

def mouse_in_box_menu(level):
    pos_button[1] = 240
    global clicked
    for i in range(6):
        if ((pos_button[0]+100) > mouse_pos[0] > (pos_button[0]) and (pos_button[1]+20) > mouse_pos[1]> (pos_button[1])):
                if (mouse_click[0]):
                    clicked = True
                    return level

        pos_button[1] += 40

        if level == 18:
            level = 6

        elif level >= 12 :
            level += 3

        else:
            level += 2
    
    return level
                

def level_choice():
    cards = []
    for i in range(level):
        for e in range(2):
            cards.append(i)
    return cards

pygame.init()
screen = pygame.display.set_mode((640,480))
my_font = pygame.freetype.Font("comic.ttf", 15)
screen.fill((0, 40, 0))

colors = [(255, 0 , 0), (0, 255, 0),(0, 0, 255),(0, 0, 0),(255, 255, 255),(0, 255, 255),(255, 255, 0),(255, 0, 255),(155, 155, 255),(255, 155, 155),(155, 255, 155),(140, 80, 200),(80, 140, 200),(140, 80, 200),(180,90,0),(0,90,180),(90,180,0),(90,90,100)]

level = 6
score = 0
penality = 0

compare = []
ban_list = []

menu = True
game_start = True
board = False

pos_button = [270,240]
clicked = False

previous_mouse_press = [ False, False, False ]
mouse_click = [ False, False, False ]

while (True):

    mouse_pos = pygame.mouse.get_pos()
    current_mouse_press = pygame.mouse.get_pressed()

    for i in range(len(mouse_click)):
        if (previous_mouse_press[i] != current_mouse_press[i]):
            mouse_click[i] = current_mouse_press[i]
        else:
            mouse_click[i] = False
        previous_mouse_press[i] = current_mouse_press[i]

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
            
    if (menu):
        if (game_start):
            game_start = False
            board = False
            level = 6
            score = 0
            cards = []

            pos_button = [270,240]
            menu_creation()
    

            compare = []
            ban_list = []

        level = mouse_in_box_menu(level)

        if (clicked):
            clicked = False
            menu = False
            game_start = True
            screen.fill((0,40,0))

        pygame.display.flip()

        if ((120) > mouse_pos[0] > (20) and (460) > mouse_pos[1] > (440) and mouse_click[0]):
            exit()

        pygame.time.wait(10)

    if (game_start):
        if (not board):
            cards = level_choice()
            shuffle(cards)

            card_board()

            my_font = pygame.freetype.Font("comic.ttf", 24)
            p_score = my_font.render_to(screen,(500,20),("Score : %s" % score),(200,50,0))
            my_font = pygame.freetype.Font("comic.ttf", 15)

            pygame.draw.rect(screen,(0,0,0), (520, 400, 60, 20), 1)
            my_font.render_to(screen, (538,405), ("Exit"), (150,0,150))
            board = True
            pygame.display.flip()

        compare = mouse_in_box_game(compare)

        if (len(compare) == 4):
            if (compare[0] == compare[2]):
                pygame.time.wait(500)
                pygame.draw.rect(screen,(0,40,0), (compare[1][0], compare[1][1], 40, 70), 0)
                ban_list.append((compare[1][0], compare[1][1]))
                pygame.draw.rect(screen,(0,40,0), (compare[3][0], compare[3][1], 40, 70), 0)
                ban_list.append((compare[3][0], compare[3][1]))

                compare = []
                score += 100
                penality = 0

                screen.fill((0, 40, 0), (500,20,200,40))
                my_font = pygame.freetype.Font("comic.ttf", 24)
                p_score = my_font.render_to(screen,(500,20),("Score : %s" % score),(200,50,0))
                my_font = pygame.freetype.Font("comic.ttf", 15)
                pygame.display.flip()

            else:
                pygame.time.wait(500)
                refresh_board()
                compare = []
                penality += 1
                score -= 20*penality
                if score < 0:
                    score = 0
                screen.fill((0, 40, 0), (500,20,200,40))
                my_font = pygame.freetype.Font("comic.ttf", 24)
                p_score = my_font.render_to(screen,(500,20),("Score : %s" % score),(200,50,0))
                my_font = pygame.freetype.Font("comic.ttf", 15)
                pygame.display.flip()
        
        if ((600) > mouse_pos[0] > (500) and (420) > mouse_pos[1]> (400) and mouse_click[0]):
            screen.fill((0,40,0))
            menu = True

        pygame.time.wait(10)