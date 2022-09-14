import pygame

class Button:
    isHover = False

    def __init__(self, settings, x, y, width, height, default_color, hover_color, border_color, text='', font_size=20):
        self.settings = settings
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.default_color = default_color
        self.hover_color = hover_color
        self.border_color = border_color
        self.text = text
        self.font_size = font_size

    # Draw the mouse to the screen
    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, 
            self.hover_color if self.isHover else self.default_color,
            pygame.Rect(self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('georgia', self.font_size)
            text = font.render(self.text, 1, (0,0,0))
            SCREEN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    # Returns true is the mouse is hovering over the button
    def isMouseOver(self, mouse_x, mouse_y):
        if (mouse_x > self.x and mouse_x < self.x + self.width):
            if (mouse_y > self.y and mouse_y < self.y + self.height):
                return True
        return False