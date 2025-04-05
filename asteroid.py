from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,SHOT_RADIUS):
        super().__init__(x,y,SHOT_RADIUS)


    def draw(self,screen):
        pygame.draw.circle(screen,"White", self.position, self.radius)

    def update(self,dt):
        self.position += (self.velocity * dt)





