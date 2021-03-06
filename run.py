import pygame
import sys
from player import Player
from tor_two_one import Tor_two_one
from tor_one_two import Tor_one_two
from tor_two_two import  Tor_two_two
from pygame import mixer

class Two_two(object):

    def __init__(self):
        #konfiguracja
        self.FPS = 60
        click = False
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        self.player = Tor_two_two(self)

        # trzymanie okna
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    Menu()

            self.delta += self.fpsClock.tick() / 1000.0
            while self.delta > 1 / self.FPS:  # Ograniczenie FPS
                self.tick()
                self.delta -= 1 / self.FPS

            self.screen.fill((53, 107, 57))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

class One_two(object):

    def __init__(self):
        #konfiguracja
        self.FPS = 60
        click = False
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        self.player = Tor_one_two(self)

        # trzymanie okna
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    Menu()

            self.delta += self.fpsClock.tick() / 1000.0
            while self.delta > 1 / self.FPS:  # Ograniczenie FPS
                self.tick()
                self.delta -= 1 / self.FPS

            self.screen.fill((53, 107, 57))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

class Tor_one(object):

    def __init__(self):
        #konfiguracja
        self.FPS = 60
        click = False
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        self.player = Player(self)

        # trzymanie okna
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    Menu()

            self.delta += self.fpsClock.tick() / 1000.0
            while self.delta > 1 / self.FPS:  # Ograniczenie FPS
                self.tick()
                self.delta -= 1 / self.FPS

            self.screen.fill((53, 107, 57))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

class Tor_two(object):

    def __init__(self):
        #konfiguracja
        self.FPS = 60
        click = False
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        self.player = Tor_two_one(self)

        # trzymanie okna
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    Menu()

            self.delta += self.fpsClock.tick() / 1000.0
            while self.delta > 1 / self.FPS:  # Ograniczenie FPS
                self.tick()
                self.delta -= 1 / self.FPS

            self.screen.fill((53, 107, 57))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

class Select(object):

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
            mx, my = pygame.mouse.get_pos()#pozycja myszki

            if pygame.key.get_pressed()[pygame.K_m]:
                print('x-', mx)
                print('y-',my)
            #przyciski
            button_1 = pygame.Rect(352, 131, 135, 135)
            button_2 = pygame.Rect(352, 370, 135, 135)
            button_4 = pygame.Rect(777, 132, 135, 135)
            button_5 = pygame.Rect(777, 369, 135, 135)
            button_3 = pygame.Rect(514, 648, 135, 35)
            if button_1.collidepoint((mx, my)):
                if click:
                    pygame.mixer.music.load('carstartgarage.mp3')
                    pygame.mixer.music.play()
                    Tor_one()
            if button_2.collidepoint((mx, my)):
                if click:
                    pygame.mixer.music.load('carstartgarage.mp3')
                    pygame.mixer.music.play()
                    Tor_two()
            if button_4.collidepoint((mx, my)):
                if click:
                    pygame.mixer.music.load('carstartgarage.mp3')
                    pygame.mixer.music.play()
                    One_two()
            if button_5.collidepoint((mx, my)):
                if click:
                    pygame.mixer.music.load('carstartgarage.mp3')
                    pygame.mixer.music.play()
                    Two_two()
            if button_3.collidepoint((mx, my)):
                if click:
                    Menu()

            self.screen.blit(pygame.image.load('select.png'), ((self.szerokosc / 2) - 350, 0))
            self.screen.blit(pygame.image.load('menu_lewo.png'), ((self.szerokosc / 2) + 369,0))
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

class Menu(object):

    def __init__(self):
        click = False
        # konfiguracja
        self.FPS = 60
        pygame.init()
        self.szerokosc = 1280
        self.wysokosc = 720
        self.screen = pygame.display.set_mode((self.szerokosc, self.wysokosc))  # rodzielczosc, bedzie sie pozniej dostosowywac do monitora
        self.fpsClock = pygame.time.Clock()
        self.delta = 0.0
        font = pygame.font.Font(None, 32)

        pygame.mixer.music.load('Game-Menu_Looping.mp3')
        pygame.mixer.music.play(-1)

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
            mx, my = pygame.mouse.get_pos()#pozycja myszki

            if pygame.key.get_pressed()[pygame.K_m]:
                print('x-', mx)
                print('y-',my)
            #przyciski
            button_1 = pygame.Rect(308, 80, 135, 35)
            button_2 = pygame.Rect(308, 127, 135, 35)
            if button_1.collidepoint((mx, my)):
                if click:
                    Select()
            if button_2.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(pygame.image.load('bird_menu.png'), ((self.szerokosc / 2) - 350, 0))
            self.screen.blit(pygame.image.load('menu_lewo.png'), ((self.szerokosc / 2) + 369,0))
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
Menu()