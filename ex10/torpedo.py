
class Torpedo:
    """
    The torpedo object class
    """

    def __init__(self, location_x, location_y,direct, x_speed, y_speed,radios):
        """The function responsible for the torpedo fields
        :param location_x: Position on the x axis
        :param location_y: Position on the y axis
        :param direct: The direction of the torpedo
        :param x_speed: Speed ​​on the x axis
        :param y_speed: Speed ​​on the y axis
        :param radios: The torpedo radius"""
        self.__x_location = location_x
        self.__y_location = location_y
        self.__y_speed = y_speed
        self.__x_speed = x_speed
        self.__direction = direct
        self.__radios = radios
        self.__life_time = 0

    def get_life_time(self):
        """
        A function that returns a life time of the torpedo
        :return: The life time of the torpedo
        """
        return self.__life_time

    def get_radius(self):
        """
        A function that returns a radius of the torpedo
        :return: radius of the torpedo
        """
        return self.__radios

    def add_life_time(self, num):
        """
         A function that adds life time to the torpedo
        :param num: Life time to add to the torpedo
        :return:
        """
        self.__life_time += num

    def get_speed(self):
        """
        A function that returns the torpedo speed
        :return: the torpedo speed
        """
        return self.__x_speed, self.__y_speed

    def set_location(self,location_x,location_y):
        """
        A function that changes the position of the torpedo
        :param location_x: New location on the x axis
        :param location_y: New location on the y axis
        """
        self.__x_location = location_x
        self.__y_location = location_y

    def get_xlocation(self):
        """
         A function that returns the position of the torpedo on the x axis
        :return: location on the x axis
        """
        return self.__x_location

    def get_ylocation(self):
        """
         A function that returns the position of the torpedo on the y axis
        :return: location on the y axis
        """
        return self.__y_location

    def get_head(self):
        """
        A function that returns the direction of the torpedo
        :return: direction of the torpedo
        """
        return self.__direction
