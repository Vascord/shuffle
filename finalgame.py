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
                    pygame.draw.rect(screen,(0,40,0), (pos_card[0], pos_card[1], 40, 70), 0)
                    pygame.draw.rect(screen,colors[cards[i]][0], (pos_card[0], pos_card[1], 40, 70), 1)
                    if(colors[cards[i]][1] == "square"):
                        pygame.draw.rect(screen,colors[cards[i]][0], (pos_card[0]+10, pos_card[1]+25, 20, 20), 0)
                    elif(colors[cards[i]][1] == "circle"):
                        pygame.draw.circle(screen,colors[cards[i]][0], (pos_card[0]+20, pos_card[1]+35),10,0)
                    elif(colors[cards[i]][1] == "triangle"):
                        pygame.draw.polygon(screen,colors[cards[i]][0], ((pos_card[0]+20, pos_card[1]+25),(pos_card[0]+10, pos_card[1]+40),(pos_card[0]+30, pos_card[1]+40)),0)
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

colors = [((255, 0 , 0),"square"),((255, 0 , 0),"circle"),((255, 0 , 0),"triangle"),((0,255 , 0),"square"),((0,255 , 0),"circle"),((0,255 , 0),"triangle"),((0,0 , 255),"square"),((0,0 , 255),"circle"),((0,0 , 255),"triangle"),((0,0 ,0),"square"),((0,0 , 0),"circle"),((0,0 , 0),"triangle"),((255,255 ,255),"square"),((255,255 ,255),"circle"),((255,255 ,255),"triangle"),((255,0 ,255),"square"),((255,0 ,255),"circle"),((255,0 ,255),"triangle")]

level = 6
score = 0
penality = 0

compare = []
ban_list = []

menu = True
game_start = True
board = False
combo = 0
tries = 0
senpai = 0

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
            combo = 0
            tries = 0
            senpai = 0
            cards = []

            pos_button = [270,240]
            menu_creation()
    

            compare = []
            ban_list = []

        level = mouse_in_box_menu(level)

        if ((600) > mouse_pos[0] > (0) and (220) > mouse_pos[1]> (100) and mouse_click[0]):
            senpai += 1
            if (senpai == 3):
                my_font = pygame.freetype.Font("comic.ttf", 18)
                my_font.render_to(screen,(300,10),("S-Stop clicking on me ... BAKANO !!"),(200,50,0))
                my_font = pygame.freetype.Font("comic.ttf", 15)

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
            my_font.render_to(screen,(500,20),("Score : %s" % score),(200,50,0))
            my_font.render_to(screen,(500,60),("Tries : %s" % tries),(200,50,0))
            my_font.render_to(screen,(500,100),("Combo : %s" % combo),(200,50,0))
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
                combo += 1
                tries += 1
                penality = 0

                screen.fill((0, 40, 0), (500,20,200,300))
                my_font = pygame.freetype.Font("comic.ttf", 24)
                my_font.render_to(screen,(500,20),("Score : %s" % score),(200,50,0))
                my_font.render_to(screen,(500,60),("Tries : %s" % tries),(200,50,0))
                if (combo < 5):
                    my_font.render_to(screen,(500,100),("Combo : %s" % combo),(200,50,0))
                elif (combo >= 5):
                    my_font.render_to(screen,(500,100),("Combo : %s" % combo),(200,50,0))
                    my_font.render_to(screen,(500,140),("COMBO"),(200,50,0))
                    my_font.render_to(screen,(500,180),("BREAKER !!"),(200,50,0))
                my_font = pygame.freetype.Font("comic.ttf", 15)
                if (len(ban_list) >= level*2):
                    my_font = pygame.freetype.Font("comic.ttf", 24)
                    my_font.render_to(screen,(240,216),("Well played !!!"),(200,50,0))
                    my_font = pygame.freetype.Font("comic.ttf", 15)
                pygame.display.flip()

            else:
                pygame.time.wait(500)
                refresh_board()
                compare = []
                penality += 1
                score -= 20*penality
                combo = 0
                tries += 1
                if score < 0:
                    score = 0
                screen.fill((0, 40, 0), (500,20,200,300))
                my_font = pygame.freetype.Font("comic.ttf", 24)
                my_font.render_to(screen,(500,20),("Score : %s" % score),(200,50,0))
                my_font.render_to(screen,(500,60),("Tries : %s" % tries),(200,50,0))
                my_font.render_to(screen,(500,100),("Combo : %s" % combo),(200,50,0))
                my_font = pygame.freetype.Font("comic.ttf", 15)
                pygame.display.flip()
        
        if ((600) > mouse_pos[0] > (500) and (420) > mouse_pos[1]> (400) and mouse_click[0]):
            screen.fill((0,40,0))
            menu = True

        pygame.time.wait(10)