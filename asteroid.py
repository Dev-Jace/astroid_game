import pygame
import random
from CircleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        #pass
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        for i in range (0,2):
            asteroid2 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
            asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, random.uniform(20,50) )
            
        