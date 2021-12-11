import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 40
        self.q = 1

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, 'white', (self.left + j * self.cell_size,
                                                   self.top + i * self.cell_size,
                                                   self.cell_size,
                                                   self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x_cell = ((mouse_pos[0] - self.left) // self.cell_size)
        y_cell = ((mouse_pos[1] - self.top) // self.cell_size)
        if self.width > x_cell >= 0 and self.height > y_cell >= 0:
            return x_cell, y_cell
        return None

    def on_click(self, cell_coords):
        j, i = cell_coords
        cell = self.get_cell(mouse_pos)
        if self.q == 1:
            if self.board[i][j] == 2:
                x = cell[0]
                y = cell[1]
                for j in range(self.width):
                    x_1 = j * self.cell_size + self.cell_size // 2
                    y_1 = y * self.cell_size + self.cell_size // 2
                    pygame.draw.circle(screen, 'red', (x_1, y_1), 17)



    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        x = cell[0]
        y = cell[1]
        if cell:
            self.on_click((x, y))



pygame.init()
screen = pygame.display.set_mode((500, 400))
board = Board(10, 8)
screen.fill((0, 0, 0))
width = 10
height = 8
cell_size = 40
for i in range(height // 2):
    for j in range(width):
        x_1 = j * cell_size + cell_size // 2
        y_1 = i * cell_size + cell_size // 2
        pygame.draw.circle(screen, 'red', (x_1, y_1), 17)
for i in range(height // 2, height):
    for j in range(width):
        x_1 = j * cell_size + cell_size // 2
        y_1 = i * cell_size + cell_size // 2
        pygame.draw.circle(screen, 'blue', (x_1, y_1), 17)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            board.get_click(mouse_pos)
    board.render(screen)
    pygame.display.flip()