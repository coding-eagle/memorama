# ###################################################
# __  __ ___ __  __  ___  ___    _   __  __   _     #
# |  \/  | __|  \/  |/ _ \| _ \  /_\ |  \/  | /_\   #
# | |\/| | _|| |\/| | (_) |   / / _ \| |\/| |/ _ \  #
# |_|  |_|___|_|  |_|\___/|_|_\/_/ \_\_|  |_/_/ \_\ #
#####################################################
# A memorization game written in Python with the help of the pygame library

import pygame
from random import seed, randint
from abc import ABC, abstractmethod


class Memorama:
    _window_width = 640
    _window_height = 480
    _window_title = "Memorama v1.0 - Coding Eagle"
    _background_color = (208, 208, 208)
    _red_sqr_active_res = "resources/red_active.png"
    _red_sqr_inactive_res = "resources/red_inactive.png"
    _red_sqr_pos = (50, 20)
    _yellow_sqr_active_res = "resources/yellow_active.png"
    _yellow_sqr_inactive_res = "resources/yellow_inactive.png"
    _yellow_sqr_pos = (192, 20)
    _blue_sqr_active_res = "resources/blue_active.png"
    _blue_sqr_inactive_res = "resources/blue_inactive.png"
    _blue_sqr_pos = (334, 20)
    _lapis_sqr_active_res = "resources/lapis_active.png"
    _lapis_sqr_inactive_res = "resources/lapis_inactive.png"
    _lapis_sqr_pos = (50, 162)
    _gray_sqr_active_res = "resources/gray_active.png"
    _gray_sqr_inactive_res = "resources/gray_inactive.png"
    _gray_sqr_pos = (192, 162)
    _orange_sqr_active_res = "resources/orange_active.png"
    _orange_sqr_inactive_res = "resources/orange_inactive.png"
    _orange_sqr_pos = (334, 162)
    _green_sqr_active_res = "resources/green_active.png"
    _green_sqr_inactive_res = "resources/green_inactive.png"
    _green_sqr_pos = (50, 304)
    _magenta_sqr_active_res = "resources/magenta_active.png"
    _magenta_sqr_inactive_res = "resources/magenta_inactive.png"
    _magenta_sqr_pos = (192, 304)
    _cyan_sqr_active_res = "resources/cyan_active.png"
    _cyan_sqr_inactive_res = "resources/cyan_inactive.png"
    _cyan_sqr_pos = (334, 304)
    _square_size = (150, 150)
    _heart_res = "resources/heart.png"
    _heart_one_pos = (500, 20)
    _heart_two_pos = (550, 20)
    _heart_three_pos = (600, 20)
    _heart_size = (30, 28)
    _input_correct_res = "resources/excellent_100.png"
    _input_correct_pos = (20, 20)
    _input_correct_size = (500, 291)
    _input_wrong_res = "resources/incorrect_100.png"
    _input_wrong_pos = (20, 20)
    _input_wrong_size = (500, 291)
    _game_over_res = "resources/game_over.png"
    _game_over_pos = (60, 100)
    _game_over_size = (500, 291)
    IDLE_STATE = 0
    PLAY_SEQUENCE_STATE = 1
    INPUT_SEQUENCE_STATE = 2
    INPUT_CORRECT_STATE = 3
    INPUT_WRONG_STATE = 4
    GAME_OVER_STATE = 5

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._red_square = None
        self._yellow_square = None
        self._blue_square = None
        self._lapis_square = None
        self._gray_square = None
        self._orange_square = None
        self._green_square = None
        self._magenta_square = None
        self._cyan_square = None
        self._heart_one = None
        self._heart_two = None
        self._heart_three = None
        self._input_correct = None
        self._input_wrong = None
        self._game_over = None
        self._controls = []
        self._current_state = Memorama.IDLE_STATE
        self._clock = pygame.time.Clock()
        self._render_time = 0
        self._frame_count = 0
        self._sequence = []
        self._squares_dict = {}
        self._current_square = 0
        self._expected_square_clicked = False
        self._strikes = 0

    def init(self):
        pygame.init()
        seed()
        self._display_surf = pygame.display.set_mode((self._window_width, self._window_height), pygame.HWSURFACE)
        self._display_surf.fill(self._background_color)
        pygame.display.set_caption(self._window_title)

        self._red_square = Square(
            "RED_SQUARE",
            pygame.image.load(self._red_sqr_inactive_res),
            pygame.image.load(self._red_sqr_active_res),
            self._red_sqr_pos,
            self._square_size,
            True,
            False)

        self._yellow_square = Square(
            "YELLOW_SQUARE",
            pygame.image.load(self._yellow_sqr_inactive_res),
            pygame.image.load(self._yellow_sqr_active_res),
            self._yellow_sqr_pos,
            self._square_size,
            True,
            False)

        self._blue_square = Square(
            "BLUE_SQUARE",
            pygame.image.load(self._blue_sqr_inactive_res),
            pygame.image.load(self._blue_sqr_active_res),
            self._blue_sqr_pos,
            self._square_size,
            True,
            False)

        self._lapis_square = Square(
            "LAPIS_SQUARE",
            pygame.image.load(self._lapis_sqr_inactive_res),
            pygame.image.load(self._lapis_sqr_active_res),
            self._lapis_sqr_pos,
            self._square_size,
            True,
            False)

        self._gray_square = Square(
            "GRAY_SQUARE",
            pygame.image.load(self._gray_sqr_inactive_res),
            pygame.image.load(self._gray_sqr_active_res),
            self._gray_sqr_pos,
            self._square_size,
            True,
            False)

        self._orange_square = Square(
            "ORANGE_SQUARE",
            pygame.image.load(self._orange_sqr_inactive_res),
            pygame.image.load(self._orange_sqr_active_res),
            self._orange_sqr_pos,
            self._square_size,
            True,
            False)

        self._green_square = Square(
            "GREEN_SQUARE",
            pygame.image.load(self._green_sqr_inactive_res),
            pygame.image.load(self._green_sqr_active_res),
            self._green_sqr_pos,
            self._square_size,
            True,
            False)

        self._magenta_square = Square(
            "MAGENTA_SQUARE",
            pygame.image.load(self._magenta_sqr_inactive_res),
            pygame.image.load(self._magenta_sqr_active_res),
            self._magenta_sqr_pos,
            self._square_size,
            True,
            False)

        self._cyan_square = Square(
            "CYAN_SQUARE",
            pygame.image.load(self._cyan_sqr_inactive_res),
            pygame.image.load(self._cyan_sqr_active_res),
            self._cyan_sqr_pos,
            self._square_size,
            True,
            False)

        self._heart_one = Image(
            "HEART_ONE",
            pygame.image.load(self._heart_res),
            self._heart_one_pos,
            self._heart_size,
            True)

        self._heart_two = Image(
            "HEART_TWO",
            pygame.image.load(self._heart_res),
            self._heart_two_pos,
            self._heart_size,
            True)

        self._heart_three = Image(
            "HEART_THREE",
            pygame.image.load(self._heart_res),
            self._heart_three_pos,
            self._heart_size,
            True)

        self._input_correct = Image(
            "INPUT_CORRECT",
            pygame.image.load(self._input_correct_res),
            self._input_correct_pos,
            self._input_correct_size,
            False
        )

        self._input_wrong = Image(
            "INPUT_WRONG",
            pygame.image.load(self._input_wrong_res),
            self._input_wrong_pos,
            self._input_wrong_size,
            False
        )

        self._game_over = Image(
            "GAME_OVER",
            pygame.image.load(self._game_over_res),
            self._game_over_pos,
            self._game_over_size,
            False)

        self._controls.extend([
            self._red_square,
            self._yellow_square,
            self._blue_square,
            self._lapis_square,
            self._gray_square,
            self._orange_square,
            self._green_square,
            self._magenta_square,
            self._cyan_square,
            self._heart_one,
            self._heart_two,
            self._heart_three,
            self._input_correct,
            self._input_wrong,
            self._game_over
        ])

        self._squares_dict["RED_SQUARE"] = self._red_square
        self._squares_dict["YELLOW_SQUARE"] = self._yellow_square
        self._squares_dict["BLUE_SQUARE"] = self._blue_square
        self._squares_dict["LAPIS_SQUARE"] = self._lapis_square
        self._squares_dict["GRAY_SQUARE"] = self._gray_square
        self._squares_dict["ORANGE_SQUARE"] = self._orange_square
        self._squares_dict["GREEN_SQUARE"] = self._green_square
        self._squares_dict["MAGENTA_SQUARE"] = self._magenta_square
        self._squares_dict["CYAN_SQUARE"] = self._cyan_square

        self._running = True

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Traverse the list in reverse order so that the frontmost control is evaluated first
            for control in reversed(self._controls):
                # Only visible controls can be clicked
                if control.is_point_clickable(event.pos) and control.visible:
                    control.clicked = True
                    break
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for control in self._controls:
                control.clicked = False

    def run_state_machine(self):
        if self._current_state == Memorama.IDLE_STATE:
            self.idle_state()
        elif self._current_state == Memorama.PLAY_SEQUENCE_STATE:
            self.play_sequence_state()
        elif self._current_state == Memorama.INPUT_SEQUENCE_STATE:
            self.input_sequence_state()
        elif self._current_state == Memorama.INPUT_CORRECT_STATE:
            self.input_correct_state()
        elif self._current_state == Memorama.GAME_OVER_STATE:
            self.game_over_state()
        elif self._current_state == Memorama.INPUT_WRONG_STATE:
            self.input_wrong_state()

    def render(self):
        self._display_surf.fill(self._background_color)
        for control in self._controls:
            control.draw(self._display_surf)
        pygame.display.flip()
        self._render_time = self._clock.tick(30)

    def execute(self):
        self.init()
        while self._running:
            for event in pygame.event.get():
                self.process_event(event)
            self.run_state_machine()
            self.render()

    def idle_state(self):
        squares = list(self._squares_dict.keys())
        squares.sort()
        index = randint(0, 8)
        self._sequence.append(squares[index])
        self._current_state = Memorama.PLAY_SEQUENCE_STATE

    def play_sequence_state(self):
        self._frame_count += 1
        if self._frame_count == 7:
            square_name = self._sequence[self._current_square]
            square_handle = self._squares_dict[square_name]
            if square_handle.active:
                square_handle.active = False
                self._current_square += 1
                if self._current_square >= len(self._sequence):
                    self._current_square = 0
                    self._current_state = Memorama.INPUT_SEQUENCE_STATE
            else:
                square_handle.active = True
            self._frame_count = 0

    def input_sequence_state(self):
        expected_square_name = self._sequence[self._current_square]
        for control in self._controls:
            if control.clicked:
                if control.name == expected_square_name:
                    self._expected_square_clicked = True
                    control.active = True
                else:
                    self._strikes += 1
                    self._current_square = 0
                    if self._strikes < 3:
                        self._current_state = Memorama.INPUT_WRONG_STATE
                    else:
                        self._current_state = Memorama.GAME_OVER_STATE
            else:
                if control.name == expected_square_name and self._expected_square_clicked:
                    self._expected_square_clicked = False
                    control.active = False
                    self._current_square += 1
                if self._current_square >= len(self._sequence):
                    self._current_square = 0
                    control.active = False
                    self._current_state = Memorama.INPUT_CORRECT_STATE
        self._heart_one.visible = (self._strikes < 3)
        self._heart_two.visible = (self._strikes < 2)
        self._heart_three.visible = (self._strikes == 0)

    def input_correct_state(self):
        self._frame_count += 1
        self._input_correct.visible = True
        if self._frame_count >= 30:
            self._input_correct.visible = False
            self._current_state = Memorama.IDLE_STATE
            self._frame_count = 0

    def input_wrong_state(self):
        self._frame_count += 1
        self._input_wrong.visible = True
        if self._frame_count >= 30:
            self._input_wrong.visible = False
            self._current_state = Memorama.PLAY_SEQUENCE_STATE
            self._frame_count = 0

    def game_over_state(self):
        self._frame_count += 1
        self._game_over.visible = True
        if self._frame_count >= 90:
            self._strikes = 0
            self._sequence.clear()
            self._game_over.visible = False
            self._frame_count = 0
            self._current_state = Memorama.IDLE_STATE


