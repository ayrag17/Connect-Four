#
#
# A Connect-Four Player class 
#  

from Board_Class import Board

# write your class below.

# Function 1
class Player:
    
    def __init__(self, checker):
        """constructs a new Player object by initializing two attributes
        """
        self.checker = checker
        self.num_moves = 0

# Function 2
    def __repr__(self):
        """returns a string representing a Board object.
        """
        s = 'Player ' + self.checker
        return s
    
# Function 3
    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
# Function 4
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column where the player wants to make the next move.
        """
        self.num_moves +=1
            
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')

    