VERTICAL = 0
HORIZO = 1
DIRACT = {'up': 'u', 'down': 'd', 'right': 'r', 'left': 'l'}
HO_DICT = {'r': 'The car will move one step to the right ',
                    'l': 'The car will move one step to the left'}
VE_DICT = {'u': 'The car will move one step further ',
                    'd': 'The car will move one step back'}
DIRECTIONS = ['u', 'd', 'r', 'l']

class Car:
    """
    A class that produces the vehicle object as per requirements.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row,col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.length = length
        self._location = location
        self._orientation = orientation


    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        lst = []
        if self._orientation == VERTICAL:
            for i in range(self.length):
                lst.append((self._location[0]+i, self._location[1]))
        elif self._orientation == HORIZO:
            for i in range(self.length):
                lst.append((self._location[0], self._location[1]+i))
        return lst


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
                 permitted by this car.
        """
        coor = self._location
        if self._orientation == VERTICAL:
            if coor[0] == 0:
                return {'d': VE_DICT['d']}
            elif coor[0] == 6:
                return {'u': VE_DICT['u']}
            return VE_DICT
        elif self._orientation == HORIZO:
            if coor[1] == 0:
                return {'r': HO_DICT['r']}
            elif coor[1] == 6:
                if coor[0] == 3:
                    return HO_DICT
                return {'l': HO_DICT['l']}
            return HO_DICT



    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
                 this move to be legal.
        """
        lst = []
        if movekey == DIRACT['up']:
            lst.append((self._location[0]-1, self._location[1]))
        if movekey == DIRACT['down']:
            lst.append((self.car_coordinates()[-1][0]+1,
                        self.car_coordinates()[-1][1]))
        if movekey == DIRACT['right']:
            lst.append((self.car_coordinates()[-1][0],
                        self.car_coordinates()[-1][1]+1))
        if movekey == DIRACT['left']:
            lst.append((self._location[0], self._location[1]-1))
        return lst


    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self._orientation == 0:
            if movekey == DIRECTIONS[0]:
                self._location = (self._location[0] - 1, self._location[1])
                return True
            elif movekey == DIRECTIONS[1]:
                self._location = (self._location[0] + 1, self._location[1])
                return True
            return False
        elif self._orientation == 1:
            if movekey == DIRECTIONS[2]:
                self._location = (self._location[0], self._location[1] + 1)
                return True
            elif movekey == DIRECTIONS[3]:
                self._location = (self._location[0], self._location[1] - 1)
                return True
            return False
        return False


    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name




