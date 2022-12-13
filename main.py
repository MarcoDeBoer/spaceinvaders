import keyboard as keyboard
import pygame

# initialize
pygame.init()
place_x = 370
place_y = 500
WIDTH = 800
HEIGHT = 600

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-invaders.png')
# playerImg = pygame.transform.scale(playerImg, (32, 32))
playerX = place_x
playerY = place_y
playerX_change = 0


def player(x, y):
    if x <= 0:
        x = 0
    elif x >= 736:
        x = 736
    screen.blit(playerImg, (x, y))


# game loop
running = True
while running:
    # RGB = red, green, blue
    screen.fill((100, 0, 0))
    for event in pygame.event.get():
        # keyboard
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # if key is pressed check if it's right or left
            if event.key == pygame.K_LEFT:
                playerX_change = -1
                print(f'left is pressed : {playerX}')
            elif event.key == pygame.K_a:
                playerX_change = -1
                print(f'left is pressed : {playerX}')
            elif event.key == pygame.K_RIGHT:
                print(f'right is pressed : {playerX}')
                playerX_change = 1
            elif event.key == pygame.K_d:
                print(f'right is pressed : {playerX}')
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
