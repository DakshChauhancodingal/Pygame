import pygame
import random
SCREEN_WIDTH,SCREEN_HEIGHT=500,400
MOVEMENT_SPEED=5
FONT_SIZE=75
pygame.init()
background_image=pygame.transform.scale(pygame.image.load("Background_image.png"),
                                        SCREEN_WIDTH,SCREEN_HEIGHT)
font=pygame.font.SysFont("Times New Roman ",FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.surface([width,height])
        self.image.fill(pygame.color("dodgerblue"))
        pygame.draw.rect(self.image,color ,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()

    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,SCREEN_WIDTH-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change,SCREEN_HEIGHT-self.rect.height),0)
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite collision")
all_sprite=pygame.sprite.Group()
sprite1=Sprite(pygame.Color("Black"),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,SCREEN_WIDTH-sprite1.rect.width)(0,SCREEN_HEIGHT-sprite1.rect.height)
all_sprite.add(sprite1)
sprite2=Sprite(pygame.Color("Red"),20,30)
sprite1.rect.x,sprite2.rect.y=random.randint(0,SCREEN_WIDTH-sprite1.rect.width)(0,SCREEN_HEIGHT-sprite1.rect.height)
all_sprite.add(sprite2)