class Control(ABC):
    def __init__(self, name, surface, position, size, visible):
        self._name = name
        self._surface = surface
        self._position = position
        self._size = size
        self._border_size = 8
        self.visible = visible
        self.clicked = False

    @property
    def name(self):
        return self._name

    @property
    def surface(self):
        return self._surface

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def size(self):
        return self._size

    @property
    def border_size(self):
        return self._border_size

    def is_point_clickable(self, coord):
        coord_x, coord_y = coord
        x_pos, y_pos = self.position
        width, height = self.size

        left_bound = x_pos + self.border_size
        right_bound = x_pos + width - self.border_size
        top_bound = y_pos + self.border_size
        bottom_bound = y_pos + height - self.border_size
        result = (left_bound < coord_x < right_bound) and (top_bound < coord_y < bottom_bound)
        return result

    @abstractmethod
    def draw(self, dst_surface):
        pass


class Square(Control):
    def __init__(self, name, inactive_surface, active_surface, position, size, visible, active):
        super().__init__(name, inactive_surface, position, size, visible)
        self._inactive_surface = inactive_surface
        self._active_surface = active_surface
        self.active = active

    @property
    def inactive_surface(self):
        return self._inactive_surface

    @property
    def active_surface(self):
        return self._active_surface

    def draw(self, dst_surface):
        if self.visible:
            if self.active:
                dst_surface.blit(self.active_surface, self._position)
            else:
                dst_surface.blit(self._inactive_surface, self._position)


class Image(Control):
    def __init__(self, name, surface, position, size, visible):
        super().__init__(name, surface, position, size, visible)

    def draw(self, dst_surface):
        if self.visible:
            dst_surface.blit(self._surface, self._position)


def main():
    memorama = Memorama()
    memorama.execute()


if __name__ == '__main__':
    main()
