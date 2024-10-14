import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        vec_plus = self.velocity.rotate(angle)
        vec_minus = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_plus = Asteroid(self.position.x, self.position.y, new_radius)
        ast_plus.velocity = vec_plus*1.2

        ast_minus = Asteroid(self.position.x, self.position.y, new_radius)
        ast_minus.velocity = vec_minus
