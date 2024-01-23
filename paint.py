import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 500
GUI_MARGIN = 75
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

# colors
white = pygame.color.Color('white')
black = pygame.color.Color('black')
red = pygame.color.Color('red')
blue = pygame.color.Color('blue')
yellow = pygame.color.Color('yellow')
orange = pygame.color.Color('orange')
green = pygame.color.Color('green')
purple = pygame.color.Color('purple')

#font
font = pygame.font.SysFont('Arial', 15)

#brush

brush_size = 5
eraser_brush_size = 5
paint = False 


class Paint():
    def __init__(self, color):
        self.color = color
        self.paint_data_coordinates = []
        self.paint_data_tuple = []  
        
    def draw_cursor(self, x, y, size):
        pygame.draw.circle(screen, yellow, (x, y), size)

    def draw_brush(self, screen, color,  x, y, radius):
        point = pygame.draw.circle(screen, color,(x, y), radius)
        return point
    
    
    def draw_world(self, color):
        for x, y in self.paint_data_coordinates:
            rect = self.draw_brush(screen, color,x, y, brush_size)
            self.paint_data_tuple.append((rect, x, y))
            
    def erase(self,input_rect):
        for rect, x, y in self.paint_data_tuple:
            if input_rect.colliderect(rect):
                for circle in self.paint_data_coordinates:
                    if circle == (x, y):
                        self.paint_data_coordinates.remove(circle)
                    
    def clear(self):
        self.paint_data_coordinates.clear()
        self.paint_data_tuple.clear()
        
      

def button(screen,colour, x, y, width, height, border_width=0):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, colour, button, border_width)
    return button

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

paint_instances = []            
initial_brush = Paint(black) 
paint_instances.append(initial_brush)



run = True
while run:
    screen.fill(white)
    mx, my = pygame.mouse.get_pos()
    
    
    
    
    
    
    #colour menu
    yellow_button = button(screen, yellow, 400, 330, 30, 30)
    if yellow_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           yellow_brush = Paint(yellow)
           paint_instances.append(yellow_brush)
    red_button = button(screen, red, 400, 360, 30, 30)
    if red_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           red_brush = Paint(red)
           paint_instances.append(red_brush)
    blue_button = button(screen, blue, 430, 330, 30, 30)
    if blue_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           blue_brush = Paint(blue)
           paint_instances.append(blue_brush)
    green_button = button(screen, green, 430, 360, 30, 30)
    if green_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           green_brush = Paint(green)
           paint_instances.append(green_brush)
    orange_button = button(screen, orange, 460, 330, 30, 30)
    if orange_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           orange_brush = Paint(orange)
           paint_instances.append(orange_brush)
    purple_button = button(screen, purple, 460, 360, 30, 30)
    if purple_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           purple_brush = Paint(purple)
           paint_instances.append(purple_brush)
    black_button = button(screen, black, 370, 330, 30, 30)
    if black_button.collidepoint((mx, my)):
       if pygame.mouse.get_pressed()[0]:
           black_brush = Paint(black)
           paint_instances.append(black_brush)
    #clear button
    clear_button = button(screen, red, 100, 330, 50, 30, 1)
    draw_text("clear", font, red, 112, 335)
    if clear_button.collidepoint((mx, my)):
        if pygame.mouse.get_pressed()[0]:
            for brush in paint_instances:
                brush.clear()
    
        
           
           
    
    if mx  < SCREEN_WIDTH and my < SCREEN_HEIGHT - GUI_MARGIN:
        if pygame.mouse.get_pressed()[0]:
            for brush in paint_instances:
                brush.paint_data_coordinates.append((mx, my))
        if pygame.mouse.get_pressed()[2]:
            rect = brush.draw_brush(screen, black, mx, my, eraser_brush_size)
            for brush in paint_instances:
                brush.erase(rect)
    for brush in paint_instances:
        brush.draw_world(brush.color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                sys.exit()
        
            
    clock.tick(FPS)        
    pygame.display.update()