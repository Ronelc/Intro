from screen import Screen
from torpedo import Torpedo
from asteroid import Asteroid
from ship import Ship
import sys
import random
import math


CRASH = "A collision occurred"
CRASH_MSG = "Asteroid crashed into the spacecraft"
DEFAULT_ASTEROIDS_NUM = 5
WIN = "you won"
LOSS = "you lose"
END = "The game is over"
QUIT = "you chose to quit"
ASTEROIDS_START_SIZE = 3
ASTEROIDS_MEDIUM_SIZE = 2
ASTEROIDS_SMALL_SIZE = 1
CHANGE_DEGREE = 7


class GameRunner:
    """
    The main class that runs the game
    """

    MAX_TORPEDO = 10
    TORPEDO_RADIOS = 4
    SHIP_RADIOS = 1
    LIFE_TIME_TORPIDO = 200
    START_LIFE = 3

    def __init__(self, asteroids_amount):
        """
         A function that runs the game and within it are the needed fields
        :param asteroids_amount: The number of asteroids in play
        """
        self.__ship_life = self.START_LIFE
        self.__torpedo_lst = []
        self.__asteroids_lst = []
        self.asteroids_amount = asteroids_amount
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__score = 0
        x, y = self.get_random_x_y()
        self.__ship = Ship(x, y, 0, 0, 0, self.SHIP_RADIOS)
        for i in range(asteroids_amount):
            self.add_new_asteroid()

    def get_random_x_y(self):
        """
        A function that selects a random position on the axes,
        within the boundaries of the screen
        :return: Location on the axes
        """
        x = random.randint(self.__screen_min_x, self.__screen_max_x)
        y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return x, y

    def run(self):
        """
        A function that runs the start screen
        """
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):

        self.draw_all()
        self.check_press()
        self.move_all()
        self.check_interactions()
        self.is_finish()

    def draw_all(self):
        """
        draw all the objects
        :return:
        """
        self.draw_ship()
        self.draw_torpedoes()
        self.draw_asteroids()

    def check_press(self):
        """
        A function that checks which keys have been pressed
        and operated accordingly
        """
        if self.__screen.is_left_pressed():
            self.__ship.set_head(CHANGE_DEGREE)
        if self.__screen.is_right_pressed():
            self.__ship.set_head(-1 * CHANGE_DEGREE)
        if self.__screen.is_up_pressed():
            self.change_speed()
        if self.__screen.is_space_pressed():
            if len(self.__torpedo_lst) < self.MAX_TORPEDO:
                self.__screen.register_torpedo(self.add_torpedo())

    def is_finish(self):
        """
        A function that checks whether the game should end
        """
        if self.__ship_life == 0:
            self.__screen.show_message(END, LOSS)
            self.__screen.end_game()
            sys.exit()

        elif not self.__asteroids_lst:
            self.__screen.show_message(END, WIN)
            self.__screen.end_game()
            sys.exit()

        elif self.__screen.should_end():
            self.__screen.show_message(END, QUIT)
            self.__screen.end_game()
            sys.exit()

    def draw_torpedoes(self):
        """
        the function draw the torpedoes
        :return:
        """
        for torpedo in self.__torpedo_lst:
            self.__screen.draw_torpedo(torpedo, torpedo.get_xlocation(),
                                       torpedo.get_ylocation(),
                                       torpedo.get_head())

    def draw_ship(self):
        """
        the function draw the ship
        :return:
        """
        self.__screen.draw_ship(self.__ship.get_xlocation(),
                                self.__ship.get_ylocation(),
                                self.__ship.get_head())

    def change_speed(self):
        """
        A function that changes the speed of the spacecraft
        and gives it a new speed
        :return:
        """
        x, y = self.__ship.get_speed()
        x = x + math.cos(math.radians(self.__ship.get_head()))
        y = y + math.sin(math.radians(self.__ship.get_head()))
        self.__ship.set_speed(x, y)

    def move_obj(self, obj):
        """
         A function that is responsible for moving the objects on the screen
        :param obj: Asteroid, torpedo or ship
        :return:
        """
        x_speed, y_speed = obj.get_speed()
        delta_x = self.__screen_max_x - self.__screen_min_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        obj.set_location(self.__screen_min_x + (obj.get_xlocation() + x_speed -
                                                self.__screen_min_x) % delta_x,
                         self.__screen_min_y + (obj.get_ylocation() + y_speed -
                                                self.__screen_min_y) % delta_y)

    def add_torpedo(self):
        """
        A function that adds torpedo to the screen, and to the torpedos list
        :return: The new torpedo who added to the list
        :return:
        """
        x_location = self.__ship.get_xlocation()
        y_location = self.__ship.get_ylocation()
        head = self.__ship.get_head()
        x_speed, y_speed = self.__ship.get_speed()
        x_speed += math.cos(math.radians(head))
        y_speed += math.sin(math.radians(head))
        self.__torpedo_lst.append(
            Torpedo(x_location, y_location, head, x_speed,
                    y_speed, self.TORPEDO_RADIOS))
        return self.__torpedo_lst[-1]

    def move_all(self):
        """
         A function that checks the torpedo's lifespan and
        deletes it from the screen if necessary

        :return:
        """
        self.move_obj(self.__ship)
        for torpedo in self.__torpedo_lst:
            self.move_obj(torpedo)
            torpedo.add_life_time(1)
            if torpedo.get_life_time() == self.LIFE_TIME_TORPIDO:
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedo_lst.remove(torpedo)
                del torpedo
        for asteroid in self.__asteroids_lst:
            self.move_obj(asteroid)

    def check_interactions(self):
        """
        A function that checks if an object conflict occurs and
        updates the screen accordingly
        :return:
        """
        for asteroid in self.__asteroids_lst:
            if asteroid.has_intersection(self.__ship):
                self.__ship_life -= 1
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids_lst.remove(asteroid)
                del asteroid
                self.__screen.show_message(CRASH, CRASH_MSG)
                self.__screen.remove_life()
                break
            for torpedo in self.__torpedo_lst:
                if asteroid.has_intersection(torpedo):
                    self.split(asteroid,torpedo)
                    break

    def add_new_asteroid(self):
        """
        the function add an asteroid to the list and to the screen
        :return:
        """
        x, y = self.get_random_x_y()
        while x == self.__ship.get_xlocation() and \
                y == self.__ship.get_xlocation():
            x, y = self.get_random_x_y()
        self.__asteroids_lst.append(Asteroid(x, y, self.get_random_speed(),
                                             self.get_random_speed(),
                                             ASTEROIDS_START_SIZE))
        self.__screen.register_asteroid(self.__asteroids_lst[-1],
                                        ASTEROIDS_START_SIZE)

    def draw_asteroids(self):
        """
        the function draw asteroid
        :return:
        """
        for asteroid in self.__asteroids_lst:
            self.__screen.draw_asteroid(asteroid, asteroid.get_xlocation(),
                                        asteroid.get_ylocation())

    def remove(self, asteroid, torpedo):
        """
        A function that removes actionable objects from the game
        :param asteroid: Asteroid object
        :param torpedo: Torpedo object
        """
        self.__screen.unregister_torpedo(torpedo)
        self.__torpedo_lst.remove(torpedo)
        del torpedo
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids_lst.remove(asteroid)
        del asteroid

    def add_asteroid(self,asteroid):
        """
        add asteroid to the list and on the screen
        :param asteroid: asteroid
        :return:
        """
        self.__asteroids_lst.append(asteroid)
        self.__screen.register_asteroid(asteroid, asteroid.get_size())
        self.__screen.draw_asteroid(asteroid, asteroid.get_xlocation(),
                                    asteroid.get_ylocation())

    def split(self, asteroid, torpedo):
        """
        A function that splits the asteroid into two smaller asteroids,
        or deletes the asteroid when needed. And updates the score
        :param asteroid: Asteroid object
        :param torpedo: Torpedo object
        """
        if asteroid.get_size() == ASTEROIDS_SMALL_SIZE:
            self.remove(asteroid, torpedo)
            self.__score += 100
        else:
            asteroid_location_x = asteroid.get_xlocation()
            asteroid_location_y = asteroid.get_ylocation()
            size = 0
            speed_x, speed_y = self.new_speed(asteroid,torpedo)
            if asteroid.get_size() == ASTEROIDS_START_SIZE:
                size = ASTEROIDS_MEDIUM_SIZE
                self.__score += 20
            elif asteroid.get_size() == ASTEROIDS_MEDIUM_SIZE:
                size = ASTEROIDS_SMALL_SIZE
                self.__score += 50
            self.add_asteroid(Asteroid(asteroid_location_x,asteroid_location_y,
                                       1 * speed_x, 1 * speed_y, size))
            self.add_asteroid(Asteroid(asteroid_location_x,asteroid_location_y,
                                       -1 * speed_x, -1 * speed_y, size))
            self.remove(asteroid, torpedo)
        self.__screen.set_score(self.__score)

    def new_speed(self, asteroid, torpedo):
        """
        calculate the speed for the new asteroid
        :param asteroid: asteroid
        :param torpedo: torpedo
        :return:
        """
        lst = []
        torpedo_speed = torpedo.get_speed()
        old_speed_asteroid = asteroid.get_speed()
        for i in range(2):
            new_speed = (torpedo_speed[i] + old_speed_asteroid[i]) / \
                        math.sqrt(old_speed_asteroid[0] ** 2 +
                                  old_speed_asteroid[1] ** 2)
            lst.append(new_speed)
        return lst[0], lst[1]

    def get_random_speed(self):
        """
        The function selects a random position between 1 and 4 on the axes
        :return: Location on the axes
        """
        speed = random.randint(1, 4)
        direction = random.choice([1,-1])
        return speed * direction


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
