from display import *
from draw import *

screen = new_screen()
wcolor = [ 0, 255, 0 ]
color = [255,0,255]
volor = [255,100,100]


l = 150
w = 100
h = 50
l1 = 50
w1 = 150
h1 = 100
l2 = 100
w2 = 50
h2 = 150

root3 = 1.73205080757

def drawprism(x0,y0,l,w,h,screen,color):
    vertices = [[int(x0+root3*w/2),int(y0+w/2)],[int(x0+root3*l/2),int(y0-l/2)],[x0,y0-h],
                [int(x0+(l+w)*root3/2),int(y0+(w-l)/2)],[int(x0+root3*w/2),int(y0+w/2-h)],
                [int(x0+root3*l/2),int(y0-l/2-h)],[int(x0+(l+w)*root3/2),int(y0-h+(w-l)/2)]]
    draw_line(x0,y0,vertices[0][0],vertices[0][1],screen,color)
    draw_line(x0,y0,vertices[1][0],vertices[1][1],screen,color)
    draw_line(x0,y0,vertices[2][0],vertices[2][1],screen,color)
    draw_line(vertices[0][0],vertices[0][1],vertices[3][0],vertices[3][1], screen, color)
    draw_line(vertices[0][0],vertices[0][1],vertices[4][0],vertices[4][1], screen, color)
    draw_line(vertices[1][0],vertices[1][1],vertices[3][0],vertices[3][1], screen, color)
    draw_line(vertices[1][0],vertices[1][1],vertices[5][0],vertices[5][1], screen, color)
    draw_line(vertices[2][0],vertices[2][1],vertices[5][0],vertices[5][1], screen, color)
    draw_line(vertices[2][0],vertices[2][1],vertices[4][0],vertices[4][1], screen, color)
    draw_line(vertices[3][0],vertices[3][1],vertices[6][0],vertices[6][1], screen, color)
    draw_line(vertices[4][0],vertices[4][1],vertices[6][0],vertices[6][1], screen, color)
    draw_line(vertices[5][0],vertices[5][1],vertices[6][0],vertices[6][1], screen, color)

start1x = int(250-30-root3/2*w)
start1y = int(250 - w/2)
start2x = int(start1x - l1*root3/2)
start2y = int(start1y + l1/2 + h1)
start3x = 250 + 12
start3y = start2y+50
drawprism(start1x,start1y-2,l,w,h,screen,wcolor)
drawprism(start2x,start2y,l1,w1,h1,screen,volor)
drawprism(start3x,start3y,l2,w2,h2,screen,color)

save_extension(screen, 'img.png')
display(screen)
