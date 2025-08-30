import random
import pygame
import numpy as np
import sys
import math

WIDTH, HEIGHT = 800, 800
FPS = 60

max_velo = 3

BLACK = (0, 0, 0)

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Mitosis Simulation {WIDTH}x{HEIGHT}")
clock = pygame.time.Clock()

cursor_img = pygame.image.load('./images/cursor.png')
cursor_img = cursor_img.subsurface(pygame.Rect(0, 0, 16, 16)).copy()

font = pygame.font.Font('./fonts/Jersey10-Regular.ttf', 30)
font_l = pygame.font.Font('./fonts/Jersey10-Regular.ttf', 35)
font_s = pygame.font.Font('./fonts/Jersey10-Regular.ttf', 20)
