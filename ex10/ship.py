
class Ship:
    """
    The ship object class
    """

    def __init__(self, location_x, location_y, direct, x_speed, y_speed,
                 radios):
        """
        The function responsible for the ship fields
        :param location_x: Position on the x axis
        :param location_y: Position on the y axis
        :param direct: The direction of the ship
        :param x_speed: Speed ​​on the x axis
        :param y_speed: Speed ​​on the y axis
        :param radios: The ship radius
        """
        self.__x_location = location_x
        self.__y_location = location_y
        self.__y_speed = y_speed
        self.__x_speed = x_speed
        self.__direction = direct
        self.__radios = radios

    def get_xlocation(self):
        """
        A function that returns the position of the ship on the x axis
        :return: The position on the x axis
        """
        return self.__x_location

    def get_ylocation(self):
        """
        A function that returns the position of the shipon the y axis
        :return: The position on the y axis.
        """
        return self.__y_location

    def get_radius(self):
        """
         A function that returns a radius of the ship
        :return: radius of the ship
        """
        return self.__radios

    def get_speed(self):
        """
         A function that returns velocity on the axes.
        :return: the ship speed
        """
        return self.__x_speed, self.__y_speed

    def set_location(self, location_x, location_y):
        """
                A function that changes the position of the ship
        :param location_x: New location on the x axis
        :param location_y: New location on the y axis
        :param location_x:
        :param location_y:
        :return:
        """
        self.__x_location = location_x
        self.__y_location = location_y

    def set_speed(self, new_x, new_y):
        """
         A function that changes the speed of the ship
        :param new_x: New speed on the x axis
        :param new_y: New speed on the y axis
        :return:
        """
        self.__y_speed = new_y
        self.__x_speed = new_x

    def set_head(self, change):
        """
        A function that changes the direction of the ship
        :param change: a new direction
        :return:
        """
        self.__direction += change
        if self.__direction > 360:
            self.__direction = self.__direction - 360
        elif self.__direction < 0:
            self.__direction = 360 + self.__direction

    def get_head(self):
        """
         A function that returns the direction of the ship
        :return: direction of the torpedo
        """
        return self.__direction
