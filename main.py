# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player_1  = Player(x, y)
    
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    
    field = AsteroidField()
    
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable) 
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for player in updatable:
            player.update(dt)
            
        for asteroid in asteroids:
            if asteroid.colliding(player_1):
                print("Game Over!")                
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.colliding(shot):
                    asteroid.split()
                    shot.kill()
                    
        for player in drawable:
            player.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()