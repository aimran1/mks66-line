from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
#45 Degrees
draw_line(0,0,500,500,screen,color)
#Vertical
draw_line(0,0,0,500,screen,color)
#Horizontal
draw_line(0,0,500,0,screen,color)
#Octant 1
draw_line(0,0,500,100,screen,color)
#Octant 2
draw_line(0,0,100,500,screen,color)
display(screen)
save_extension(screen, 'img.png')
