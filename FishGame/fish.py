import pygame, random


class Fish(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("fish.png")
        scale = random.randint(1, 5) * 10
        self.image = pygame.transform.smoothscale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randint(2, 5))
        rotation = random.randint(0, 360)
        self.speed.rotate_ip(rotation)
        self.image = pygame.transform.rotate(self.image, 180 - rotation)

    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        # While it is longer than previous versions,
        # bouncing looks better with this code
        if self.rect.left < 0:
            self.speed[0] *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.left = 0
        elif self.rect.right > screen_info.current_w:
            self.speed[0] *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.right = screen_info.current_w
        if self.rect.top < 0:
            self.speed[1] *= -1
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.top = 0
        elif self.rect.bottom > screen_info.current_h:
            self.speed[1] *= -1
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottom = screen_info.current_h