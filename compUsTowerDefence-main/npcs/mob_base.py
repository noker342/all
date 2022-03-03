import pygame


class MobBasic:
    def __init__(self, x, y, route, hp=100, speed=2, damage=1):
        self.x, self.y = x, y
        self.route = route
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect(middle=(x, y))

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def move(self):
        if self.route:
            print(self.route)
            dx, dy = 0, 0
            dist_x = self.rect.x - self.route[0][0]
            dist_y = self.rect.y - self.route[0][1]
            dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
            if dist <= self.speed:
                self.route.pop(0)
            if dist:
                cos = round(dist_x / dist, 2)
                sin = round(dist_y / dist, 2)
                if dist_x != 0 and dist_y != 0:
                    dx, dy = -self.speed * cos, self.speed * sin
                if cos == 1 or cos == -1:
                    dx = -cos * self.speed
                if sin == 1 or sin == -1:
                    dy = -sin * self.speed
            self.rect.x += dx
            self.rect.y += dy