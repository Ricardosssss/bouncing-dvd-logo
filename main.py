import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((750, 450))

speed = [1, 1]

dvd = pygame.image.load("dvd.png")
dvd = pygame.transform.scale(dvd, (169.5, 74.5))
dvd_rect = dvd.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    dvd_rect = dvd_rect.move(speed[0], speed[1])
    if dvd_rect.left < 0 or dvd_rect.right > 750:
        speed[0] = -speed[0]
    if dvd_rect.top < 0 or dvd_rect.bottom > 450:
        speed[1] = -speed[1]

    screen.fill("black")
    screen.blit(dvd, dvd_rect)
    pygame.display.flip()