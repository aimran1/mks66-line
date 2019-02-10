from display import *
from draw import *

screen = new_screen()
wcolor = [ 0, 255, 0 ]
color = [255,0,255]
#45 Degrees UP
draw_line(0,0,500,500,screen,wcolor)
#45 Degrees DOWN
draw_line(0,500,500,0,screen,color)
#Vertical
draw_line(0,0,0,500,screen,wcolor)
#Vertical RIGHT
draw_line(499,0,499,500,screen,color)
#Horizontal
draw_line(0,0,500,0,screen,wcolor)
#Horizontal UP
draw_line(0,500,500,499,screen,color)
#Octant 1
draw_line(0,0,500,100,screen,wcolor)
#Octant 2
draw_line(0,0,100,500,screen,wcolor)
#Octant 8
draw_line(0,500,500,400,screen,color)
#Octant 7
draw_line(0,500,100,0,screen,color)
display(screen)
save_extension(screen, 'img.png')
