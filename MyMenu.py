import pygame
import MyPlay

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "EASY"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -50)
            self.game.draw_text("EASY", 30, self.startx, self.starty)
            self.game.draw_text("NOMAL", 30, self.optionsx, self.optionsy)
            self.game.draw_text("HARD", 30, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'EASY':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'NOMAL'
            elif self.state == 'NOMAL':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'HARD'
            elif self.state == 'HARD':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'EASY'
        elif self.game.UP_KEY:
            if self.state == 'EASY':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'HARD'
            elif self.state == 'NOMAL':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'EASY'
            elif self.state == 'HARD':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'NOMAL'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'EASY':
                self.game.playing = True
                MyPlay.Play(3000)
            elif self.state == 'NOMAL':
                self.game.playing = True
                MyPlay.Play(7000)
            elif self.state == 'HARD':
                self.game.playing = True
                MyPlay.Play(15000)
            self.run_display = False


