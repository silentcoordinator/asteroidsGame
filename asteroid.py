from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,SHOT_RADIUS):
        super().__init__(x,y,SHOT_RADIUS)


    def draw(self,screen):
        pygame.draw.circle(screen,"White", self.position, self.radius)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)
        self.velocity = pygame.Vector2.rotate(self.velocity,random_angle)

        new_velocity1 = self.velocity.rotate(-random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(random_angle) * 1.2

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        asteroidOne = Asteroid(self.position.x,self.position.y, newRadius)
        asteroidTwo = Asteroid(self.position.x,self.position.y, newRadius)

        asteroidOne.velocity = new_velocity1
        asteroidTwo.velocity = new_velocity2








