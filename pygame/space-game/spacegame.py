import pygame as pg
import sys
import os
import time
pg.font.init()

WIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = ((255,255,255))
SHIP_HEIGHT, SHIP_WIDTH = 55, 40
BG = pg.image.load(os.path.join('pygame/space-game/Assets','space.png'))

class SpaceGame:
    def __init__(self, game) -> None:
        self.spacegame = game
        self.import_assets()
        self.level = 1
        self.lives = 5
        self.main_font = pg.font.SysFont("comicsans", 28, True)

    def import_assets(self):
        # Load Spaceship
        self.YELLOW_SPACESHIP_IMG = pg.image.load(os.path.join('pygame/space-game/Assets','spaceship_yellow.png'))
        self.YELLOW_SPACESHIP = pg.transform.rotate(pg.transform.scale(self.YELLOW_SPACESHIP_IMG, (SHIP_HEIGHT, SHIP_WIDTH)),180)
        # Load Lasers
        self.RED_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_red.png'))
        self.BLUE_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_blue.png'))
        self.GREEN_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_green.png'))
        self.YELLOW_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_yellow.png'))
        #self.RED_SPACESHIP_IMG = pg.image.load(os.path.join('pygame/space-game/Assets','spaceship_red.png'))
        #self.RED_SPACESHIP = pg.transform.rotate(pg.transform.scale(self.RED_SPACESHIP_IMG, (SHIP_HEIGHT, SHIP_WIDTH)), 90)

    def draw_ships(self):
        self.spacegame.screen.blit(self.YELLOW_SPACESHIP, (self.yellow.x,self.yellow.y))

    def print_caption(self):
        self.level_label = self.main_font.render(f"Level:  {self.level}", True, "black", "yellow")
        self.lives_label = self.main_font.render(f"Lives:  {self.lives}", True, "black", "yellow")
        self.spacegame.screen.blit(self.level_label, (20, 20))
        self.spacegame.screen.blit(self.lives_label, (WIDTH - self.lives_label.get_width() - 20, 20))


    
    def run(self):
        self.yellow = pg.Rect(350,700, SHIP_WIDTH, SHIP_HEIGHT)
        self.yellow.y += 1
        self.draw_ships()
        self.print_caption()
    
    

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.spacegame = SpaceGame(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    def run(self):
        while True:
            self.screen.blit(BG, (0,0))
            self.spacegame.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(FPS)
            


if __name__ == "__main__":
    game = Game()
    game.run()
