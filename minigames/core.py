import pygame
pygame.init()
window = pygame.display.set_mode((700, 600))
window.fill((200, 255, 255))
clock = pygame.time.Clock()
font_size = 30
font = pygame.font.SysFont("Futura",font_size)

class Area():
    def __init__(self, x, y, width=75, height=75, color=None):
        self.rect = pygame.Rect(x, y, width, height) 
        self.fill_color = color
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def new_file(self, filename):
        self.image = pygame.image.load(filename)

class Label(Area):
    def set_text(self, text):
        self.text = text
    def set_text_settings(self, font_name, font_size, text_color=(0,0,0)):
        font = pygame.font.SysFont(font_name, font_size)
        self.text_render = font.render(self.text, True, text_color)

    def draw_text(self, shift_x=0, shift_y=0):
        x = self.rect.x + shift_x
        y = self.rect.y + shift_y
        window.blit(self.text_render,(x,y))