import os
import random
import pygame
# from maps import *

path = '/Users/mac2/Desktop/towdef/maps'


def process_cords(cords):
    for i in range(len(cords)):
        cord = cords[i].replace('(', '').replace(')', '').replace('\n', '').replace(',', '').split()
        cord = int(cord[0]), int(cord[1])
        cords[i] = cord
    return cords


class BattleMap:
    def __init__(self):
        chozen_map = random.choice([file for file in os.listdir(path)])
        self.map_img = pygame.image.load(f"{path}/{chozen_map}/{chozen_map}.png")
        self.map_rect = self.map_img.get_rect(topleft=(0, 0))
        self.waypoints = process_cords(open(f"{path}/{chozen_map}/{chozen_map}.route").readlines())


    def draw(self, screen):
        screen.blit(self.map_img, self.map_rect)
