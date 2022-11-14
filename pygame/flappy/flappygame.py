import pygame as pg

HEIGHT = 600
WIDTH = 600
FPS = 60
BG = "darkslategrey"
PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50

class Ship:
    def __init__(self, x, y, helth=100):
        self.x = x
        self.y = y

    def run(self):
        self.draw_sprite()

    def draw_sprite(self):
        pg.draw.rect(self.screen,(255,255,255),pg.Rect(300,500,PLAYER_HEIGHT,PLAYER_WIDTH))


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.ship = Ship(self, self.screen)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
            key_pressed = pg.key.get_pressed()
            self.moveShooter(key_pressed)

    def moveShooter(self, key_press, ship):
        key_press = pg.key.get_pressed()
        if key_press[pg.K_LEFT]:
            ship.x -= 2
        if key_press[pg.K_RIGHT]:
            ship.x += 2
        if key_press[pg.K_UP]:
            ship.y -= 2
        if key_press[pg.K_DOWN]:
            ship.y += 2


    def draw_window(self):
        self.screen.fill(BG)

        
    def run(self):    
        while True:
            self.draw_window()
            self.ship.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    newGame = Game()
    newGame.run()
