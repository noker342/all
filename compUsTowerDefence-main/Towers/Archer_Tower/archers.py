import pygame

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
running = True
clock = pygame.time.Clock()


class Archer_Tower:
    def __init__(self, x, y):
        self.width, self.height = 75, 75
        self.center = x, y
        self.x, self.y = x - self.width // 2, y - self.height // 2
        self.radius = 300
        self.tower = pygame.image.load('archertower.png')
        self.tower_rect = self.tower.get_rect(center=(x, y))
        self.calldown = 100
        self.curent_colldown = self.calldown
        self.arrows = []
    
    def draw(self, screen):
        screen.blit(self.tower, self.tower_rect)
        
    def checkRange(self, npc):
        npcInRange = []
        for i in range(len(npc)):
            xo = self.center[0] - npc[i].x
            yo = self.center[1] - npc[i].y
            distance = (xo ** 2 + yo ** 2) ** 0.5
            if distance <= self.radius:
                npcInRange.append((npc[i], distance))
            print(npcInRange)
        return npcInRange
    
    def chooseTarget(self, npc):
        npcInRange = self.checkRange(npc)
        if npcInRange:
            for i in range(len(npcInRange)):
                minimum = i
                for j in range(i + 1, len(npcInRange)):
                    if npcInRange[j][1] < npcInRange[minimum][1]:
                        minimum = j
                    npcInRange[minimum], npcInRange[i] = npcInRange[i], npcInRange[minimum]
            return npcInRange[0][0]

    def calldownBomb(self):
        self.curent_colldown -= 1
        if self.curent_colldown == 0:
            self.curent_colldown = self.calldown
        return self.curent_colldown

    def shoot(self, npc):
        if self.checkRange(npc) and self.calldownBomb() == self.calldown:
            self.arrows.append(Arrow(self.center, self.chooseTarget(npc)))

    def maintainTower(self):
        self.draw(screen)
        self.shoot(npc)
        for arrow in self.arrows:
            arrow.move()
            arrow.draw(screen)
            if arrow.dead:
                for target in npc:
                    target.hp -= arrow.damage
                self.arrows.remove(arrow)
            
        
class Arrow:
    def __init__(self, center, target):
        self.center = center
        self.x, self.y = self.center
        self.arrows = [pygame.image.load('up.png'), pygame.image.load('left.png'), pygame.image.load('right.png'), pygame.image.load('down.png')]
        self.arrows_rect = self.arrows[0].get_rect(center=(self.x, self.y))
        self.damage = 400
        self.speed = 5
        self.arrow = None
        self.target = target

    def move(self):
        dx, dy = 0, 0
        dist_x = self.arrows_rect.x - self.target.x
        dist_y = self.arrows_rect.y - self.target.y
        dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
        if dist:
            cos = round(dist_x / dist, 2)
            sin = round(dist_y / dist, 2)
            if dist_x != 0 and dist_y != 0:
                dx, dy = -self.speed * cos, self.speed * sin
            if cos == 1 or cos == -1:
                dx = -cos * self.speed
            if sin == 1 or sin == -1:
                dy = -sin * self.speed
        self.arrows_rect.x += dx
        self.arrows_rect.y -= dy

    def chooseArrow(self):
        if self.target.x > self.arrows_rect.x:
            self.arrow = self.arrows[2]
        if self.target.x < self.arrows_rect.x:
            self.arrow = self.arrows[1]
        if self.target.y > self.arrows_rect.y:
            self.arrow = self.arrows[3]
        if self.target.y < self.arrows_rect.y:
            self.arrow = self.arrows[0]

        return self.arrow

    def draw(self, screen):
        self.chooseArrow()
        screen.blit(self.arrow, self.arrows_rect)


class Npc:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.hp = 500
        self.dead = False
        self.picture = pygame.image.load('/Users/compus/test_files/compUsTowerDefence-main/Towers/Scorers/boom1.png')
        self.rect = self.picture.get_rect(center=(self.x, self.y))

    def draw(self):
        screen.blit(self.picture, self.rect)

    def death(self):
        if self.hp <= 0:
            self.dead = True


a = Archer_Tower(1920 // 2, 1080 // 2)
npc = []
for i in range(100):
    npc.append(Npc(width, height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((255, 255, 255))
    for i in npc:
        i.draw()
        i.death()
        if i.dead:
            npc.remove(i)
    a.maintainTower()
    pygame.display.flip()
    clock.tick(60)