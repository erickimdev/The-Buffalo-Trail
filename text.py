import pygame

class Text:
    def __init__(self, text, x, y, text_size, color):
        self.text = text
        self.x = x
        self.y = y
        self.text_size = text_size
        self.color = color

    def draw(self, screen):
        font = pygame.font.Font('assets/font.TTF', self.text_size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)
        screen.blit(text_surface, text_rect)