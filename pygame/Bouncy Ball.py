import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 50
ACCELERATION = .5


class Ball():
    def __init__(self):
        self.y = 200
        self.velocity = 8

    def draw(self):
        pygame.draw.circle(display, (0, 255, 0), (400, int(self.y)), 20)

    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 380:
            self.velocity = -self.velocity


def draw_window():
    display.fill((255, 255, 200))


def game():
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ball.move()
        draw_window()
        pygame.draw.line(display, (0, 0, 0), (0, 400), (800, 400), 10)
        ball.draw()
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()