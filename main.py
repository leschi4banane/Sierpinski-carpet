import pygame as pg

def devide(top_left, botton_right, depth):


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

    pg.draw.rect(screen, (0,0,0), pg.Rect((start_1[0], start_1[0], start_2[1], start_2[1])))

    pg.display.flip()
