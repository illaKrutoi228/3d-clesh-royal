import pygame as pg
from nastrfoiki import *
import math
from wotld_clash import world_map

class Sprite:
    def __init__(self, game, x, y, scale, image):
        self.x = x * TILE
        self.y = y * TILE
        self.scale = scale
        self.image = image
        self.w = image.get_width()
        self.h = image.get_height()
        self.sc = game.screen
    def render(self, player, objects):
        dx = self.x - player.x
        dy = self.y - player.y
        theta = math.atan2(dy, dx)
        delta = theta - player.angle
        if dx > 0 and player.angle > math.pi:
            delta += math.tau
        delta_rays = delta / DELTA_ANGLE
        x = (NUM_OF_RAYS / 2 + delta_rays) * SCALE
        dist = math.hypot(dx, dy)
        norm_dist = dist * math.cos(delta)
        if -self.w / 2 < x < (WIDTH - self.w / 2) and norm_dist > 0.5:
            proj = SCREEN_DITH / norm_dist * self.scale
            proj_width = proj * (self.w / self.h)
            proj_height = proj
            y = HALF_HEIGHT - max(proj_height, 0.0001) / 2 + 0.0
            # pg.draw.rect(self.sc, self.colour, (x, y, proj_width, proj_height))
            img = pg.transform.scale(self.image, (proj_width, proj_height))
            # self.sc.blit(img, (x, y))
            objects.append((dist, (x, y+player.height*proj_height), img))
class MiniPekka(Sprite):
    def __init__(self, game, x , y, scale):
        super().__init__(game, x , y, scale, game.sprites["minipeka"])
    def check_collisions(self, dx, dy):
        if (self.x+dx//TILE, self.y+dy//TILE):
            return True
        return False
    def update(self, player):
        h = True
        for x, y in world_map:
            rect = pg.Rect(x, y, TILE, TILE)
            if rect.clipline((self.x, self.y, player.x, player.y)):
                h = False
                break
        dx = self.x - player.x
        dy = self.y - player.y
        dist = math.hypot(dx, dy)
        if dist > 50:
            dx, dy = 0, 0
            if self.x > player.x:
                dx = -2
            if self.y > player.y:
                dy = -2
            if self.x < player.x:
                dx = 2
            if self.y < player.y:
                dy = 2
            #if not self.check_collisions(dx, dy):
            self.x += dx
            self.y += dy