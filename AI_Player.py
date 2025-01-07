#
#
# AI Player for use in Connect Four  
#

import random  
from Playing_the_game import *

class AIPlayer(Player):
    
    #Function 1
    def __init__(self, checker, tiebreak, lookahead):
        """ constructor for AIPlayer that constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    # Function 2
    def __repr__(self):
        """returns a string representing an AIPlayer object. This method will override/replace the __repr__ method that is inherited from Player.
        """
        if self.checker == 'X':
            s = 'Player X ' + '('+ str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
            return s
        else:
            s = 'Player O ' + '('+ str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
            return s

    # Function 3
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score.
        """
        max_score = max(scores)
        max_ind = []
        for x in range(len(scores)):
            if scores[x] == max_score:
                max_ind += [x]
        
        if self.tiebreak == 'RIGHT':
            return max_ind[-1]
        elif self.tiebreak == 'LEFT':
            return max_ind[0]
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_ind)
        
    # Function 4    
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores for the columns in b. Each column should be assigned one of the four possible scores discussed in the Overview at the start of this problem, based on the called AIPlayer‘s lookahead value.
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                scores[col] = 100 - max(opp_scores)
                b.remove_checker(col)
        return scores
    
    # Function 5   
    def next_move(self, b):
        """this version of next_move should return the called AIPlayer‘s judgment of its best possible move.
        """
        scores = self.scores_for(b)
        max_col = self.max_score_column(scores)
        self.num_moves += 1
        return max_col
    
    
    
    
    
    