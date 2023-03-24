from pygame import *

window = display.set_mode((1000, 500))
background = transform.scale(image.load("fon.jpg"), (1000, 500))

#игровой цикл
game = True
clock = time.Clock()
FPS = 60
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -=  self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y +=  self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -=  self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y +=  self.speed
    
    
player1 = Player1('platform.png', 10, 100, 10, 30, 110)
player2 = Player2('platform.png', 960, 100, 10, 30, 110)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()

    

    display.update()
    clock.tick(FPS)

























































# import pygame
# pygame.init()
# mw = pygame.display.set_mode((500, 500))
# mw.fill ((255, 255, 255))
# clock = pygame.time.Clock()
# class Area():
#     def __init__(self, image, x = 55, y = 55, width = 10, height = 10):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.image = pygame.image.load(image)
#     def draw(self, shift_x = 0, shift_y = 0):
#         mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
# class Enemy(Area):
#     def __init__(self, x, y):
#         Area.__init__(self, 'enemy.png', x, y, 30, 30)
# class Platform(Area):
#     def __init__(self, x, y):
#         Area.__init__(self, 'platform.png', x, y, 95, 40)
#     def move_left(self):
#         self.rect.x -= 10
       
#     def move_right(self):
#         self.rect.x += 10
# class Ball(Area):
#     def __init__(self, x, y):
#         Area.__init__(self, 'platform.png', x, y)
#         self.speed_x = 4
#         self.speed_y = -4
        
#     def move(self):
#         self.rect.x += self.speed_x
#         self.rect.y += self.speed_y
#         self.collide()
#     def collide(self):
#         if self.rect.right >= 500:
#             self.rect.right = 500
#             self.speed_x *= -1
#         elif self.rect.x <= 0:
#             self.rect.x = 0
#             self.speed_x *= -1
#         if self.rect.bottom <= 0:
#             self.rect_y = 0
#             self.speed_y *= -1
#         if self.rect.colliderect(platform.rect):
#             self.speed_y *= -1
#         for enemy in enemy_list:
#             if self.rect.colliderect(enemy.rect):
#                 enemy_list.remove(enemy)
#                 self.speed_y *= -1
        
# enemy_list = [0] * 24
# x = 10
# y = 0
# for i in range(len(enemy_list)):
#     if i == 9:
#         y += 55
#         x = 35
#     if i == 17:
#         y += 55
#         x = 60
#     enemy_list[i] = Enemy(x, y)
#     x += 55
# platform = Platform(200, 290)
# ball = Ball(100, 250)
# font = pygame.font.Font(None, 128)
# lose = font.render('Loser!', True, (255, 0, 0))
# win = font.render('Winner!', True, (0, 255, 0))
# while True:
#     clock.tick(10)
#     mw.fill((255, 255, 255))
#     if pygame.key.get_pressed()[pygame.K_a]:
#         platform.move_left()
#     elif pygame.key.get_pressed()[pygame.K_d]:
#         platform.move_right()
#     platform.draw()
#     ball.draw()
#     if len(enemy_list) == 0:
#         mw.blit(win, (160, 170))
#         isRunning = False
#     elif ball.rect.bottom > 300:
#         mw.blit(lose, (160, 170))
#         isRunning = False
#     for i in range(len(enemy_list)):
#         enemy_list[i].draw()
#     ball.move()
#     pygame.display.update()