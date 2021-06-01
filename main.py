import pygame as pg
import pickle
import sys
from os import path
from settings import *

class Login:
    def __init__(self):
        self.dt = 0
        self.playing = True
        pg.init()
        self.screen = pg.display.set_mode((300, 400))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.username = ''
        self.password = ''
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.basic_font = path.join(img_folder, 'BASIC.TTF')
        self.user_rect = pg.Rect(275, 355, 150, 30)
        self.pass_rect = pg.Rect(275, 405, 150, 30)
        self.run()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.playing:
            self.select = False
            self.mx, self.my = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.select = True



class Application:
    def __init__(self):
        self.dt = 0
        self.y_count = 0
        self.select = False
        self.x_count = 0
        self.mx, self.my = 0,0
        self.playing = True
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.basic_font = path.join(img_folder, 'BASIC.TTF')
        self.user_rect = pg.Rect(275, 355, 150, 30)
        self.pass_rect = pg.Rect(275, 405, 150, 30)

    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def events(self):
        self.select = False
        self.mx, self.my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.select = True
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def quit(self):
        self.save_data()
        pg.quit()
        sys.exit()

    def update(self):
        mouse_rect = pg.Rect(self.mx, self.my, 5,5)
        if mouse_rect.colliderect(self.user_rect):
            if self.select:
                username = input()
                print(username)

    def save_data(self):
        pass

    def draw(self):
        self.screen.fill(WHITE)
        back_ground = pg.Rect(0, 0, WIDTH, HEIGHT)

        header = pg.Rect(0, 20, WIDTH, 175)
        pg.draw.rect(self.screen, GREY, back_ground)
        pg.draw.rect(self.screen, BLACK, header)
        pg.draw.rect(self.screen, WHITE, self.user_rect)
        pg.draw.rect(self.screen, WHITE, self.pass_rect)
        self.draw_text('BotLer', self.basic_font, 100, WHITE, 200, 75)
        self.draw_text('Please Log in:', self.basic_font, 50, BLACK, 100, 250)
        self.draw_text('Username:', self.basic_font, 30, BLACK, 100, 350)
        self.draw_text('Password:', self.basic_font, 30, BLACK, 100, 400)

        pg.display.flip()

app = Application()
app.run()