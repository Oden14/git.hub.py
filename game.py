
import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

class Button:
    def __init__(self, text, x, y, width, height, function):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, 1, (0, 0, 0))
        screen.blit(text, (self.x + self.width / 4 - text.get_width() / 4, self.y + self.height / 4 - text.get_height() / 4))

    def check_click(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            self.function()

def quit_game():
    pygame.quit()

def start_game():
    print("Starting game...")

button1 = Button("Start", 200, 200, 200, 50, start_game)
button2 = Button("Quit", 200, 300, 200, 50, quit_game)
button3 = Button("2 player", 200,100, 200, 50, start_game)
button4 = Button("1 player", 200, 400, 200, 50, start_game)

running = True
while running:
    screen.fill((0, 0, 0))
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            button1.check_click(mouse_pos)
            button2.check_click(mouse_pos)
            button3.check_click(mouse_pos)
            button4.check_click(mouse_pos)
    pygame.display.flip()
