# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
#from CircleShape import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    group_updateable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_astroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()
    Player.containers = (group_updateable, group_drawable)
    Asteroid.containers = (group_astroids, group_updateable, group_drawable)
    AsteroidField.containers = (group_updateable)
    Shot.containers = (group_shots,group_updateable, group_drawable)

    play_char = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #comet = Asteroid(SCREEN_WIDTH/3, SCREEN_HEIGHT/3,20)
    starry = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in group_updateable:
            thing.update(dt)

        for toids in group_astroids:
            if play_char.collision(toids):
                sys.exit("Game over!")
        for astroid in group_astroids:
            for shot in group_shots:
                if astroid.collision(shot):
                    astroid.split()
                    shot.kill()

        screen.fill("black")

        for thing2 in group_drawable:
            thing2.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

#end main

if __name__ == "__main__":
    main()
