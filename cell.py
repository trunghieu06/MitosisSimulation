from const import *

def random_vector(a, b, c, d):
    return np.array((random.uniform(a, b), random.uniform(c, d)), dtype=np.float64)

def random_color():
    return (random.uniform(100, 255), random.uniform(100, 255), random.uniform(100, 255))
    
class Cell:
    def __init__(self, pos = random_vector(0, WIDTH, 0, HEIGHT), r = 60, c = random_color()):
        self.pos = pos
        self.r = r
        self.c = c
    def move(self):
        velo = random_vector(-max_velo, max_velo, -max_velo, max_velo)
        self.pos += velo
    def mitosis(self):
        new_cell = Cell(pos=self.pos + random_vector(-10, 10, -10, 10), r=self.r / 1.5, c=self.c)
        return new_cell

    def show(self):
        pygame.draw.circle(SCREEN, self.c, self.pos, self.r)
        pygame.draw.circle(SCREEN, BLACK, self.pos, self.r, 3)
