import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rope Simulation")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)

particles = []
segments = []
GRAVITY = 0.5
SEGMENT_LENGTH = 20
dragging = False
running_physics = False

class Particle:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.old_pos = pygame.Vector2(pos)
        self.radius = 5
        self.pinned = False
        self.locked = False
    
    def update(self, dt):
        if self.pinned or self.locked:
            return

        velocity = self.pos - self.old_pos
        self.old_pos = self.pos.copy()
        self.pos += velocity + pygame.Vector2(0, GRAVITY)

    def draw(self):
        pygame.draw.circle(screen, RED, self.pos, self.radius)

    def constrain(self):
        if self.pos.y > HEIGHT - 10:
            self.pos.y = HEIGHT - 10
            self.old_pos.y = HEIGHT - 10
        if self.pos.x < 10:
            self.pos.x = 10
            self.old_pos.x = 10
        if self.pos.x > WIDTH - 10:
            self.pos.x = WIDTH - 10
            self.old_pos.x = WIDTH - 10

def create_segment(p1, p2):
    segments.append((p1, p2))

def update_segments():
    for p1, p2 in segments:
        dir = p1.pos - p2.pos
        dist = dir.length()
        if dist == 0:
            continue
        offset = dir.normalize() * SEGMENT_LENGTH
        mid = (p1.pos + p2.pos) / 2
        p1.pos = mid + offset / 2
        p2.pos = mid - offset / 2

while True:
    dt = clock.tick(60) / 1000 
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # ПКМ
            pos = pygame.mouse.get_pos()
            particles.append(Particle(pos))
            if len(particles) >= 2:
                create_segment(particles[-2], particles[-1])

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running_physics = not running_physics
            if particles:
                particles[0].pinned = True

    if running_physics:
        for p in particles:
            p.update(dt)
            p.constrain()
        
        for _ in range(5): 
            for p1, p2 in segments:
                dir = p1.pos - p2.pos
                dist = dir.length()
                if dist == 0:
                    continue
                delta = (dist - SEGMENT_LENGTH) / dist * 0.5
                if not p1.pinned:
                    p1.pos -= dir * delta
                if not p2.pinned:
                    p2.pos += dir * delta

    for p1, p2 in segments:
        pygame.draw.line(screen, BLACK, p1.pos, p2.pos, 2)
    for p in particles:
        p.draw()

    pygame.display.flip()