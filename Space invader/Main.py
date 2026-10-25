import math
import random
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=170
PLAYER_START_Y=180
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED=10
COLLISION_DIATANCE=27

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode(SCREEN_WIDTH,
SCREEN_HEIGHT)
background=pygame.image.load("Background.jfif")
background=pygame.transform.scale(background,(SCREEN_WIDTH,
SCREEN_HEIGHT))
pygame.display.set_caption("Space invader")
pygame.display.set_icon(pygame.image.load("ufo image.png"))
playering=pygame.image.load("Player.png")
playering=pygame.transform.scale(playering,(64,64))
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0
num_of_enimies=6