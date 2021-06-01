import pygame as pg
import pickle
import sys
from os import path
from settings import *

class NewUser:
    def __init__(self):
        self.dt = 0
        self.y_count = 0
        self.select = False
        self.x_count = 0
        self.mx, self.my = 0,0
        self.playing = True
        self.user_input = ''
        self.username = ''
        self.password1 = ''
        self.password2 = ''
        self.logged_in = False
        self.get_input = False
        self.input_type = ''
        self.final_status = ''
        pg.init()
        # self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen = pg.display.set_mode((300, 500))
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
        self.user_rect = pg.Rect(50, 160, 150, 30)
        self.pass_rect = pg.Rect(50, 240, 150, 30)
        self.pass_rect2 = pg.Rect(50, 320, 150, 30)
        self.login_rect = pg.Rect(80, 380, 100, 50)

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
                if self.get_input:
                    if event.key == pg.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    else:
                        self.user_input += event.unicode

    def quit(self):
        self.save_data()
        pg.quit()
        sys.exit()

    def check_login(self):
        # this will check the users input for username and password to see if any matches in file
        log_data = []
        try:
            with open('log.pkl', 'rb') as f:
                data = pickle.load(f)
                log_data.append(data)
            if self.username in log_data:
                print('test')


        except:
            # if no file then proceed with new user
            self.final_status = 'new user'
            self.playing = False

    def update(self):
        mouse_rect = pg.Rect(self.mx, self.my, 5, 5)

        if self.get_input:
            if self.input_type == 'username':
                self.username = self.user_input
            if self.input_type == 'password1':
                self.password1 = self.user_input
            if self.input_type == 'password2':
                self.password2 = self.user_input

        if not self.logged_in:
            if mouse_rect.colliderect(self.user_rect):
                if self.select:
                    self.user_input = ''
                    self.get_input = True
                    self.input_type = 'username'
            if mouse_rect.colliderect(self.pass_rect):
                if self.select:
                    self.user_input = ''
                    self.get_input = True
                    self.input_type = 'password1'
            if mouse_rect.colliderect(self.pass_rect2):
                if self.select:
                    self.user_input = ''
                    self.get_input = True
                    self.input_type = 'password2'
            if mouse_rect.colliderect(self.login_rect):
                if self.select:
                    if self.username != '':
                        if self.password != '':
                            self.check_login()

    def save_data(self):
        pass

    def display_login(self):
        back_ground = pg.Rect(0, 0, 300, 500)
        header = pg.Rect(0, 0, 300, 60)
        pg.draw.rect(self.screen, GREY, back_ground)
        pg.draw.rect(self.screen, BLACK, header)
        if self.input_type == "username":
            pg.draw.rect(self.screen, OFF_WHITE, self.user_rect)
        else:
            pg.draw.rect(self.screen, WHITE, self.user_rect)
        pg.draw.rect(self.screen, BLACK, self.user_rect, 2)
        if self.input_type == 'password1':
            pg.draw.rect(self.screen, OFF_WHITE, self.pass_rect)
        else:
            pg.draw.rect(self.screen, WHITE, self.pass_rect)
        if self.input_type == 'password2':
            pg.draw.rect(self.screen, OFF_WHITE, self.pass_rect2)
        else:
            pg.draw.rect(self.screen, WHITE, self.pass_rect2)
        pg.draw.rect(self.screen, BLACK, self.pass_rect, 2)
        pg.draw.rect(self.screen, BLACK, self.pass_rect2, 2)
        pg.draw.rect(self.screen, WHITE, self.login_rect)
        pg.draw.rect(self.screen, BLACK, self.login_rect, 2)
        self.draw_text('BotLer', self.basic_font, 50, WHITE, 70, 10)
        self.draw_text('---New User---', self.basic_font, 20, BLACK, 70, 65)
        self.draw_text('Username:', self.basic_font, 20, BLACK, 40, 120)
        if self.username != '':
            self.draw_text(self.username, self.basic_font, 20, BLACK, self.user_rect.x + 5, self.user_rect.y + 5)
        self.draw_text('Password:', self.basic_font, 20, BLACK, 40, 200)
        if self.password1 != '':
            privacy_screen = ''
            for count in range(len(self.password1)):
                privacy_screen += '*'
            self.draw_text(privacy_screen, self.basic_font, 20, BLACK, self.pass_rect.x + 5, self.pass_rect.y + 5)
        self.draw_text('Password:', self.basic_font, 20, BLACK, 40, 280)
        if self.password2 != '':
            privacy_screen2 = ''
            for count in range(len(self.password2)):
                privacy_screen2 += '*'
            self.draw_text(privacy_screen2, self.basic_font, 20, BLACK, self.pass_rect2.x + 5, self.pass_rect2.y + 5)
        self.draw_text('Login', self.basic_font, 25, BLACK, self.login_rect.x + 15,
                       self.login_rect.y + 12)

    def display_menu(self):
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

    def draw(self):
        self.screen.fill(WHITE)
        if not self.logged_in:
            self.display_login()
        else:
            self.display_menu()
        pg.display.flip()


