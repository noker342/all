import pygame
from Towers
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
running = True


class Game:
    def __init__(self):
        self.maps = pygame.image.load('/Users/compus/test_files/compUsTowerDefence-main/maps/example/example.png')
        self.maps_rect = self.maps.get_rect(center=(1920//2, 1080//2))
        self.scorersTowerPicture = pygame.image.load('/Users/compus/test_files/compUsTowerDefence-main/Towers/Scorers/tower_1_lvl.png')

    def drawWorld(self):
        screen.blit(self.maps, self.maps_rect)

    def drawTowers(self, x, y):
        self.scorersTowerPicture_rect = self.scorersTowerPicture.get_rect(center=(x, y))
        screen.blit(self.scorersTowerPicture, self.scorersTowerPicture_rect)

    def menuOfTowers(self):
        if input() == 1:
            choice = '/Users/compus/test_files/compUsTowerDefence-main/Towers/Scorers/scorers.py'
        if input() == 2:
            choice = 'laser'
        if input() == 3:
            choice = 'archer'
        if input() == 4:
            choice = 'pvo'


g = Game()
while running:
    g.drawWorld()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            file = open('/Users/compus/test_files/compUsTowerDefence-main/maps/example/example.route')
            checker = file.read()
            if x == checker and y == checker:
                g.drawTowers(x, y)
    pygame.display.flip()