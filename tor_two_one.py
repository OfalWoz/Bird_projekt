import  pygame
from pygame.math import Vector2
class Tor_two_one(object):

    def __init__(self, game):
        self.clock = pygame.time.Clock()
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.font = pygame.font.Font(None, 32)

        self.last_minutes = 0
        self.last_seconds = 0
        self.last_milliseconds = 0

        self.best_minutes = 10000
        self.best_seconds = 10000
        self.best_milliseconds = 10000

        self.check = 0
        self.lap = 0

        self.done = False
        self.start_time = pygame.time.get_ticks()

        self.tor_bok = pygame.image.load('tor_bok.png')
        self.tor = pygame.image.load('tor_two.png')
        self.play = pygame.image.load('bolid_red_left.png')
        self.game = game

        size = self.game.screen.get_size()
        self.hight = 695
        self.widht = 1255

        self.p_pos = Vector2(550, 500)
        self.p_v = Vector2(0, 0)
        self.p_a = Vector2(0, 0)

    def tick(self):
        #stoper
        if self.milliseconds > 1000:
            self.seconds += 1
            self.milliseconds -= 1000
        if self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60
        self.milliseconds += self.clock.tick_busy_loop(60)

        #ograniczenie pola
        if self.p_pos.x >= 943:
            self.p_pos.x = 942

        if self.p_pos.x <= 387:
            self.p_pos.x = 388

        if self.p_pos.y >= 651:
            self.p_pos.y = 651

        if self.p_pos.y <= 194:
            self.p_pos.y = 195

        if self.p_v == Vector2(0, 10):
            self.p_v = Vector2(0, 9.9)
        else:
            self.p_v += self.p_a
        self.p_pos += self.p_v
        self.p_a *= 0.1
        self.p_v *= 0.5

        # ruch gracza
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
            self.p_a += Vector2(0, 0.05)
            self.p_a += Vector2(0.05, 0)
            self.play = pygame.image.load('bolid_red_down_right.png')
        if pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
            self.p_a += Vector2(-0.05, 0)
            self.p_a += Vector2(0, 0.05)
            self.play = pygame.image.load('bolid_red_down_left.png')
        if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
            self.p_a += Vector2(0,-0.05)
            self.p_a += Vector2(0.05, 0)
            self.play = pygame.image.load('bolid_red_up_right.png')
        if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
            self.p_a += Vector2(0,-0.5)
            self.p_a += Vector2(0, 0.5)
            self.play = pygame.image.load('bolid_red_up_left.png')

        #przeszkody
        self.grass_1 = pygame.Rect(526, 160, 90, 100)
        self.grass_2 = pygame.Rect(550, 260, 50, 40)
        self.grass_3 = pygame.Rect(830, 194, 200, 161)
        self.grass_4 = pygame.Rect(870, 358, 200, 30)
        self.grass_5 = pygame.Rect(924, 384, 200, 500)
        self.grass_6 = pygame.Rect(387, 517, 364, 500)
        self.grass_7 = pygame.Rect(387, 194, 11, 1000)
        self.grass_8 = pygame.Rect(484, 325, 270, 167)
        self.grass_9 = pygame.Rect(422, 264, 80, 200)
        self.grass_10 = pygame.Rect(784, 362, 20, 70)
        self.grass_11 = pygame.Rect(640, 251, 162, 140)
        self.grass_12 = pygame.Rect(823, 422, 63, 170)
        self.grass_13 = pygame.Rect(746, 555, 53, 96)

        #kolizje
        if self.grass_1.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_2.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_3.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_4.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_5.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_6.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_7.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_8.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_9.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_10.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_11.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_12.collidepoint((self.p_pos.x, self.p_pos.y)) or self.grass_13.collidepoint((self.p_pos.x, self.p_pos.y)):
            self.p_a *= 0.1

        #mierzenie czasu i punkty
        self.stop = pygame.Rect(518, 490, 1, 150)
        self.check_1 = pygame.Rect(454, 197, 1, 50)
        self.check_2 = pygame.Rect(616, 277, 50, 1)
        self.check_3 = pygame.Rect(724, 194, 1, 50)
        self.check_4 = pygame.Rect(850, 387, 1, 50)
        self.check_5 = pygame.Rect(873, 621, 1, 50)

        #checkpoints
        if self.check_1.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check < 1:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_2.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check == 1:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_3.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check == 2:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_4.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check == 3:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        if self.check_5.collidepoint((self.p_pos.x, self.p_pos.y)) and self.check == 4:
            self.check += 1
            print(self.check)
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()

        #linia mety
        if self.check >= 5 and self.stop.collidepoint((self.p_pos.x, self.p_pos.y)):
            pygame.mixer.music.load('UI_Quirky1.mp3')
            pygame.mixer.music.play()
            self.last_minutes = self.minutes
            self.last_seconds = self.seconds
            self.last_milliseconds = self.milliseconds
            self.last_time = (self.last_minutes * 1000000) + (self.last_seconds * 1000) + self.last_milliseconds
            self.best_time = (self.best_minutes * 1000000) + (self.best_seconds * 1000) + self.best_milliseconds
            if self.best_time >= self.last_time:
                self.best_minutes = self.last_minutes
                self.best_seconds = self.last_seconds
                self.best_milliseconds = self.last_milliseconds
            self.minutes = 0
            self.seconds = 0
            self.milliseconds = 0
            self.check = 0
            self.lap += 1

    def draw(self):
        self.timelabel = self.font.render("{}:{}:{}".format(self.minutes, self.seconds, self.milliseconds), 1,(0, 0, 0))
        self.last_timelabel = self.font.render("{}:{}:{}".format(self.last_minutes, self.last_seconds, self.last_milliseconds), 1, (0, 0, 0))
        self.best_timelabel = self.font.render("{}:{}:{}".format(self.best_minutes, self.best_seconds, self.best_milliseconds), 1, (0, 0, 0))

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, (0,0,0))
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)
        self.game.screen.blit(self.tor_bok, (-400, 250))
        self.game.screen.blit(self.tor_bok, (self.game.szerokosc/2 + 350, 0))
        self.game.screen.blit(self.tor, (self.game.szerokosc/2 - 350, 0)) #wyswietlanie toru
        self.game.screen.blit(self.play, (self.p_pos.x, self.p_pos.y)) #pozycja gracza
        draw_text('Aktualny czas:', self.font, (255, 255, 255), self.game.screen, 10, 50)
        self.game.screen.blit(self.timelabel, (180, 50)) #aktualny czas
        draw_text('Czas ostatniego okrążenia:', self.font, (255, 255, 255), self.game.screen, 10, 100)
        draw_text('Najlepszy czas:', self.font, (255, 255, 255), self.game.screen, 10, 150)
        draw_text('Okrążenie: '+str(self.lap), self.font, (255, 255, 255), self.game.screen, 10, 200)
        draw_text('Punkty kontrolne: '+str(self.check)+'/5', self.font, (255, 255, 255), self.game.screen, 10, 250)
        if self.lap >= 1: #wyswietlanie czasow po jednym okrazeniu
            self.game.screen.blit(self.last_timelabel, (310, 100))
            self.game.screen.blit(self.best_timelabel, (180, 150))

        if pygame.key.get_pressed()[pygame.K_m]:
            mx, my = pygame.mouse.get_pos()  # pozycja myszki
            print('x-', mx)
            print('y-', my)
        if pygame.key.get_pressed()[pygame.K_p]:
            mx, my = pygame.mouse.get_pos()  # pozycja myszki
            print('x-', self.p_pos.x)
            print('y-', self.p_pos.y)