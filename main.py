# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (170, 0, 150)
SQUARE = (250, 107, 255)
COLORS = (SQUARE, RED, BLACK)

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################


class Box:
    def __init__(self, display, x, y, width, height, color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0
        self.y_speed = random.randint(3,5)
        self.color = color

    def draw_box(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.speed

        if self.x <= 0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def drop_box(self):

        if self.y > DISPLAY_HEIGHT:
            self.x = random.randrange(0, DISPLAY_WIDTH, 5)
            self.y = random.randrange(-100, 0, 5)
            self.y_speed = random.randint(3, 5)

        self.y += self.y_speed

    def is_collided(self, other):
        counter = 0
        if(self.x <= other.x <= self.x+self.width or \
           self.x <= other.x+other.width <= self.x+self.width) and \
                (self.y < other.y+other.width < self.y+self.width or \
                self.y <= other.y + other.width <= self.y + self.width):

            counter += 1
            self.color = random.choice(COLORS)
        if counter == 3:
            return True




pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# create player
player_width = 50
x_loc = (DISPLAY_WIDTH - player_width)/2
y_loc = DISPLAY_HEIGHT - 2*player_width

# create enemies
enemy_width = 20
enemy_list = []
for i in range(10):
    x_coord = random.randrange(0, DISPLAY_WIDTH, 5)
    random_y = random.randrange(-100, 0, 5)
    print(random_y)
    enemy_list.append(Box(screen, x_coord, random_y, enemy_width, enemy_width, WHITE))

player = Box(screen, x_loc, y_loc, player_width, player_width, SQUARE)

running = True
while running:

    pos = pygame.mouse.get_pos()
    player.x = pos[0]-.5*player.width
    player.y = pos[1]-.5*player.width

    # pressed_lft = pygame.mouse.get_pressed()[0]
    # print(pressed_lft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player.speed = 5
        #     elif event.key == pygame.K_LEFT:
        #         player.speed = -5
        # elif event.type == pygame.KEYUP:
        #     player.speed = 0


    screen.fill(PINK)

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()
        if player.is_collided(enemy):
            running = False


    player.draw_box()
    player.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
