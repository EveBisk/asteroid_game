import sys

import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroid_field import AsteroidField
from shot import  Shot
def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    display = pygame.display
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x0 = SCREEN_WIDTH/2
    y0 = SCREEN_HEIGHT/2

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Player.containers = (updatables, drawables)
    Shot.containers = (updatables, drawables, shots)

    player = Player(x0, y0)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updt in updatables:
            updt.update(dt)

        screen.fill(color=(0, 0, 0))

        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over")
                sys.exit()

            for bullet in shots:
                if asteroid.collides(bullet):
                    asteroid.split()
                    bullet.kill()

        display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
