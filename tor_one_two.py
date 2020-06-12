import pygame
import sys
from pygame.math import Vector2

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
                    import run
                    run.Menu()

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
                    import run
                    run.Menu()

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

class Tor_one_two(object):

    def __init__(self, game):
        self.font = pygame.font.Font(None, 32)

        self.check = 0
        self.lap = 0
        self.check2 = 0
        self.lap2 = 0

        self.done = False
        self.start_time = pygame.time.get_ticks()

        self.tor_bok = pygame.image.load('tor_bok.png')
        self.tor = pygame.image.load('tor_one.png')
        self.play = pygame.image.load('bolid_red_left.png')
        self.play2 = pygame.image.load('bolid_blue_left.png')
        self.game = game

        size = self.game.screen.get_size()
        self.hight = 695
        self.widht = 1255

        self.p_pos = Vector2(514, 497)
        self.p_v = Vector2(0, 0)
        self.p_a = Vector2(0, 0)

        self.p2_pos = Vector2(514, 512)
        self.p2_v = Vector2(0, 0)
        self.p2_a = Vector2(0, 0)

        #przeszkody
        self.grass_1 = pygame.Rect(528, 160, 500, 100)
        self.grass_2 = pygame.Rect(578, 260, 500, 40)
        self.grass_3 = pygame.Rect(830, 310, 200, 50)
        self.grass_4 = pygame.Rect(870, 358, 200, 30)
        self.grass_5 = pygame.Rect(924, 384, 200, 500)
        self.grass_6 = pygame.Rect(387, 517, 1000, 500)
        self.grass_7 = pygame.Rect(387, 194, 11, 1000)
        self.grass_8 = pygame.Rect(484, 325, 270, 167)
        self.grass_9 = pygame.Rect(422, 264, 80, 200)
        self.grass_10 = pygame.Rect(784, 362, 20, 70)

        #mierzenie czasu i punkty
        self.stop = pygame.Rect(518, 490, 1, 150)
        self.check_1 = pygame.Rect(450, 195, 1, 100)
        self.check_2 = pygame.Rect(850, 395, 1, 100)

    def tick(self):
        #ograniczenie pola
        if self.p_pos.x >= 943:
            self.p_pos.x = 942

        if self.p_pos.x <= 387:
            self.p_pos.x = 388

        if self.p_pos.y >= 536:
            self.p_pos.y = 535

        if self.p_pos.y <= 194:
            self.p_pos.y = 195

        if self.p_v == Vector2(0,10):
            self.p_v = Vector2(0,9.9)
        else:
            self.p_v += self.p_a
        self.p_pos += self.p_v
        self.p_a *= 0.1
        self.p_v *= 0.5

        if self.p2_pos.x >= 943:
            self.p2_pos.x = 942

        if self.p2_pos.x <= 387:
            self.p2_pos.x = 388

        if self.p2_pos.y >= 536:
            self.p2_pos.y = 535

        if self.p2_pos.y <= 194:
            self.p2_pos.y = 195

        if self.p2_v == Vector2(0,10):
            self.p2_v = Vector2(0,9.9)
        else:
            self.p2_v += self.p2_a
        self.p2_pos += self.p2_v
        self.p2_a *= 0.1
        self.p2_v *= 0.5

        # ruch gracza 1
        if pygame.key.get_pressed()[pygame.K_w]:
            self.p_a += Vector2(0,-0.5)
            self.play = pygame.image.load('bolid_red_up.png')
        if pygame.key.get_pressed()[pygame.K_d]:
            self.p_a += Vector2(0.5, 0)
            self.play = pygame.image.load('bolid_red_right.png')
        if pygame.key.get_pressed()[pygame.K_s]:
            self.p_a += Vector2(0,0.5)
            self.play = pygame.image.load('bolid_red_down.png')
        if pygame.key.get_pressed()[pygame.K_a]:
           self.p_a += Vector2(-0.5, 0)
           self.play = pygame.image.load('bolid_red_left.png')
        if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_s]:
            self.play = pygame.image.load('bolid_red_down_right.png')
        if pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
            self.play = pygame.image.load('bolid_red_down_left.png')
        if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
            self.play = pygame.image.load('bolid_red_up_right.png')
        if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
            self.play = pygame.image.load('bolid_red_up_left.png')

        # ruch gracza 2
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.p2_a += Vector2(0,-0.5)
            self.play2 = pygame.image.load('bolid_blue_up.png')
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.p2_a += Vector2(0.5, 0)
            self.play2 = pygame.image.load('bolid_blue_right.png')
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.p2_a += Vector2(0,0.5)
            self.play2 = pygame.image.load('bolid_blue_down.png')
        if pygame.key.get_pressed()[pygame.K_LEFT]:
           self.p2_a += Vector2(-0.5, 0)
           self.play2 = pygame.image.load('bolid_blue_left.png')
        if pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_DOWN]:
            self.play2 = pygame.image.load('bolid_blue_down_right.png')
        if pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_DOWN]:
            self.play2 = pygame.image.load('bolid_blue_down_left.png')
        if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.play2 = pygame.image.load('bolid_blue_up_right.png')
        if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_LEFT]:
            self.play2 = pygame.image.load('bolid_blue_up_left.png')

        if self.grass_1.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_2.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_3.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_4.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_5.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_6.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_7.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_8.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_9.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_10.collidepoint((self.p_pos.x, self.p_pos.y)):
            self.p_a *= 0.1

        if self.grass_1.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_2.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_3.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_4.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_5.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_6.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_7.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_8.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_9.collidepoint((self.p2_pos.x, self.p2_pos.y)) or self.grass_10.collidepoint((self.p2_pos.x, self.p2_pos.y)):
            self.p2_a *= 0.1

        #checkpoints
        if self.check_1.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check < 1:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_1.collidepoint((self.p2_pos.x, self.p2_pos.y)) and self.check2 < 1:
            self.check2 += 1
            print(self.check2)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_2.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check == 1:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_2.collidepoint((self.p2_pos.x, self.p2_pos.y)) and self.check2 == 1:
            self.check2 += 1
            print(self.check2)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        #linia mety
        if self.check >= 2 and self.stop.collidepoint((self.p_pos.x, self.p_pos.y)):
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()
            self.check = 0
            self.lap += 1

        if self.check2 >= 2 and self.stop.collidepoint((self.p2_pos.x, self.p2_pos.y)):
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()
            self.check2 = 0
            self.lap2 += 1

        if self.lap >= 4:
            pygame.mixer.music.load('win.mp3')
            pygame.mixer.music.play()
            Win_red()
        if self.lap2 >= 4:
            pygame.mixer.music.load('win.mp3')
            pygame.mixer.music.play()
            Win_blue()

    def draw(self):
        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, (0,0,0))
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        self.game.screen.blit(self.tor_bok, (-400, 100))
        self.game.screen.blit(self.tor_bok, (self.game.szerokosc/2 + 350, 120))
        self.game.screen.blit(self.tor, (self.game.szerokosc/2 - 350, 0)) #wyswietlanie toru
        self.game.screen.blit(self.play, (self.p_pos.x, self.p_pos.y))
        self.game.screen.blit(self.play2, (self.p2_pos.x, self.p2_pos.y))#pozycja gracza
        draw_text('Okrążenie RED: '+str(self.lap)+'/3', self.font, (255, 255, 255), self.game.screen, 10, 20)
        draw_text('Okrążenie BLUE: ' + str(self.lap2)+'/3', self.font, (255, 255, 255), self.game.screen, self.game.szerokosc/2 + 345, 20)
        draw_text('Punkty kontrolne RED: '+str(self.check)+'/2', self.font, (255, 255, 255), self.game.screen, 10, 80)
        draw_text('Punkty kontrolne BLUE: ' + str(self.check2) + '/2', self.font, (255, 255, 255), self.game.screen, self.game.szerokosc/2 + 345, 80)

        if pygame.key.get_pressed()[pygame.K_m]:
            mx, my = pygame.mouse.get_pos()  # pozycja myszki
            print('x-', mx)
            print('y-', my)
        if pygame.key.get_pressed()[pygame.K_p]:  # pozycja gracza
            print('x-', self.p_pos.x)
            print('y-', self.p_pos.y)