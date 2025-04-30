
import pygame as pg
import nastrfoiki
from wotld_clash import world_map,text_map

def ray_casting(sc, player,textures):
    cur_angle = player.angle - nastrfoiki.HALF_FOV
    xo, yo = player.pos

    for ray in range(nastrfoiki.NUM_OF_RAYS):
        cos_a = nastrfoiki.math.cos(cur_angle)
        sin_a = nastrfoiki.math.sin(cur_angle)

        depth = 0
        step = nastrfoiki.TILE

        while depth < nastrfoiki.MAX_DEPTH:
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            objects = []
            #pg.draw.line(sc,nastrfoiki.WHITE, player.pos, (x, y), 5)
            if (x // nastrfoiki.TILE, y // nastrfoiki.TILE) in world_map:
                if step < 2:
                    depth *= nastrfoiki.math.cos(player.angle - cur_angle)
                    proj_height = min(nastrfoiki.PROJ_COEF/(depth+0.0001), nastrfoiki.HEIGHT)+10

                    offset = ((x/nastrfoiki.TILE-int(x/nastrfoiki.TILE))+(y/nastrfoiki.TILE-int(y/nastrfoiki.TILE)))
                    #color1= 255*(1-(depth/nastrfoiki.MAX_DEPTH))
                    #pg.draw.rect(sc,(color1, color1, color1), (ray*nastrfoiki.SCALE, nastrfoiki.HALF_HEIGHT - (proj_height/2), nastrfoiki.SCALE, proj_height ))
                    texture = text_map[int(y//nastrfoiki.TILE)][int(x//nastrfoiki.TILE)]
                    txtr = textures[texture]
                    wall_column = txtr.subsurface(offset*nastrfoiki.TILE,0, txtr.get_width()//nastrfoiki.TILE, txtr.get_height())
                    wall_column = pg.transform.scale(wall_column, (nastrfoiki.SCALE, abs(proj_height)))

                    sc.blit(wall_column, (ray*nastrfoiki.SCALE, (nastrfoiki.HALF_HEIGHT -proj_height/2)+player.height*proj_height))
                    objects.append([depth,(ray*nastrfoiki.SCALE, (nastrfoiki.HALF_HEIGHT -proj_height//2)+player.height*proj_height),wall_column])
                    break
                else:
                    depth -=  step
                    step /= 2
            depth += step
        cur_angle += nastrfoiki.DELTA_ANGLE
    return objects