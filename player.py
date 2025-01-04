import pygame
from CircleShape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_TURN_SPEED, 
                       PLAYER_SPEED,PLAYER_SHOOT_SPEED,SHOT_RADIUS)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_LEFT]:
            #print("rotate counter-clockwise")
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            # rotate clockwise
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            # rotate clockwise
            if self.cooldown <= 0:
                self.shoot(self.rotation)
                self.cooldown = 0.3
        
        self.cooldown -= dt
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #print("draw player")
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def shoot(self, rotation):
        bullet = Shot(self.position[0], self.position[1])
        bullet.velocity = pygame.Vector2(0,1).rotate(rotation)
#

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius*3,2)

    def update(self,dt):
        #pass
        self.position += self.velocity * dt * PLAYER_SHOOT_SPEED
#