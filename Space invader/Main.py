import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 170
PLAYER_START_Y = 420
PLAYER_SPEED = 5
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
ENEMY_SIZE = 50
NUM_ENEMIES = 6

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

background = pygame.image.load("Background.jfif").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_icon(pygame.image.load("ufo image.png"))

player_image = pygame.image.load("Player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (64, 64))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg, enemyX, enemyY, enemyX_change, enemyY_change = [], [], [], [], []
for i in range(NUM_ENEMIES):
    enemy_img = pygame.image.load("Enemy.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (ENEMY_SIZE, ENEMY_SIZE))
    enemyImg.append(enemy_img)
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet_img = pygame.image.load("Bullet.png").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (16, 32))
bulletX = 0
bulletY = PLAYER_START_Y
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

running = True
game_over = False


def reset_enemy(index):
    enemyX[index] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
    enemyY[index] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)


while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX + 24
                bulletY = playerY
                bullet_state = "fire"
            elif event.key == pygame.K_q and game_over:
                running = False
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0

    if not game_over:
        playerX += playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

        if bullet_state == "fire":
            bulletY -= BULLET_SPEED_Y
            screen.blit(bullet_img, (bulletX, bulletY))
            if bulletY <= 0:
                bulletY = PLAYER_START_Y
                bullet_state = "ready"

        for i in range(NUM_ENEMIES):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_SIZE:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            screen.blit(enemyImg[i], (enemyX[i], enemyY[i]))

            if bullet_state == "fire" and math.hypot(
                enemyX[i] + ENEMY_SIZE / 2 - (bulletX + 8),
                enemyY[i] + ENEMY_SIZE / 2 - bulletY,
            ) < COLLISION_DISTANCE + 10:
                score += 1
                bulletY = PLAYER_START_Y
                bullet_state = "ready"
                reset_enemy(i)

            if enemyY[i] + ENEMY_SIZE >= playerY and abs(
                enemyX[i] + ENEMY_SIZE / 2 - (playerX + 32)
            ) < 40:
                game_over = True

        if game_over:
            screen.blit(game_over_font.render("Game Over", True, (255, 255, 255)), (180, 220))

    screen.blit(player_image, (playerX, playerY))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        screen.blit(game_over_font.render("Game Over", True, (255, 255, 255)), (180, 220))
        quit_text = font.render("Press Q to quit", True, (255, 255, 255))
        screen.blit(quit_text, (220, 300))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
