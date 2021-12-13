CARS = ['Y', 'B', 'O', 'W', 'G', 'R']
ERROR = 'The move is not possible.'
END = '!'
WIN = 'You won'
import board
import car
import sys
import helper


class Game:
    """
    A class that produces the game object and uses the car and board objects.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board
        self.dictenari = helper.load_json(sys.argv[1])


    def __check_input(self, user_input):
        """
        A function that checks whether the user's input is correct
        :param user_input: user input car name and direction
        :return: True upon possible. False if failed
        """
        if user_input == '!':
            return [True]
        if len(user_input) != 3:
            return [False]
        name = user_input[0]
        direction = user_input[2]
        if name in CARS:
            if direction in car.DIRECTIONS:
                lst = self.board.possible_moves()
                lst2 = []
                for i in range(len(lst)):
                    lst2.append(lst[i][1])
                    if direction in lst2:
                        return [True, name, direction]
        return [False]


    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        """
        print(self.board)
        print(self.board.possible_moves())
        user_input = input('Enter the car color and direction ')
        check = self.__check_input(user_input)
        if check[0] == True:
            if user_input != '!':
                self.board.move_car(check[1], check[2])
            return user_input
        if check[0] == False:
            print(ERROR)

            
    def __check_args(self):
        """
        A function that checks if the json file is correct
        :return: True upon possible. False if failed
        """
        lst1 = []
        dicr = self.dictenari
        if type(dicr) == dict:
            for k in dicr.keys():
                if k in CARS:
                    lst = dicr[k]
                    length = lst[0]
                    coordinate = tuple(lst[1])
                    orientation = lst[2]
                    if length in range(2, 5):
                        if coordinate in board.cell_list():
                            if orientation in [car.HORIZO, car.VERTICAL]:
                                carToAdd = car.Car(k, length, coordinate,
                                                   orientation)
                                flag = True
                                for cord in carToAdd.car_coordinates():
                                    if cord not in board.cell_list():
                                        flag = False
                                if flag:
                                    lst1.append(carToAdd)
        return lst1



    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        tar = self.board.target_location()
        lst = self.__check_args()
        for c in lst:
            if tar in c.car_coordinates():
                print(WIN)
                return
            self.board.add_car(c)
        user_input = self.__single_turn()
        while user_input != END and self.board.board[tar[0]][tar[1]] == 'E':
            user_input = self.__single_turn()
        if user_input == '!':
            return
        print(self.board)
        print(WIN)


if __name__== "__main__":
    board = board.Board()
    game = Game(board)
    game.play()

