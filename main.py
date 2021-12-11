import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 40
        self.top = 40
        self.cell_size = 40

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    color = 'white'
                elif self.board[i][j] == 1:
                    color = 'red'
                elif self.board[i][j] == 2:
                    color = 'blue'
                pygame.draw.rect(screen, color, (self.left + j * self.cell_size,
                                                   self.top + i * self.cell_size,
                                                   self.cell_size,
                                                   self.cell_size),
                                 0 if self.board[i][j] else 1)

    def get_cell(self, mouse_pos):
        x_cell = ((mouse_pos[0] - self.left) // self.cell_size)
        y_cell = ((mouse_pos[1] - self.top) // self.cell_size)
        if self.width > x_cell >= 0 and self.height > y_cell >= 0:
            return x_cell, y_cell
        return None

    def on_click(self, cell_coords):
        j, i = cell_coords
        if self.board[i][j] == 0:
            self.board[i][j] = 1
        elif self.board[i][j] == 1:
            self.board[i][j] = 2
        elif self.board[i][j] == 2:
            self.board[i][j] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        x = cell[0]
        y = cell[1]
        if cell:
            self.on_click((x, y))


pygame.init()
screen = pygame.display.set_mode((300, 350))
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            board.get_click(mouse_pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()