#game class
#contains a board and a list of players
import board
from random import randint
depth = 0

class game:
   def __init__(self, board_size, pit_count):
       self.game_board = board.board(board_size, pit_count)
       self.player_score = [0,0]
       self.current_player = 0


   def switchPlayer(self):
      '''
      moves to the next player
      '''
      self.current_player = (self.current_player + 1)% 2

      
   def updateScore(self,score):
      '''
      update scores of the current player
      '''
      
      self.player_score[self.current_player] = self.player_score[self.current_player] + score
      

   def isGame(self):
      '''
      returns True is the game has not reached the end
      returns False otherwise
      '''
      if self.game_board.isHalfEmpty():
         return False
      else:
         return True

   def getCurrentWinner(self):
      '''
      get who leads currently
      this method will return the winning player once called after the game is over
      '''
      return max(xrange(2), key=self.player_score.__getitem__)
      
   def Naiveplay1(self):
      '''
      play the game
      heuristics: select the first non-empty pit
      '''
               
      #choosing a pit
      pit = self.game_board.generateOptions(self.current_player)[0]

      #make moves and update score   
      score = self.game_board.move(pit)
      self.updateScore(score)
      self.switchPlayer()


      
   def Naiveplay2(self):
      '''
      play the game
      heuristics: select a random pit 
      '''
      
      #choosing a pit
      pits = self.game_board.generateOptions(self.current_player)
      pit = pits[randint(0, len(pits))]

      #make moves and update score   
      score = self.game_board.move(pit)
      self.updateScore(score)
      self.switchPlayer()


   def greedyPlay(self):
      '''
      plays the game
      heuristics: look ahead for one step and select the move with maximum score
      '''
   
      #choosing a pit
      max_score = float("-inf")
      max_move = 0
      moves = board.generateOptions(player)

      for move_option in moves:
         new_board = board.clone()
         new_board_score = new_board.move(move_option)
         if new_board_score > max_score:
            max_score = new_board_score
            max_move = move_option
               
      pit = max_move
      #make moves and update score   
      score = self.game_board.move(pit)
      self.updateScore(score)
      self.switchPlayer()


   def ModifiedMinMax(self, board, limit, player, checker = 0):
      global depth
      depth = depth + 1
      '''
      a recursive min-max function
      the function changes min/max utility based on the player passed
      the algorithm is modified such that the selection is made based on maximizing one score and minimizing a different score at each step
      '''

      #if the board is half empty the game is over 
      if board.isHalfEmpty():
         return 0

      max_score = float("-inf")
      max_move = 0
      moves = board.generateOptions(player)
      isCloneMove = True


      #check if the game state is in the level just above the limit in the min max tree
      #only check for maximum profit of the current player and return the best move
      if ((depth == (limit - 1)) or ((depth == limit) and (limit == 1))):
         for move_option in moves:         
            
            new_board = board.clone()
            new_board_score = new_board.move(move_option, isCloneMove)
                      
            if new_board_score > max_score:
               max_score = new_board_score
               max_move = move_option       

      #on any depth other than limit - 1 recursively call the function and get the best score of the opponent in the resulting stage of the current move
      #calculate the ratio of the addition to current player score by the move, to best potential addition to the opponent score of the resulting game state by the move
      #choose the move with maximum ratio
      else:
         max_ratio = float("-inf")
         for move_option in moves:
            new_board = board.clone()
            new_player = (player + 1) % 2
            score = new_board.move(move_option, isCloneMove)
            opponent_score = self.ModifiedMinMax(new_board, limit, new_player, depth)

            if opponent_score != 0:
               if float(score/opponent_score) > max_ratio:
                  max_score = score
                  max_ratio = float(score/opponent_score)
                  max_move = move_option
            else:
                  max_score = score
                  max_move = move_option

      if checker == 1:
            return max_move
      else:
            return max_score         
                  
   def MinMaxplay(self, limit):
      '''
      plays the game based on modified min max strategy
      since the entire tree traversal is not optimal, a depth limit is provided
      '''
      global depth
      
      #choosing a pit
      pit = self.ModifiedMinMax(self.game_board, limit, self.current_player, 1)
      depth = depth - 1
      #make moves and update score
      score = self.game_board.move(pit)
      self.updateScore(score)
      self.switchPlayer()


   def Play(self):
      '''
      play the game until a end of game game state is reached
      By default I choose Min Max strategy for Player 0 and Naive Strategy I for Player 1
      By default the limit of the min max is set to 3
      '''

      while self.isGame():
         if self.current_player == 0:
            self.MinMaxplay(2)
         else:
            self.Naiveplay1()

      #print board
      self.printGame()
      
   def printGame(self):
      '''
      this function prints the game on the command line
      the function is used for debugging purpose
      '''

      print "Final Board:"
      self.game_board.printBoard()
      print "\n"
      print "Scores:"
      print str(self.player_score[0]) + ", " + str(self.player_score[1])

      
   def __main__(self):
      print "Player 0: Computer with Min Max Strategy"
      print "Player 1: Compter with Naive Stategy"
      self.Play()
      print "Winning Player~"
      print "Player ", self.getCurrentWinner()

      
newgame = game(12, 5)
newgame.__main__()




