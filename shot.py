from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__ (self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.shot_radius = SHOT_RADIUS
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.shot_radius)
    
    def update(self, dt):
        self.position += self.velocity * dt