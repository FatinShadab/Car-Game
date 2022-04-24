import random
import pygame
from pygame.locals import *


class SimpleCarGame:
    def __init__(self, winSize, lvlChanger, speedValue, iconPath, playerCarPath, computerCarPath):

        self.active = True

        self.SIZE = self.WIDTH, self.HEIGHT = winSize
        self.ROAD_WIDTH = int(self.WIDTH/1.5)
        self.ROAD_LINE_WIDTH = self.WIDTH/80

        self.lvl = 0
        self.lvlChanger = lvlChanger

        self.itr = 0

        self.left_key_pressed = 0
        self.right_key_pressed = 1 

        self.icon = pygame.image.load(iconPath)

        self.playerCar = pygame.image.load(playerCarPath)
        self.playerCar = pygame.transform.scale(self.playerCar, (120, 250))
        self.playerCar_loc = self.playerCar.get_rect()
        self.playerCar_loc.center = self.WIDTH/2 + self.ROAD_WIDTH/4, self.HEIGHT*.8

        self.computerCar = pygame.image.load(computerCarPath)
        self.computerCar_loc = self.computerCar.get_rect()
        self.computerCar_loc.center = self.WIDTH/2 - self.ROAD_WIDTH/4, self.HEIGHT*.2
        self.computerCar_speed = speedValue

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        pygame.init()

    def __draw_road(self, screenObj):

        pygame.draw.rect(
            screenObj,
            (50, 50, 50),
            (self.WIDTH/2-self.ROAD_WIDTH/2, 0, self.ROAD_WIDTH, self.HEIGHT)
        )

        pygame.draw.rect(
            screenObj,
            (255, 240, 60),
            (self.WIDTH/2 - self.ROAD_LINE_WIDTH/2, 0, self.ROAD_LINE_WIDTH, self.HEIGHT)
        )

        pygame.draw.rect(
            screenObj,
            (255, 255, 255),
            (self.WIDTH/2 - self.ROAD_WIDTH/2 + self.ROAD_LINE_WIDTH*2, 0, self.ROAD_LINE_WIDTH, self.HEIGHT)
        )

        pygame.draw.rect(
            screenObj,
            (255, 255, 255),
            (self.WIDTH/2 + self.ROAD_WIDTH/2 - self.ROAD_LINE_WIDTH*3, 0, self.ROAD_LINE_WIDTH, self.HEIGHT)
        )

    def start(self):

        _temp = self.lvlChanger

        while self.active:

            pygame.display.set_caption(" HIT THE ROAD")
            pygame.display.set_icon(self.icon)

            # Increase speed and change lvl + move the computer-car
            self.computerCar_loc[1] += self.computerCar_speed
            if self.computerCar_loc[1] > self.HEIGHT:
                self.computerCar_loc.center = random.choice([int(self.WIDTH/2 -self.ROAD_WIDTH/4), int(self.WIDTH/2 + self.ROAD_WIDTH/4)]), -200
                self.itr += 1
                if self.itr == self.lvlChanger:
                    self.lvl += 1
                    self.lvlChanger += _temp
                    self.computerCar_speed += .5

            # checks if both car crashed or not
            if self.playerCar_loc.center[0] == self.computerCar_loc.center[0] and self.computerCar_loc.center[1] > (self.playerCar_loc.center[1] -250):
                print("Crashed")
                self.active = False

            # checks for user keyboard inputs and do as programmed
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.active = False

                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        if self.left_key_pressed < 1:
                            self.playerCar_loc = self.playerCar_loc.move([-int(self.ROAD_WIDTH/2), 0])
                            self.left_key_pressed += 1
                            if self.right_key_pressed > 0:
                                self.right_key_pressed -= 1

                    if event.key in [K_s, K_RIGHT]:
                        if self.right_key_pressed < 1:
                            self.playerCar_loc = self.playerCar_loc.move([int(self.ROAD_WIDTH/2), 0])
                            self.right_key_pressed += 1
                            if self.left_key_pressed > 0:
                                self.left_key_pressed -= 1

            # draw and fill screen with green color
            screen = pygame.display.set_mode(self.SIZE)
            screen.fill((60, 220, 0))

            # draw's the road on the screen
            self.__draw_road(screenObj=screen)

            lvlText = self.font.render(f'Level : {self.lvl}', False, (0, 0, 0))
            lvlText_loc = (self.WIDTH*.85, 0)

            pointText = self.font.render(f'Point : {self.itr}', False, (0, 0, 0))
            pointText_loc = (self.WIDTH - self.WIDTH*.98, 0)

            screen.blit(lvlText, lvlText_loc)
            screen.blit(pointText, pointText_loc)
            screen.blit(self.playerCar, self.playerCar_loc)
            screen.blit(self.computerCar, self.computerCar_loc)
            pygame.display.update()

        if not self.active:
            print('inside logic')
            pygame.quit()


if __name__ == "__main__":
    game = SimpleCarGame(
        winSize = (1000, 800),
        iconPath = '../resources\\racing-cars-svgrepo-com.svg',
        lvlChanger = 5,
        speedValue = 1.5,
        playerCarPath = '../resources\\car_topview.svg',
        computerCarPath = '../resources\\otherCar.png'
    )
    game.start()