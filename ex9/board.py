import car
DIRECTIONS = ['u', 'd', 'r', 'l']


class Board:
    """
    A class that makes up the game board.
    """

    def board_str(self):
        """
        A function that makes up the game board according to the
        given constraints
        :return: board
        """
        lst = []
        for i in range(7):
            if i != 3:
                lst.append(['_' for j in range(7)])
                continue
            a = ['_' for i in range(7)]
            a.append("E")
            lst.append(a)
        return lst


    def __init__(self):
        """
        A constructor for a Car object
        """
        self.cars_lst = []
        self.board = self.board_str()



    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        b = ''
        for i in self.board:
            b += (' '.join(i)) + '\n'
        return b


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst = []
        for i in range(4):
            for j in range(7):
                lst.append((i, j))
        lst.append((3, 7))
        for i in range(4, 7):
            for j in range(7):
                lst.append((i, j))
        return lst


    def __help_possible(self, movekey, car):
        """
        A function that checks if the movekey is correct
        :param movekey: Key of move in car to activate
        :param car: object of car
        :return: True upon possible. False if failed
        """
        if movekey in DIRECTIONS:
            keys = car.possible_moves().keys()
            if movekey in keys:
                return True
        return False


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        lst = []
        for c in self.cars_lst:
            move_desc = c.possible_moves()
            keys = move_desc.keys()
            for k in keys:
                if self.__help_possible(k, c) == True:
                    req = c.movement_requirements(k)[0]
                    if req in self.cell_list():
                        if req == self.target_location() or \
                                self.board[req[0]][req[1]] == '_':
                            lst.append((c.get_name(), k, move_desc[k]))
        return lst




    def target_location(self):
        """
        This function returns the coordinates of the location which is to
        be filled for victory.
        :return: (row,col) of goal location
        """
        return ((3, 7))


    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if coordinate in self.cell_list():
            row = coordinate[0]
            col = coordinate[1]
            if self.board[row][col] == '_' or self.board[row][col] == 'E':
                return None
            else:
                return self.board[row][col]


    def __help_add(self, car):
        """
         check if its possible to add a car to the game.
        :param car: car object of car to add
        :return: True upon possible. False if failed
        """
        if car.length >= 7:
            return False
        for c in self.cars_lst:
            if c.get_name() == car.get_name():
                return False
            if c._orientation not in [0, 1]:
                return False
        coordinate = car.car_coordinates()
        for coord in coordinate:
            if self.cell_content(coord) != None:
                return False
            if coord not in self.cell_list():
                return False
        return True


    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        if self.__help_add(car):
            self.cars_lst.append(car)
            lst_coordinates = car.car_coordinates()
            name = car.get_name()
            for coor in lst_coordinates:
                self.board[coor[0]][coor[1]] = name
            return True
        return False


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for c in self.cars_lst:
            car_name = c.get_name()
            if car_name == name:
                coor_lst = c.car_coordinates()
                move = c.movement_requirements(movekey)[0]
                empty = self.cell_content(move)
                if move in self.cell_list():
                    if movekey == car.DIRACT['up'] or\
                            movekey == car.DIRACT['left']:
                        clear = coor_lst[-1]
                        if empty == None:
                            self.board[clear[0]][clear[1]] = '_'
                            self.board[move[0]][move[1]] = name
                            c._location = move
                            return True
                    else:
                        clear = coor_lst[0]
                        if empty == None:
                            self.board[clear[0]][clear[1]] = '_'
                            self.board[move[0]][move[1]] = name
                            c._location = ((c._location[0], c._location[1]+1))
                            return True
                return False
        return False
