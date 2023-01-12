import pygame as pg

def rainbow_color(value):
    step = (value*1536 // 255) % 6
    pos = value*1536 % 255
    if step == 0:
        return (255, pos, 0)
    if step == 1:
        return (255-pos, 255, 0)
    if step == 2:
        return (0, 255, pos)
    if step == 3:
        return (0, 255-pos, 255)
    if step == 4:
        return (pos, 0, 255)
    if step == 5:
        return (255, 0, 255-pos)

def devide(top_left, size, depth):
    if depth != 0:
        segment = size/3
        color = rainbow_color(depth/max_depth)

        pg.draw.rect(screen, color, pg.Rect(top_left[0]+segment, top_left[1]+segment, segment, segment))
        
        for x in range(3):
            for y in range(3):
                if x==1 and y==1:
                    pass
                else:
                    devide((top_left[0] + segment*x, top_left[1] + segment*y), segment, depth-1)

pg.init()

screen = pg.display.set_mode((800,800))
screen.fill((255,255,255))

start_1 = (0,0)
start_2 = (800,800)

max_depth = 6


while 1:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()

    devide(start_1, 800, max_depth)
    max_depth = 6

    pg.display.flip()
