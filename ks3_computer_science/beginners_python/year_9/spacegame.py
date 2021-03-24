import pygame

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = ((255,255,255))
FPS = 60

def drawWindow():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False

        drawWindow()

    pygame.QUIT()



