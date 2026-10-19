import sys
import pygame


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Moving Rectangles")


BACKGROUND_COLOR = (30, 30, 30) 
RECT1_COLOR = (0, 128, 255) 
RECT2_COLOR = (255, 100, 0)  

rect1 = pygame.Rect(200, 250, 60, 60)


rect2 = pygame.Rect(550, 250, 60, 60)

speed = 5


clock = pygame.time.Clock()


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_LEFT] and rect1.left > 0:
        rect1.x -= speed
    if keys[pygame.K_RIGHT] and rect1.right < SCREEN_WIDTH:
        rect1.x += speed
    if keys[pygame.K_UP] and rect1.top > 0:
        rect1.y -= speed
    if keys[pygame.K_DOWN] and rect1.bottom < SCREEN_HEIGHT:
        rect1.y += speed


    if keys[pygame.K_a] and rect2.left > 0:
        rect2.x -= speed
    if keys[pygame.K_d] and rect2.right < SCREEN_WIDTH:
        rect2.x += speed
    if keys[pygame.K_w] and rect2.top > 0:
        rect2.y -= speed
    if keys[pygame.K_s] and rect2.bottom < SCREEN_HEIGHT:
        rect2.y += speed

    
    screen.fill(BACKGROUND_COLOR) 

    
    pygame.draw.rect(screen, RECT1_COLOR, rect1)
    pygame.draw.rect(screen, RECT2_COLOR, rect2)

   
    pygame.display.flip()

    
    clock.tick(60)


pygame.quit()
sys.exit()
