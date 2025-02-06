import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x, y) 
    asteroid_field = AsteroidField()

    dt = 0

    #game loop
    while True:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #updatable.update(dt)
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # Clear screen
        screen.fill((0, 0, 0))
        
        # Draw player
        for obj in drawable:
            obj.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
