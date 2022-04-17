import random
import pygame as game
from pygame.locals import *


SIZE = WIDTH, HEIGHT = (1000, 800)
ROAD_WIDTH = int(WIDTH/1.5)
ROAD_LINE_WIDTH = WIDTH/80

lvl = 0
itr = 0
lvlChanger = 5
left_key_pressed = 0
right_key_pressed = 0 

game.font.init()
font = game.font.SysFont('Comic Sans MS', 30)

gameIcon = game.image.load('resources\\racing-cars-svgrepo-com.svg')
playerCar = game.image.load('resources\\car_topview.svg')
playerCar = game.transform.scale(playerCar, (120, 250))
playerCar_loc = playerCar.get_rect()
playerCar_loc.center = WIDTH/2 + ROAD_WIDTH/4, HEIGHT*.8

computerCar = game.image.load('resources\\otherCar.png')
computerCar_loc = playerCar.get_rect()
computerCar_loc.center = WIDTH/2 - ROAD_WIDTH/4, HEIGHT*.2
computerCar_speed = 1.5


game.init()
active = True


while active:

    game.display.set_caption(" HIT THE ROAD")
    game.display.set_icon(gameIcon)

    computerCar_loc[1] += computerCar_speed
    if computerCar_loc[1] > HEIGHT:
        computerCar_loc[1] = -200
        computerCar_loc[0] = random.choice([int(WIDTH/3 - ROAD_WIDTH/4), int(WIDTH/3 + ROAD_WIDTH/4)])
        itr += 1
        if itr == lvlChanger:
            lvl += 1
            lvlChanger += 5
            computerCar_speed += .25

    if playerCar_loc[0] == computerCar_loc[0] and computerCar_loc[1] > (playerCar_loc[1] -250):
        break

    for event in game.event.get():
        if event.type == QUIT:
            active = False

        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                if left_key_pressed < 1:
                    playerCar_loc = playerCar_loc.move([-int(ROAD_WIDTH/2), 0])
                    left_key_pressed += 1
                    if right_key_pressed > 0:
                        right_key_pressed -= 1

            if event.key in [K_s, K_RIGHT]:
                if right_key_pressed < 1:
                    playerCar_loc = playerCar_loc.move([int(ROAD_WIDTH/2), 0])
                    right_key_pressed += 1
                    if left_key_pressed > 0:
                        left_key_pressed -= 1

    screen = game.display.set_mode(SIZE)
    screen.fill((60, 220, 0))
    game.draw.rect(
        screen,
        (50, 50, 50),
        (WIDTH/2-ROAD_WIDTH/2, 0, ROAD_WIDTH, HEIGHT)
    )
    game.draw.rect(
        screen,
        (255, 240, 60),
        (WIDTH/2 - ROAD_LINE_WIDTH/2, 0, ROAD_LINE_WIDTH, HEIGHT)
    )
    game.draw.rect(
        screen,
        (255, 255, 255),
        (WIDTH/2 - ROAD_WIDTH/2 + ROAD_LINE_WIDTH*2, 0, ROAD_LINE_WIDTH, HEIGHT)
    )

    game.draw.rect(
        screen,
        (255, 255, 255),
        (WIDTH/2 + ROAD_WIDTH/2 - ROAD_LINE_WIDTH*3, 0, ROAD_LINE_WIDTH, HEIGHT)
    )

    lvlText = font.render(f'Level : {lvl}', False, (0, 0, 0))
    lvlText_loc = (WIDTH*.85, 0)

    pointText = font.render(f'Point : {itr}', False, (0, 0, 0))
    pointText_loc = (WIDTH-WIDTH*.98, 0)

    screen.blit(lvlText, lvlText_loc)
    screen.blit(pointText, pointText_loc)
    screen.blit(playerCar, playerCar_loc)
    screen.blit(computerCar, computerCar_loc)
    game.display.update()

game.quit()