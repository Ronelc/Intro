
import math


class Asteroid:
    """
    The asteroid object class
    """

    def __init__(self, location_x, location_y, x_speed, y_speed, size):
        """
       The function responsible for the asteroid fields
       :param location_x: Position on the x axis
       :param location_y: Position on the y axis
       :param x_speed: Speed ​​on the x axis
       :param y_speed: Speed ​​on the y axis
       :param size: Asteroid size
        """
        self.__x_location = location_x
        self.__y_location = location_y
        self.__y_speed = y_speed
        self.__x_speed = x_speed
        self.__asteroid_size = size

    def get_xlocation(self):
        """
         A function that returns the position of the asteroid on the x axis
        :return: The position on the x axis.
        """
        return self.__x_location

    def get_ylocation(self):
        """
        A function that returns the position of the asteroid on the y axis
        :return: The position on the y axis.
        """
        return self.__y_location

    def get_size(self):
        """
        Asteroid size on the axes.
        :return: the asteroid size
        """
        return self.__asteroid_size

    def get_speed(self):
        """
        Asteroid velocity on the axes.
        :return: asteroid velocity
        """
        return self.__x_speed, self.__y_speed

    def asteroid_radius(self):
        """
        A function that returns a radius of the asteroid
        :return: The asteroid radius.
        """
        return self.__asteroid_size * 10 - 5

    def has_intersection(self, obj):
        """
        A function that checks if an object conflict occurs
        :param obj: torpedo or ship
        :return: True if success, False otherwise
        """
        obj_xlocation = obj.get_xlocation()
        obj_ylocation = obj.get_ylocation()
        obj_radius = int(obj.get_radius())
        a = (obj_xlocation - self.__x_location)**2
        b = (obj_ylocation - self.__y_location)**2
        distance = math.sqrt(a + b)
        if distance <= int(self.asteroid_radius()) + obj_radius:
            return True
        return False

    def set_location(self, location_x, location_y):
        """

        A function that changes the position of the asteroid
        :param location_x: New location on the x axis
        :param location_y: New location on the y axis
        :return:
        """
        self.__x_location = location_x
        self.__y_location = location_y
