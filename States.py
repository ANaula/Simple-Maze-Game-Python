import pygame
from Static_Objects import Static_Objects
from Moving_Objects import Moving_Objects
from Goal_Objects import Goal_Objects
from Button import Button
from Player import Player
from sys import exit


class States():
    def __init__(self, window):
        self.type = "Main_Menu"
        self.window = window
        self.text_font = pygame.font.Font("font/Lato-Regular.ttf", 100)
        self.small_text_font = pygame.font.Font("font/Lato-BlackItalic.ttf", 35)
        self.game_level = 0

    def game_state(self):
        background_surface = pygame.Surface((self.window.get_width(), self.window.get_height()))
        background_surface.fill((173, 216, 230))
        static_objects = pygame.sprite.Group()
        player = pygame.sprite.GroupSingle()
        moving_objects = pygame.sprite.Group()
        goal_object = pygame.sprite.GroupSingle()

        def level_manager():
            if self.game_level == 0:
                next_level_check(True)

            if self.game_level == 1:
                static_objects.add(Static_Objects(200, 0, 50, 620))
                static_objects.add(Static_Objects(1030, 100, 50, 620))

                player.add(Player(0, 0, self.window))

                moving_objects.add(Moving_Objects(250, 0, 156, 156, "down", self.window, static_objects))
                moving_objects.add(Moving_Objects(406, 564, 156, 156, "up", self.window, static_objects))
                moving_objects.add(Moving_Objects(562, 0, 156, 156, "down", self.window, static_objects))
                moving_objects.add(Moving_Objects(718, 564, 156, 156, "up", self.window, static_objects))
                moving_objects.add(Moving_Objects(874, 0, 156, 156, "down", self.window, static_objects))
                moving_objects.add(Moving_Objects(250, 282, 156, 156, "right", self.window, static_objects))
                moving_objects.add(Moving_Objects(0, 250, 40, 170, "right", self.window, static_objects))
                moving_objects.add(Moving_Objects(1240, 250, 40, 170, "left", self.window, static_objects))

                goal_object.add(Goal_Objects(1210, 650))
                level_display_surface = self.small_text_font.render(f"Level {self.game_level}", False, (105, 105, 105))
                level_display_rect = level_display_surface.get_rect(topleft=(10, 0))

                clock = pygame.time.Clock()

                while self.game_level == 1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.type = "Pause"
                                return 0

                    self.window.blit(background_surface, (0, 0))
                    static_objects.draw(self.window)
                    self.window.blit(level_display_surface, level_display_rect)
                    moving_objects.draw(self.window)
                    goal_object.draw(self.window)
                    player.draw(self.window)

                    player.update(player_object_collision())
                    moving_objects.update()
                    next_level_check()

                    pygame.display.update()
                    clock.tick(60)
            if self.game_level == 2:
                static_objects.add(Static_Objects(1070, 0, 60, 570))
                static_objects.add(Static_Objects(210, 510, 860, 60))
                static_objects.add(Static_Objects(150, 150, 60, 420))
                static_objects.add(Static_Objects(210, 150, 610, 60))

                player.add(Player(1230, 0, self.window))

                moving_objects.add(Moving_Objects(1130, 150, 50, 50, "right", self.window, static_objects))
                moving_objects.add(Moving_Objects(1230, 350, 50, 50, "left", self.window, static_objects))
                moving_objects.add(Moving_Objects(580, 620, 50, 50, "up", self.window, static_objects))
                moving_objects.add(Moving_Objects(1230, 570, 30, 150, "left", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(100, 350, 50, 50, "left", self.window, static_objects))
                moving_objects.add(Moving_Objects(0, 0, 30, 150, "right", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(580, 0, 50, 50, "down", self.window, static_objects))
                moving_objects.add(Moving_Objects(400, 410, 200, 100, "up", self.window, static_objects))

                level_display_surface = self.small_text_font.render(f"Level {self.game_level}", False, (105, 105, 105))
                level_display_rect = level_display_surface.get_rect(topleft=(10, 0))

                goal_object.add(Goal_Objects(210, 210, 100, 300))
                clock = pygame.time.Clock()

                while self.game_level == 2:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.type = "Pause"
                                return 0

                    self.window.blit(background_surface, (0, 0))
                    static_objects.draw(self.window)
                    self.window.blit(level_display_surface, level_display_rect)
                    moving_objects.draw(self.window)
                    goal_object.draw(self.window)
                    player.draw(self.window)

                    player.update(player_object_collision())
                    moving_objects.update()
                    next_level_check()

                    pygame.display.update()
                    clock.tick(60)

            if self.game_level == 3:
                static_objects.add(Static_Objects(0, 0, 1280, 40))
                static_objects.add(Static_Objects(0, 0, 40, 720))
                static_objects.add(Static_Objects(1240, 0, 40, 720))
                static_objects.add(Static_Objects(0, 680, 1280, 40))
                static_objects.add(Static_Objects(40, 190, 200, 100))
                static_objects.add(Static_Objects(200, 0, 40, 120))
                static_objects.add(Static_Objects(240, 250, 920, 40))
                static_objects.add(Static_Objects(120, 490, 1120, 40))
                static_objects.add(Static_Objects(120, 530, 250, 70))
                static_objects.add(Static_Objects(480, 530, 250, 70))
                static_objects.add(Static_Objects(840, 530, 250, 70))

                player.add(Player(40, 40, self.window))

                moving_objects.add(Moving_Objects(240, 40, 200, 40, "down", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(510, 40, 200, 40, "down", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(780, 40, 200, 40, "down", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(1050, 40, 190, 40, "down", self.window, static_objects, 2))

                moving_objects.add(Moving_Objects(780, 290, 200, 40, "down", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(510, 450, 200, 40, "up", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(240, 290, 200, 40, "down", self.window, static_objects, 2))
                moving_objects.add(Moving_Objects(40, 450, 130, 40, "up", self.window, static_objects, 2))

                moving_objects.add(Moving_Objects(40, 600, 40, 80, "right", self.window, static_objects))

                level_display_surface = self.small_text_font.render(f"Level {self.game_level}", False, (105, 105, 105))
                level_display_rect = level_display_surface.get_rect(topleft=(10, 0))

                goal_object.add(Goal_Objects(1060, 530, 180, 70))
                clock = pygame.time.Clock()

                while self.game_level == 3:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.type = "Pause"
                                return 0

                    self.window.blit(background_surface, (0, 0))
                    static_objects.draw(self.window)
                    self.window.blit(level_display_surface, level_display_rect)
                    moving_objects.draw(self.window)
                    goal_object.draw(self.window)
                    player.draw(self.window)

                    player.update(player_object_collision())
                    moving_objects.update()
                    next_level_check()

                    pygame.display.update()
                    clock.tick(60)

        def player_object_collision():
            if pygame.sprite.spritecollide(player.sprite, moving_objects, False) or pygame.sprite.spritecollide(
                    player.sprite, static_objects, False):
                return True

        def next_level_check(start=False):
            if start or pygame.sprite.collide_rect(player.sprite, goal_object.sprite):
                if not start:
                    player.empty()
                    moving_objects.empty()
                    static_objects.empty()
                    goal_object.empty()
                self.game_level += 1
                next_surface = pygame.Surface((self.window.get_width(), self.window.get_height()))
                next_surface.fill((173, 216, 230))
                time = 0

                next_level_text_surface = self.text_font.render(f"Level {self.game_level}", False, (0, 0, 0))
                next_level_text_rect = next_level_text_surface.get_rect(center=(self.window.get_width()/2, self.window.get_height()/2))

                end_text_surface = self.text_font.render("Congratulations", False, (0, 0, 0))
                end_text_rect = end_text_surface.get_rect(center=(self.window.get_width()/2, self.window.get_height()/2-50))
                sub_end_text_surface = self.small_text_font.render("You have passed all the levels!", False, (0, 0, 0))
                sub_end_text_rect = sub_end_text_surface.get_rect(center=(self.window.get_width()/2, self.window.get_height()/2+50))

                while time < 60 * 5:
                    self.window.blit(next_surface, (0, 0))
                    if self.game_level <= 3:
                        self.window.blit(next_level_text_surface, next_level_text_rect)
                    else:
                        self.window.blit(end_text_surface, end_text_rect)
                        self.window.blit(sub_end_text_surface, sub_end_text_rect)
                    pygame.display.update()
                    time += 0.1

                if self.game_level > 3:
                    self.game_level = 0
                    self.type = "Main_Menu"

        while self.type == "Game":
            level_manager()

    def main_menu_state(self):
        background_surface = pygame.Surface((self.window.get_width(), self.window.get_height()))
        background_surface.fill((173, 216, 230))
        big_text_surface = self.text_font.render("Simple Maze Game", False, (0, 0, 0))
        big_text_rect = big_text_surface.get_rect(center=(self.window.get_width()/2, self.window.get_height()/2-200))
        small_text_surface = self.small_text_font.render("(Yet Another)", False, (0, 0, 0))
        small_text_rect = small_text_surface.get_rect(bottomleft=big_text_rect.topleft)

        play_button = Button(self.window, self.window.get_width()/2, 600, 250, 80, "Play", (0, 0, 0))
        instructions_button = Button(self.window, self.window.get_width()/2 + 350, 600, 250, 80, "Instructions", (0, 0, 0))
        quit_button = Button(self.window, self.window.get_width()/2 - 350, 600, 250, 80, "Quit", (0, 0, 0))

        player_surface = pygame.Surface((180, 180))
        player_surface.fill((139, 0, 0))
        player_rect = player_surface.get_rect(center=(self.window.get_width()/2, self.window.get_height()/2+20))

        while self.type == "Main_Menu":
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                play_button.hover_check(pos)
                instructions_button.hover_check(pos)
                quit_button.hover_check(pos)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.click_check(pos):
                        self.type = "Game"
                    if instructions_button.click_check(pos):
                        self.type = "Instructions"
                    if quit_button.click_check(pos):
                        pygame.quit()
                        exit()
            self.window.blit(background_surface, (0, 0))
            self.window.blit(big_text_surface, big_text_rect)
            self.window.blit(small_text_surface, small_text_rect)
            self.window.blit(player_surface, player_rect)

            play_button.draw()
            instructions_button.draw()
            quit_button.draw()

            pygame.display.update()

    def pause_state(self):
        background_surface = pygame.Surface((self.window.get_width(), self.window.get_height()))
        background_surface.fill((173, 216, 230))
        pause_text_surface = self.text_font.render("-Paused-", False, (105, 105, 105))
        pause_text_rect = pause_text_surface.get_rect(center=(self.window.get_width()/2, self.window.get_height()/2-50))
        continue_button = Button(self.window, self.window.get_width()/2 + 135, self.window.get_height()/2+150, 180, 75, "Continue", (0, 0, 0))
        main_menu_button = Button(self.window, self.window.get_width()/2 - 135, self.window.get_height()/2+150, 180, 75, "Main Menu", (0, 0, 0))

        while self.type == "Pause":
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                continue_button.hover_check(pos)
                main_menu_button.hover_check(pos)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if continue_button.click_check(pos):
                        self.type = "Game"
                    if main_menu_button.click_check(pos):
                        self.game_level = 0
                        self.type = "Main_Menu"
            self.window.blit(background_surface, (0, 0))
            self.window.blit(pause_text_surface, pause_text_rect)
            continue_button.draw()
            main_menu_button.draw()

            pygame.display.update()

    def instructions_state(self):
        background_instructions_surface = pygame.image.load("images/pythongameinstructions.png").convert_alpha()
        background_instructions_rect = background_instructions_surface.get_rect(topleft=(0, 0))
        main_menu_button = Button(self.window, self.window.get_width()/2, self.window.get_height()/2+280, 180, 75, "Main Menu", (0, 0, 0))

        while self.type == "Instructions":
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                main_menu_button.hover_check(pos)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_button.click_check(pos):
                        self.type = "Main_Menu"

            self.window.blit(background_instructions_surface, background_instructions_rect)
            main_menu_button.draw()

            pygame.display.update()

    def state_manager(self):
        if self.type == "Game":
            self.game_state()
        if self.type == "Main_Menu":
            self.main_menu_state()
        if self.type == "Pause":
            self.pause_state()
        if self.type == "Instructions":
            self.instructions_state()

