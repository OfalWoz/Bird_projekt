import pygame
import sys

class Win_red(object):

    def __init__(self):
        click = False
        # konfiguracja
        self.FPS = 60
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        font = pygame.font.Font(None, 32)

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    Menu()

            self.delta += self.fpsClock.tick() / 1000.0
            while self.delta > 1 / self.FPS:  # Ograniczenie FPS
                self.delta -= 1 / self.FPS

            self.screen.fill((0, 0, 0))
            mx, my = pygame.mouse.get_pos()  # pozycja myszki

            if pygame.key.get_pressed()[pygame.K_m]:
                print('x-', mx)
                print('y-', my)
            # przyciski
            button_3 = pygame.Rect(514, 648, 135, 35)
            if button_3.collidepoint((mx, my)):
                if click:
                    Menu()

            self.screen.blit(pygame.image.load('wygranko_red.png'), ((self.szerokosc / 2) - 350, 0))
            self.screen.blit(pygame.image.load('menu_lewo.png'), ((self.szerokosc / 2) + 369, 0))
            self.screen.blit(pygame.image.load('menu_prawo.png'), (-430, 0))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.flip()


class Win_blue(object):

    def __init__(self):
        click = False
        # konfiguracja
        self.FPS = 60
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        font = pygame.font.Font(None, 32)

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    Menu()

            self.delta += self.fpsClock.tick() / 1000.0
            while self.delta > 1 / self.FPS:  # Ograniczenie FPS
                self.delta -= 1 / self.FPS

            self.screen.fill((0, 0, 0))
            mx, my = pygame.mouse.get_pos()  # pozycja myszki

            if pygame.key.get_pressed()[pygame.K_m]:
                print('x-', mx)
                print('y-', my)
            # przyciski
            button_3 = pygame.Rect(514, 648, 135, 35)
            if button_3.collidepoint((mx, my)):
                if click:
                    Menu()

            self.screen.blit(pygame.image.load('wygranko_blue.png'), ((self.szerokosc / 2) - 350, 0))
            self.screen.blit(pygame.image.load('menu_lewo.png'), ((self.szerokosc / 2) + 369, 0))
            self.screen.blit(pygame.image.load('menu_prawo.png'), (-430, 0))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.flip()