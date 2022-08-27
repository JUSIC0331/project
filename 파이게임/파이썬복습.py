import sys
import pygame
from pygame.locals import QUIT
import random

pygame.init()
배경=pygame.display.set_mode((800,800))
클럭 = pygame.time.Clock()

먹이들 = []
def 먹이만들기():
    for i in range(10):
        x , y = random.randint(0, 20),random.randint(0, 20)
        먹이들.append([x , y])

def 먹이그리기():
    for pos in 먹이들:
        pygame.draw.rect(배경,(0,255,0), (pos[0]*40,pos[0]*40,40,40))

def 선그리기():
    for i in range(0,800,40):
        pygame.draw.line(배경, (255,255,255),(0,i), (800,i))
        pygame.draw.line(배경, (255,255,255),(i,0), (i,800))

def main():
    먹이만들기()
    while True:
        배경.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        먹이그리기()
        선그리기()
        pygame.display.update()
        클럭.tick(5)

main()