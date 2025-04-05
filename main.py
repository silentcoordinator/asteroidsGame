from constants import *
import pygame
from player import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
