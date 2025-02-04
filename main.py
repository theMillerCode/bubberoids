import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)



    while True:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Clear screen
        screen.fill((0, 0, 0))
        
        # Draw player
        player.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
