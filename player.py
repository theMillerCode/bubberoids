from pygame import Color
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        
        super().__init__(x, y, PLAYER_RADIUS)

        #self.position = pygame.Vector2(x, y)
        self.rotation = 0

        #timer
        self.fire_rate = 0

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
        pygame.draw.polygon(screen, Color("white"), self.triangle(), 2 )
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.fire_rate <= 0:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            # Create new shot at player position
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            # Set shot velocity
            shot.velocity = direction * PLAYER_SHOOT_SPEED
            self.fire_rate = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.fire_rate > 0:
            self.fire_rate -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    