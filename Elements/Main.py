import pygame

pygame.init()
W, H = 200, 150
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

size = 12
x, y = (W - size) // 2, (H - size) // 2
font = pygame.font.Font(None, 14)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[keys[pygame.K_LEFT] and pygame.K_LEFT]) * 2
    y += (keys[pygame.K_DOWN] - keys[keys[pygame.K_UP] and pygame.K_UP]) * 2
    x, y = max(0, min(x, W - size)), max(0, min(y, H - size))


    screen.fill((110,110,120))
    pygame.draw.rect(screen, (0, 255, 100), (x, y, size, size))
    screen.blit(font.render(f"X:{x} Y:{y}", True, (255, 255, 255)), (5, 5))
    
    pygame.display.flip()
    clock.tick(60)
    