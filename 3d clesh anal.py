import pygame as pg

from nastrfoiki import player_speed
from player import Player
from raycasting import ray_casting
import nastrfoiki
from wotld_clash import world_map
import sprite


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((nastrfoiki.WIDTH, nastrfoiki.HEIGHT))
        pg.display.set_caption("Clash Roayle: MegaKnight")
        self.clock = pg.time.Clock()
        pg.mouse.set_visible(False)
        self.player = Player(self)
        self.Texc = {"1":pg.image.load("Texc/5stena.jpg").convert_alpha()}
        self.sprites = {"minipeka":pg.image.load("sprites/mini_peka.png").convert_alpha()}

        self.sprite_objects = [
            sprite.Sprite(self, 5.5, 5.5, 50, self.sprites["minipeka"])
        ]

        self.enemys = [
            sprite.MiniPekka(self, 1.5, 1.5, 50)
        ]

    def draw_objects(self, objects):
        for obj in objects:
            self.screen.blit(obj[2],obj[1])
    def sort(self,objects):
        arr = objects
        for x in range(len(objects)-1):
            for i in range(len(objects)-1):
                if arr[i][0] < arr[i+1][0] and arr[2].get_width() < 200:
                    temp = objects[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = temp
        return arr
    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.screen.fill((0, 0, 0))
            self.player.movement()
            #for tile in world_map:
                 #rect = (tile[0]*nastrfoiki.TILE, tile[1]*nastrfoiki.TILE, nastrfoiki.TILE, nastrfoiki.TILE)
                 #pg.draw.rect(self.screen, (255, 255, 255), rect)
            #pg.draw.circle(self.screen, (255,0,0), self.player.pos, 5)
            objects = ray_casting(self.screen, self.player, self.Texc)
            for sprt in self.sprite_objects:
                sprt.render(self.player, objects)
            for enemy in self.enemys:
                enemy.render(self.player, objects)
                enemy.update(self.player)
            #objects = self.sort(objects)
            self.draw_objects(objects)
            pg.display.update()
            self.clock.tick(nastrfoiki.FPS)
if __name__ == "__main__":
    app = Game()
    app.run()