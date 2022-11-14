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
# Load Spaceship
YELLOW_SPACESHIP_IMG = pg.image.load(os.path.join('pygame/space-game/Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pg.transform.rotate(pg.transform.scale(YELLOW_SPACESHIP_IMG, (SHIP_HEIGHT, SHIP_WIDTH)),180)
# Load Lasers
RED_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_red.png'))
BLUE_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_blue.png'))
GREEN_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_green.png'))
YELLOW_LASER = pg.image.load(os.path.join('pygame/space-game/Assets','pixel_laser_yellow.png'))

class Ship:
    def __init__(self, x, y, health=100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []

    def draw_ship(self, screen):
        pg.draw.rect(screen, (255,250,0), (self.x,self.y,50,50))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = YELLOW_SPACESHIP
        self.laser_image = YELLOW_LASER
        self.mask = pg.mask.from_surface(self.ship_image)
        self.max_health = health
    

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.level = 1
        self.lives = 5
        self.main_font = pg.font.SysFont("comicsans", 28, True)
        self.player_velocity = 5


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        key_pressed = pg.key.get_pressed()
        self.moveShip(self,key_pressed)

    player = Player(350,700)

    def redraw_window(self):
        self.screen.blit(BG, (0,0))
        self.print_caption()
        self.player.draw_ship(self.screen)
        pg.display.update()

    def print_caption(self):
        self.level_label = self.main_font.render(f"Level:  {self.level}", True,  "green")
        self.lives_label = self.main_font.render(f"Lives:  {self.lives}", True,  "red")
        self.screen.blit(self.level_label, (20, 20))
        self.screen.blit(self.lives_label, (WIDTH - self.lives_label.get_width() - 20, 20))

    def moveShip(self, key_press, player):
        key_press = pg.key.get_pressed()
        if key_press[pg.K_LEFT] and self.player.x - self.player_velocity > 0:
            self.player.x -= self.player_velocity
        if key_press[pg.K_RIGHT] and self.player.x + self.player_velocity + 50 < WIDTH:
            self.player.x += self.player_velocity
        if key_press[pg.K_UP] and self.player.y - self.player_velocity > 0:
            self.player.y -= self.player_velocity
        if key_press[pg.K_DOWN] and self.player.y + self.player_velocity + 50 < HEIGHT:
            self.player.y += self.player_velocity

    def run(self):
        while True:
            self.redraw_window()
            self.print_caption()
            self.player.draw_ship(self.screen)
            self.check_events()
            self.clock.tick(FPS)

            


if __name__ == "__main__":
    game = Game()
    game.run()
