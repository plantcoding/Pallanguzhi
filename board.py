import copy
#board class
#contains the size of the board and a list of pits

class board:
    def __init__(self, board_size, pit_count):
        self.board_list = [pit_count] * board_size
        self.board_size = board_size
        self.pit_count = pit_count

    def printBoard(self):
        '''
        prints board
        '''
        
        size = self.board_size/2
        new_list = self.board_list[::-1]
        print '|'.join( [str(pit) for pit in new_list[size:] ] )
        print '|'.join( [str(pit) for pit in self.board_list[size:] ] )
        
    def isHalfEmpty(self):
        '''
        checks if one size of the board is empty or not
        useful in determining if the game is over or not
        '''

        #check if any one side of the board leaves the player with no option to choose from
        return self.generateOptions(0) == [] or self.generateOptions(1) == []
        

    def clone(self):
        '''
        clones the original board
        '''
        
        new = board(len(self.board_list),self.pit_count)
        new.board_list = copy.copy(self.board_list)
        return new
    
    def generateOptions(self, current_player):
        '''
        returns a list of indices the current player is eligable to choose from
        the half the board returned represnts the side of the current player
        '''
        
        selection = []
        side = []
        size = len(self.board_list)/2

        if current_player == 0:
            for index in xrange(0,size):
                if self.board_list[index] != 0:
                    selection.append(index)
        else:
            for index in xrange(size,size*2):
                if self.board_list[index] != 0:
                    selection.append(index)
            
        return selection
                

    def nextPit(self, pit):
        return (pit + 1) % self.board_size
    
    def move(self,start, isCloneMove = False):
        '''
        the game is played beginning from the start index
        the move ends when there the next pit is empty
        the move function returns a score
        '''

        #print the board before starting a move
        if isCloneMove ==False:
            print "BOARD"
            self.printBoard()
            print "\n"

        

        #scores, get coins to move around and set the start pit to zero coins
        score = 0
        coins = self.board_list[start]
        self.board_list[start] = 0

        #move the coins to corresponding pits
        for coin in xrange(coins):
            start = self.nextPit(start)
            self.board_list[start] = self.board_list[start] + 1            

        next_pit = self.nextPit(start)


        #check if next pit after the move is empty or not
        #if empty the move is over, take the coin from the consecutive pit to return as score
        #if not empty, recursively move again starting from the next pit
        if self.board_list[next_pit] == 0:
            score_pit = self.nextPit(next_pit)
            score = self.board_list[score_pit]

            if isCloneMove == False:
                print "BOARD"
                self.printBoard()
                print "\n"
            
            self.board_list[score_pit] = 0
        
        else:
            score = self.move(next_pit, True)

        return score




            

'''          
b = board(4,2)
b.board_list = [2,2,2,2]
print b.move(0)
'''






