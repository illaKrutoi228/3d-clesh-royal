import nastrfoiki
from wotld_clash import world_map
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.x, self.y = nastrfoiki.player_pos
        self.angle = nastrfoiki.player_angle
        self.speed = nastrfoiki.player_speed
        self.game = game
        self.sencivity = 0.004
        self.height = 0
        self.move_lock = False

    def mouse_control(self):
        if pg.mouse.get_focused():
            difference = pg.mouse.get_pos()[0] - nastrfoiki.HALF_WIDTH
            pg.mouse.set_pos((nastrfoiki.HALF_WIDTH, nastrfoiki.HALF_HEIGHT))
            self.angle += difference*self.sencivity

    @property
    def pos(self):
        return(self.x, self.y)

    def check_collisions(self,dx, dy):
        if ((self.x+dx)//nastrfoiki.TILE, (self.y+dy)//nastrfoiki.TILE) in world_map:
            return True
        return False
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pg.key.get_pressed()
        dx, dy = 0, 0
        if not self.move_lock:
            if keys[pg.K_w]:
                dx += cos_a * self.speed
                dy += sin_a * self.speed
            if keys[pg.K_s]:
                dx -= cos_a * self.speed
                dy -= sin_a * self.speed
            if keys[pg.K_a]:
                dx += sin_a * self.speed
                dy -= cos_a * self.speed
            if keys[pg.K_d]:
                dx -= sin_a * self.speed
                dy += cos_a * self.speed
        if keys[pg.K_LEFT]:
            self.angle -= .1
        if keys[pg.K_RIGHT]:
            self.angle += .1
        if keys[pg.K_SPACE] and self.height <= 0:
            self.height = 1
            dx += cos_a * self.speed*35
            dy += sin_a * self.speed*35
            self.move_lock = True
        if self.height <= 0:
            self.move_lock = False
        if self.height > 0:
            self.height -= 0.05
        if keys[pg.K_ESCAPE]:
            exit()
        self.mouse_control()
        if not self.check_collisions(dx, dy):
            self.x += dx
            self.y += dy