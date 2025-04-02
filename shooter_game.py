from pygame import *

x = 1
y = 1
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (150, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #_движение игрока_
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and y >= 0:
            self.rect.y -= 5
        if keys[K_s] and y <5:
            self.rect.y += 5
        if keys[K_a] and x >= 0:
            self.rect.x -= 5
        if keys[K_d] and x <5:
            self.rect.x += 5
Player.lost = 0
#_движение врага_
    #_отображение окна, врага и игрока_
window = display.set_mode((700, 500))
display.set_caption('Игра "защити огород Спраута')
background = transform.scale(image.load('original.jpg'), (700, 500))
hero = Player('plant.png', x, y, 180)
#_фоновая музыка_
mixer.init()
mixer.music.load('les.mp3')
mixer.music.play()
game = True
while game:
    window.blit(background,(0, 0))
    hero.update()
    hero.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()