class Login:
    def __init__(self):
        self.dt = 0
        self.y_count = 0
        self.select = False
        self.x_count = 0
        self.mx, self.my = 0,0
        self.playing = True
        self.user_input = ''
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.get_input = False
        self.input_type = ''
        self.final_status = ''
        pg.init()
        self.screen = pg.display.set_mode((300, 400))
        # self.screen = pg.display.set_mode((WIDTH, HEIGHT))
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
        self.user_rect = pg.Rect(50, 160, 150, 30)
        self.pass_rect = pg.Rect(50, 240, 150, 30)
        self.login_rect = pg.Rect(80, 300, 100, 50)

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
                if self.get_input:
                    if event.key == pg.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    else:
                        self.user_input += event.unicode

    def quit(self):
        self.save_data()
        pg.quit()
        # sys.exit()

    def check_login(self):
        # this will check the users input for username and password to see if any matches in file
        log_data = []
        try:
            with open('log.pkl', 'rb') as f:
                data = pickle.load(f)
                log_data.append(data)
            if self.username in log_data:
                print('test')


        except:
            # if no file then proceed with new user
            self.final_status = 1
            self.playing = False

    def update(self):
        mouse_rect = pg.Rect(self.mx, self.my, 5, 5)

        if self.get_input:
            if self.input_type == 'username':
                self.username = self.user_input
            if self.input_type == 'password':
                self.password = self.user_input

        if not self.logged_in:
            if mouse_rect.colliderect(self.user_rect):
                if self.select:
                    self.user_input = ''
                    self.get_input = True
                    # self.username = self.user_input
                    self.input_type = 'username'
            if mouse_rect.colliderect(self.pass_rect):
                if self.select:
                    self.user_input = ''
                    self.get_input = True
                    # self.password = self.user_input
                    self.input_type = 'password'
            if mouse_rect.colliderect(self.login_rect):
                if self.select:
                    if self.username != '':
                        if self.password != '':
                            self.check_login()
        # print(self.input_type)

    def save_data(self):
        pass

    def display_login(self):
        back_ground = pg.Rect(0, 0, 300, 500)
        header = pg.Rect(0, 0, 300, 60)
        pg.draw.rect(self.screen, GREY, back_ground)
        pg.draw.rect(self.screen, BLACK, header)
        if self.input_type == "username":
            pg.draw.rect(self.screen, OFF_WHITE, self.user_rect)
        else:
            pg.draw.rect(self.screen, WHITE, self.user_rect)
        pg.draw.rect(self.screen, BLACK, self.user_rect, 2)
        if self.input_type == 'password':
            pg.draw.rect(self.screen, OFF_WHITE, self.pass_rect)
        else:
            pg.draw.rect(self.screen, WHITE, self.pass_rect)
        pg.draw.rect(self.screen, BLACK, self.pass_rect, 2)
        pg.draw.rect(self.screen, WHITE, self.login_rect)
        pg.draw.rect(self.screen, BLACK, self.login_rect, 2)
        self.draw_text('BotLer', self.basic_font, 50, WHITE, 70, 10)
        self.draw_text('Please Log in:', self.basic_font, 20, BLACK, 70, 65)
        self.draw_text('Username:', self.basic_font, 20, BLACK, 40, 120)
        if self.username != '':
            self.draw_text(self.username, self.basic_font, 20, BLACK, self.user_rect.x + 5, self.user_rect.y + 5)
        self.draw_text('Password:', self.basic_font, 20, BLACK, 40, 200)
        if self.password != '':
            privacy_screen = ''
            for count in range(len(self.password)):
                privacy_screen += '*'
            self.draw_text(privacy_screen, self.basic_font, 20, BLACK, self.pass_rect.x + 5, self.pass_rect.y + 5)
        self.draw_text('Login', self.basic_font, 25, BLACK, self.login_rect.x + 15,
                       self.login_rect.y + 12)

    def display_menu(self):
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

    def draw(self):
        self.screen.fill(WHITE)
        if not self.logged_in:
            self.display_login()
        else:
            self.display_menu()
        pg.display.flip()

app = Login()
app.run()
print(app.final_status)
if app.final_status == 1:
    print('test')
    user = NewUser()
    # app.quit()
    user.run()