import random
import math
import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("background.png")
pygame.display.set_caption("Space-Vader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
playerimage = pygame.image.load("spaceship.png")
enemyimage = pygame.image.load("monster.png")
bulletimage = pygame.image.load("bullet.png")
game_status = "ready"

bullet_num = 5
enemy_num = 5
atomic_bomb_num = 2
game_score = 0
font1 = "freesansbold.ttf"
mixer.music.load("background.wav")
mixer.music.play(-1)
explosionSound = mixer.Sound("explosion.wav")
bulletSound = mixer.Sound("laser.wav")


class Player:
    def __init__(self, image, X, Y, state):
        self.image = image
        self.X = X
        self.Y = Y
        self.state = state

    def Move_Right(self):
        self.X += 5
        screen.blit(self.image, (self.X, self.Y))

    def Move_Left(self):
        self.X -= 5
        screen.blit(self.image, (self.X, self.Y))

    def Stop_Moving(self):
        screen.blit(self.image, (self.X, self.Y))


player1 = Player(playerimage, 370, 480, "stop")


class Enemy(Player):
    def __init__(self, image, X, Y, state):
        Player.__init__(self, image, X, Y, state)

    def Move_Left(self):
        self.X += 3
        Player.Move_Left(self)

    def Move_Right(self):
        self.X -= 3
        Player.Move_Right(self)

    def Move_Down(self):
        self.Y += 40
        screen.blit(self.image, (self.X, self.Y))


enemy_list = []
for i in range(enemy_num):
    enemy = Enemy(enemyimage, random.randint(0, 735), random.randint(20, 150), "left")
    enemy_list.append(enemy)


class Bullet(Player):
    def __init__(self, image, X, Y, state):
        Player.__init__(self, image, X, Y, state)

    def fire_bullet(self):
        self.Y -= 5
        screen.blit(self.image, (self.X, self.Y))


bullet_list = []
for i in range(bullet_num):
    bullet = Bullet(bulletimage, player1.X + 16, player1.Y + 10, "ready")
    bullet_list.append(bullet)


class Caption:
    def __init__(self, font_type, x, y, size, color, caption_text):
        self.font_type = font_type
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.caption_text = caption_text

    def show_caption(self):
        cur_font = pygame.font.Font(self.font_type, self.size)
        caption = cur_font.render(self.caption_text, True, self.color)
        screen.blit(caption, (self.x, self.y))


def is_collocion(bullet_list, enemy_list):
    global game_score
    for enemy in enemy_list:
        for bullet in bullet_list:
            distance = math.sqrt(
                math.pow((enemy.X + 32) - (bullet.X + 12), 2) + (math.pow((enemy.Y + 30) - bullet.Y, 2)))
            if distance < 35:
                explosionSound.play()
                bullet.Y = 480
                bullet.state = "ready"
                enemy.X = random.randint(0, 735)
                enemy.Y = random.randint(20, 150)
                game_score += 1


def is_game_over(enemy_list):
    global game_status
    if game_status == "ready":
        for enemy in enemy_list:
            if enemy.Y > 430:
                for i in enemy_list:
                    i.Y = 4000
                game_status = "over"


running = True
while running:

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.state = "left"
                player1.Move_Left()
            if event.key == pygame.K_RIGHT:
                player1.state = "right"
                player1.Move_Right()
            if event.key == pygame.K_SPACE:
                for bullet in bullet_list:
                    if bullet.state == "ready":
                        bullet.X = player1.X + 16
                        bullet.state = "fire"
                        bullet.fire_bullet()
                        bulletSound.play()
                        break

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.state = "stop"
                player1.Stop_Moving()

    if player1.X <= 0:
        player1.X = 0
    elif player1.X >= 736:
        player1.X = 736

    if player1.state == "right":
        player1.Move_Right()
    elif player1.state == "left":
        player1.Move_Left()
    else:
        player1.Stop_Moving()

    for enemy in enemy_list:
        if enemy.X <= 0:
            enemy.state = "right"
            enemy.Move_Down()
        elif enemy.X >= 736:
            enemy.state = "left"
            enemy.Move_Down()

    for enemy in enemy_list:
        if enemy.state == "left":
            enemy.Move_Left()
        elif enemy.state == "right":
            enemy.Move_Right()

    for bullet in bullet_list:
        if bullet.Y <= 0:
            bullet.Y = 480
            bullet.state = "ready"

    for bullet in bullet_list:
        if bullet.state == "fire":
            bullet.fire_bullet()

    is_collocion(bullet_list, enemy_list)

    score = Caption(font1, 10, 10, 32, (255, 255, 255), "Score is: " + str(game_score))
    score.show_caption()
    atomic_bomb = Caption(font1, 545, 10, 32, (255, 255, 255), "Atomic Bomb: " + str(atomic_bomb_num))
    atomic_bomb.show_caption()

    is_game_over(enemy_list)
    if game_status == "over":
        game_over = Caption(font1, 200, 200, 70, (255, 255, 255), "Game Over")
        game_over.show_caption()
    pygame.display.update()
