import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    screen.fill((0, 40, 0))

    color = (255,255,255)
    posy = [0,0]
    for i in range(4):
        pygame.draw.rect(screen,color, (posy[0], posy[1], 40, 40), 0)
        posy[0] += 100
    pos = pygame.mouse.get_pos()
    s = pygame.mouse.get_pressed()

    if (40 > pos[0]> 0 and 40 > pos[1]> 0):
        pygame.draw.rect(screen,(0,0,0), (0, 0, 40, 40), 0)
        if (s[0]):
            pygame.draw.rect(screen,(0,0,255), (0, 0, 40, 40), 0)
    
    pygame.display.flip()
    