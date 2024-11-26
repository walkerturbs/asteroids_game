from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__ (self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.player_radius = PLAYER_RADIUS
        self.cool_down = 0
        
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self, dt):
        self.cool_down -= dt
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if self.cool_down <= 0:
            shot = Shot(self.position, self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED 
            self.cool_down += PLAYER_SHOOT_COOLDOWN 
        