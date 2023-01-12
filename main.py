import pygame as pg

def devide(top_left, size, depth):
    if depth != 0:
        segment = size/3
        pg.draw.rect(screen, (0,0,0), pg.Rect(top_left[0]+segment, top_left[1]+segment, segment, segment))
        
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


while 1:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()

    devide(start_1, 800, 6)

    pg.display.flip()
