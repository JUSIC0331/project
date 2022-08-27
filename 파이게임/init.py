import pygame
from pygame.locals import QUIT
import sys
pygame.init()
배경=pygame.display.set_mode((800,800))
pygame.display.set_caption("JustWindow") # 제목
클럭 = pygame.time.Clock()


def main():
    while True:
        배경.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.draw.line(배경, (250,0,0),(10,80),(200,80))
        pygame.draw.rect(배경,(255,0,0),(10,20,100,50))
        for i in range(0,800,40):
            pygame.draw.circle(배경,(255,0,0),(i+20,20),20)
        for j in range(0,800,40):
            for y in range(0,800,40):
                pygame.draw.circle(배경,(255,0,0),(j+20,y+20),20)   

        for xpos in range(0,800,40):
            pygame.draw.line(배경,(0,0,0),(xpos,0),(xpos,800))

        for ypos in range(0,800,40):
            pygame.draw.line(배경,(0,0,0),(0,ypos),(800,ypos))
        pygame.display.update()
        클럭.tick(5)

main()




