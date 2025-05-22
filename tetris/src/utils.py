import pygame

pygame.font.init()
FONT = pygame.font.SysFont('arial', 20)

def draw_text(surface, text, x, y, color=(255, 255, 255)):
    img = FONT.render(text, True, color)
    surface.blit(img, (x, y))
