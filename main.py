from asteroid import *
from constants import *
import pygame
from player import *
from asteroidfield import *
from circleshape import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,asteroid_field_group)
    Shot.containers = (updatable,drawable,shots_group)



    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    af = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots_group:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()



        for asteroid in asteroids:
            if asteroid.collide(player):
                return print("Game Over!")
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
