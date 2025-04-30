import pygame as pg

pg.font.init()

screen = pg.display.set_mode((500, 400) , pg.FULLSCREEN)

pg.display.set_caption("Pgame")

clock = pg.time.Clock()

font = pg.sysfont.SysFont("sans", 100)


image = pg.image.load("megagy.jpg").convert_alpha()

img = image.subsurface(0, 0, 20, image.get_height())

image = pg.transform.scale(image, (200, 350))
image = pg.transform.rotate(image, 45
                            )

x, y = 125,125
spd = 50
rad = 15

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill((255, 255, 255))
    keys = pg.key.get_pressed()
    if keys[pg.K_0]:
        pg.draw.rect(screen, (0, 255, 0), (150,50,50,50))

    if keys[pg.K_UP]:
        y -= spd

    if keys[pg.K_DOWN]:
        y += spd

    if keys[pg.K_LEFT]:
        x -= spd

    if keys[pg.K_RIGHT]:
        x += spd

    if keys[pg.K_ESCAPE]:
        exit()

    if x - rad < 0:
        x += spd

    if x + rad > screen.get_width():
        x -= spd

    if y - rad < 0:
        y += spd

    if y + rad > screen.get_height():
        y -= spd

    pg.draw.circle(screen, (0, 0, 0), (x, y), rad)
    screen.blit(image, (50,50))
    text = font.render("GRafinia zadefaie", False, (229,0,0))
    screen.blit(text, (0, 0))
    pg.display.flip()
    clock.tick(100)