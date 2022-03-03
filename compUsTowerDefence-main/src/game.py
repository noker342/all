import pygame
import sys
import os
# from npcs.fast.fast import FastNpc
from Towers.Scorers import *
# from battleMap import BattleMap
from Towers.Scorers.scorers import Scorers_Tower
from src.battleMap import BattleMap
from src.waveEngine import WaveEngine



class Battlefield:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.battleMap = BattleMap()
        self.towerTypes = [Scorers_Tower, 'Archer', 'PVO', 'Laser']
        self.towerTypes[0]()
        waveEngine = WaveEngine()
        self.npcTypes = ['FastNpc', 'DefaultNpc', 'Minotaur']
        self.towers = []
        self.npc =          [FastNpc(300, 1080, 3, self.battleMap.waypoints)]
        self.projectiles =  []
        self.hp = 20
        self.gold = 0
        self.hpFlow = 0  # amount of npcHp spawned per second. measures difficulty
        self.clock = pygame.time.Clock()

    # def getNpcList(self):
    #     return os.listdir('../npcs/')[1:]

    def buildable(self, x, y):
        return True

    def utilizeCorpses(self):
        i = 0
        while i < len(self.npc):
            if self.npc[i].hp <= 0:
                self.gold += self.npc[i].bounty
                self.npc.pop(i)
            else:
                i += 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.battleMap.draw(self.screen)
        for npc in self.npc:
            npc.draw(self.screen)
        for tower in self.towers:
            tower.draw(self.screen)
        pygame.display.flip()

    def buildTower(self, tower, x, y):
        if self.buildable(x, y):
            self.towers.append(tower(x, y))
            self.gold -= tower.price

    def mainLoop(self):
        while self.hp > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.draw()
            self.update()
            self.clock.tick(60)

    def update(self):
        for npc in self.npc:
            npc.move()
        self.utilizeCorpses()


tmp = Battlefield()



