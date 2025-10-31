import pygame
import math

class SingleBullet:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        #print(f"Bullet launched in direction {direction}")

        self.rect = pygame.Rect(x, y, 10, 10)

        self.bullet_speed = 10

        self.bullet_color = (192, 192, 192)

    
    def move(self):

        if self.direction == "up":
            self.y -= self.bullet_speed
        elif self.direction == "down":
            self.y += self.bullet_speed
        elif self.direction == "left":
            self.x -= self.bullet_speed
        elif self.direction == "right":
            self.x += self.bullet_speed

        self.rect.topleft = (self.x, self.y)


    def draw(self, screen, camera_x, camera_y):
        pygame.draw.rect(screen, self.bullet_color, (self.rect.x - camera_x, self.rect.y - camera_y, 10, 10))
    

class ShotgunBullet:

    def __init__(self, x, y, direction, angle_offset=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.angle_offset = math.radians(angle_offset)

        print(f"Bullet launched in direction {direction} with angle offset {angle_offset}")

        self.rect = pygame.Rect(x, y, 10, 10)
        self.bullet_speed = 10
        self.bullet_color = (192, 192, 192)

        self.dx, self.dy = self.get_movement_vector(direction, self.angle_offset)
    
    def get_movement_vector(self, direction, angle_offset):

        direction_angles = {
            "up": -math.pi / 2,
            "down": math.pi / 2,
            "left": math.pi,
            "right": 0
        }

        base_angle = direction_angles[direction]

        final_angle = base_angle + angle_offset

        dx = math.cos(final_angle) * self.bullet_speed
        dy = math.sin(final_angle) * self.bullet_speed

        return dx, dy
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen, camera_x, camera_y):
        pygame.draw.rect(screen, self.bullet_color,
                         (self.rect.x - camera_x, self.rect.y - camera_y, 10, 10))