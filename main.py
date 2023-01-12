import pygame as pg

def devide(top_left, botton_right, depth=4):
    if depth != 0:
        segment = (botton_right[0]-top_left[0])/3
        pg.draw.rect(screen, (0,0,0), pg.Rect(top_left, botton_right), 10)

        #devide(top_left, (top_left[0]+segment, top_left[1]+segment), depth-1)
        devide((top_left[0]+segment,top_left[1]), (botton_right[0]-segment, top_left[1]+segment), depth-1)
        #devide((top_left[0]+segment*2,top_left[1]), (botton_right[0], top_left[1]+segment), depth-1)
        #devide((top_left[0],top_left[1]+segment), (top_left[0]+segment, segment), depth-1)
        #devide((top_left[0]+segment*2,top_left[1]+segment), (botton_right[0], segment), depth-1)
        #devide((top_left[0]+segment*2,top_left[0]+segment*2), botton_right, depth-1)
        #devide((top_left[0],botton_right[1]-segment), (top_left[0]+segment, botton_right[1]), depth-1)



pg.init()

screen = pg.display.set_mode((800,800))
screen.fill((255,255,255))

start_1 = (0,0)
start_2 = 800,800


while 1:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()

    devide(start_1, start_2)

    pg.display.flip()
