__author__ = 'Andrew'
import pygame
import random
from Player import *


def main():
    height = 400
    width = height*16/9
    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    running = True
    elapsed_time = 0
    updates = 0
    update_time = 0

    player = Player(width/2, height/2, 1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.direction += 20
                if event.key == pygame.K_RIGHT:
                    player.direction -= 20
                if event.key == pygame.K_UP:
                    player.velocity += .5
                if event.key == pygame.K_DOWN:
                    player.velocity -= .5
        delta = clock.tick()
        update_time += delta
        elapsed_time += delta

        #all game logic goes here everything within the if statement is run 60 times per second
        if update_time >= 1000/60:
            if player.x_pos > width:
                player.x_pos = 0
            if player.x_pos + player.width < 0:
                player.x_pos = width
            if player.y_pos > height:
                player.y_pos = 0
            if player.y_pos + player.height < 0:
                player.y_pos = height
            player.update()
            updates += 1
            update_time = 0
        if elapsed_time >= 1000:
            pygame.display.set_caption("FPS: " + str(clock.get_fps()) + " Updates: " + str(updates))
            updates = 0
            elapsed_time = 0

        screen.fill((255, 255, 255))
        screen.blit(player.image, (player.x_pos, player.y_pos))
        pygame.display.flip()

main()