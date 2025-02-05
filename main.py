import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    dt = 0

    while True:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

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
