import pygame
import MyPlay

EASYMODE = 3000
NORMALMODE = 7000
HARDMODE = 20000
GHOSTMODE = 15000

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.win = 0

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
        self.easyx, self.easyy = self.mid_w, self.mid_h + 30
        self.normalx, self.normaly = self.mid_w, self.mid_h + 60
        self.hardx, self.hardy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.easyx - 120, self.easyy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('ALPHA PONG', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -50)
            self.game.draw_text("EASY", 30, self.easyx, self.easyy)
            self.game.draw_text("NORMAL", 30, self.normalx, self.normaly)
            self.game.draw_text("HARD", 30, self.hardx, self.hardy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'EASY':
                self.cursor_rect.midtop = (self.normalx - 120, self.normaly)
                self.state = 'NORMAL'
            elif self.state == 'NORMAL':
                self.cursor_rect.midtop = (self.hardx - 120, self.hardy)
                self.state = 'HARD'
            elif self.state == 'HARD':
                self.cursor_rect.midtop = (self.easyx - 120, self.easyy)
                self.state = 'EASY'
        elif self.game.UP_KEY:
            if self.state == 'EASY':
                self.cursor_rect.midtop = (self.hardx - 120, self.hardy)
                self.state = 'HARD'
            elif self.state == 'NORMAL':
                self.cursor_rect.midtop = (self.easyx - 120, self.easyy)
                self.state = 'EASY'
            elif self.state == 'HARD':
                self.cursor_rect.midtop = (self.normalx - 120, self.normaly)
                self.state = 'NORMAL'

    def check_input(self):
        self.move_cursor()
        if self.game.GHOST:
            self.game.reset_keys()
            pygame.event.clear()
            MainMenuG(self.game).display_menu()
            self.run_display = False
        elif self.game.START_KEY:
            self.run_display = False
            if self.state == 'EASY':
                self.win = MyPlay.Play(EASYMODE, False)
            elif self.state == 'NORMAL':
                self.win = MyPlay.Play(NORMALMODE, False)
            elif self.state == 'HARD':
                self.win = MyPlay.Play(HARDMODE, False)
            self.game.reset_keys()
            pygame.event.clear()
            if self.win:
                if(self.state == 'HARD'):
                    WinMenu(self.game, self.state).display_menu_hard()
                else:
                    WinMenu(self.game, self.state).display_menu()
            else:
                LoseMenu(self.game, self.state).display_menu()

class MainMenuG(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "EASY"
        self.easyx, self.easyy = self.mid_w, self.mid_h + 30
        self.normalx, self.normaly = self.mid_w, self.mid_h + 60
        self.hardx, self.hardy = self.mid_w, self.mid_h + 90
        self.ghostx, self.ghosty = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.easyx - 120, self.easyy)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('ALPHA PONG', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -50)
            self.game.draw_text("EASY", 30, self.easyx, self.easyy)
            self.game.draw_text("NORMAL", 30, self.normalx, self.normaly)
            self.game.draw_text("HARD", 30, self.hardx, self.hardy)
            self.game.draw_text("GHOST", 30, self.ghostx, self.ghosty)
            self.draw_cursor()
            self.blit_screen()
            
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'EASY':
                self.cursor_rect.midtop = (self.normalx - 120, self.normaly)
                self.state = 'NORMAL'
            elif self.state == 'NORMAL':
                self.cursor_rect.midtop = (self.hardx - 120, self.hardy)
                self.state = 'HARD'
            elif self.state == 'HARD':
                self.cursor_rect.midtop = (self.ghostx - 120, self.ghosty)
                self.state = 'GHOST'
            elif self.state == 'GHOST':
                self.cursor_rect.midtop = (self.easyx - 120, self.easyy)
                self.state = 'EASY'
        elif self.game.UP_KEY:
            if self.state == 'EASY':
                self.cursor_rect.midtop = (self.ghostx - 120, self.ghosty)
                self.state = 'GHOST'
            elif self.state == 'GHOST':
                self.cursor_rect.midtop = (self.hardx - 120, self.hardy)
                self.state = 'HARD'
            elif self.state == 'HARD':
                self.cursor_rect.midtop = (self.normalx - 120, self.normaly)
                self.state = 'NORMAL'
            elif self.state == 'NORMAL':
                self.cursor_rect.midtop = (self.easyx - 120, self.easyy)
                self.state = 'EASY'
                
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            self.run_display = False
            self.game.reset_keys()
            pygame.event.clear()
            if self.state == 'EASY':
                self.win = MyPlay.Play(EASYMODE, False)
                if self.win:
                    WinMenu(self.game, self.state).display_menu()
                else:
                    LoseMenu(self.game, self.state).display_menu()
            elif self.state == 'NORMAL':
                self.win = MyPlay.Play(NORMALMODE, False)
                if self.win:
                    WinMenu(self.game, self.state).display_menu()
                else:
                    LoseMenu(self.game, self.state).display_menu()
            elif self.state == 'HARD':
                self.win = MyPlay.Play(HARDMODE, False)
                if self.win:
                    WinMenu(self.game, self.state).display_menu_hard()
                else:
                    LoseMenu(self.game, self.state).display_menu()
            elif self.state == 'GHOST':
                self.win = MyPlay.Play(GHOSTMODE, True)
                if self.win:
                    WinMenu(self.game, self.state).display_menu_ghost()
                else:
                    LoseMenu(self.game, self.state).display_menu()

class LoseMenu(Menu):
    def __init__(self, game, state):
        Menu.__init__(self, game)
        self.state = "RESTART"
        self.state_before = state
        self.restartx, self.restarty = self.mid_w, self.mid_h + 30
        self.gotomenux, self.gotomenuy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.restartx - 160, self.restarty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('YOU LOSE', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("RESTART", 30, self.restartx, self.restarty)
            self.game.draw_text("GO TO MENU", 30, self.gotomenux, self.gotomenuy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if (self.game.DOWN_KEY or self.game.UP_KEY):
            if self.state == 'RESTART':
                self.cursor_rect.midtop = (self.gotomenux - 160, self.gotomenuy)
                self.state = 'GO TO MENU'
            elif self.state == 'GO TO MENU':
                self.cursor_rect.midtop = (self.restartx - 160, self.restarty)
                self.state = 'RESTART'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'RESTART':
                if self.state_before == 'EASY':
                    self.win = MyPlay.Play(EASYMODE, False)
                elif self.state_before == 'NORMAL':
                    self.win = MyPlay.Play(NORMALMODE, False)
                elif self.state_before == 'HARD':
                    self.win = MyPlay.Play(HARDMODE, False)
                elif self.state_before == 'GHOST':
                    self.win = MyPlay.Play(GHOSTMODE, True)
                self.game.reset_keys()
                pygame.event.clear()
                if self.win:
                    if(self.state_before == 'HARD'):
                        WinMenu(self.game, self.state_before).display_menu_hard()
                    else:
                        WinMenu(self.game, self.state_before).display_menu()
                else:
                    LoseMenu(self.game, self.state_before).display_menu()
            elif self.state == 'GO TO MENU':
                self.game.reset_keys()
                MainMenu(self.game).display_menu()
            self.run_display = False

class WinMenu(Menu):
    def __init__(self, game, state):
        Menu.__init__(self, game)
        self.state = "NEXT LEVEL"
        self.state_before = state
        self.nextlevelx, self.nextlevely = self.mid_w, self.mid_h + 45
        self.gotomenux, self.gotomenuy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.nextlevelx - 160, self.nextlevely)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('YOU WIN', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("NEXT LEVEL", 30, self.nextlevelx, self.nextlevely)
            self.game.draw_text("GO TO MENU", 30, self.gotomenux, self.gotomenuy)
            self.draw_cursor()
            self.blit_screen()
    
    def display_menu_hard(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input2()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('YOU WIN', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("FIND HIDDEN LEVEL", 30, self.nextlevelx, self.nextlevely - 50)
            self.game.draw_text("GO TO MENU", 30, self.gotomenux, self.gotomenuy)
            self.cursor_rect.midtop = (self.gotomenux - 160, self.gotomenuy)
            self.draw_cursor()
            self.blit_screen()
    
    def display_menu_ghost(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input2()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('CONGRATULATIONS ON', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("WASTING YOUR TIME", 40, self.nextlevelx, self.nextlevely - 40)
            self.game.draw_text("GO TO MENU", 30, self.gotomenux, self.gotomenuy)
            self.cursor_rect.midtop = (self.gotomenux - 160, self.gotomenuy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if (self.game.DOWN_KEY or self.game.UP_KEY):
            if self.state == 'NEXT LEVEL':
                self.cursor_rect.midtop = (self.gotomenux - 160, self.gotomenuy)
                self.state = 'GO TO MENU'
            elif self.state == 'GO TO MENU':
                self.cursor_rect.midtop = (self.nextlevelx - 160, self.nextlevely)
                self.state = 'NEXT LEVEL'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'NEXT LEVEL':
                self.game.playing = True
                if self.state_before == 'EASY':
                    self.win = MyPlay.Play(NORMALMODE, False)
                    self.game.reset_keys()
                    pygame.event.clear()
                    if self.win:
                        WinMenu(self.game, 'NORMAL').display_menu()
                    else:
                        LoseMenu(self.game, 'NORMAL').display_menu()
                elif self.state_before == 'NORMAL':
                    self.win = MyPlay.Play(HARDMODE, False)
                    self.game.reset_keys()
                    pygame.event.clear()
                    if self.win:
                        WinMenu(self.game, 'HARD').display_menu_hard()
                    else:
                        LoseMenu(self.game, 'HARD').display_menu()
            elif self.state == 'GO TO MENU':
                self.game.reset_keys()
                pygame.event.clear()
                MainMenu(self.game).display_menu()
            self.run_display = False
            
    def check_input2(self):
        if self.game.START_KEY:
            self.game.reset_keys()
            pygame.event.clear()
            MainMenu(self.game).display_menu()
            self.run_display = False