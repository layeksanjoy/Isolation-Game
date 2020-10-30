from copy import deepcopy
# Isolation Game
xlim,ylim = 3,2

class GameState:

  def __init__(self):
      #GameBoard
      self._board = [[-1] * xlim for _ in range(ylim)]
      self._board[-1][-1] = 1 
      #Current Player 
      self._parity = 0

      #Current Pointion
      self._player_location = [None,None]
      print(self._board)

  def get_legal_moves(self):
    legalMoves= []
    if self._player_location[0] == None:
      #all are posible moves
      i,j = 0,0

      while( i>= 0 and i<ylim):
        while( j>=0 and j < xlim ):
          # print(i,j)
          if(i>=0 and j < xlim and i<ylim and j >= 0 and self._board[i][j] == -1):
            legalMoves.append((i,j))
          else:
            break
          j += 1
        j = 0
        i += 1

        
    else:
      #from that position look in all direction
      posi = self._player_location[0][0]
      posj= self._player_location[0][1]
      i,j = posi,posj

      #up
      while(i>=0):
        i -= 1
        if(i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          # print("up",i,j)
          legalMoves.append((i,j))
        else:
          break
                  
      i,j = posi,posj

      #down
      while( i>=0 and j < xlim and i<ylim and j >= 0  ):
        i += 1

        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          # print("Down",i,j)
          legalMoves.append((i,j))
        else:
          break

      i,j = posi,posj

      #left
      while( i>=0 and j < xlim and i<ylim and j >= 0 ):
        j -= 1
        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          legalMoves.append((i,j))
        else:
          break

      i,j = posi,posj

      #Right
      while( i>=0 and j < xlim and i<ylim and j >= 0 ):
        j += 1
        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j]== -1):
          # print("R",i,j)
          legalMoves.append((i,j))
        else:
          break

      i,j = posi,posj

      #Diagonal S-E
      while( i>=0 and j < xlim and i<ylim and j >= 0 ):
        i += 1
        j += 1
        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          legalMoves.append((i,j))
        else:
          break
      i,j = posi,posj

      #Diagonal S-w
      while( i>=0 and j < xlim and i<ylim and j >= 0 ):
        i -= 1
        j += 1
        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          legalMoves.append((i,j))
        else:
          break

      i,j = posi,posj

      #Diagonal N-E
      while( i>=0 and j < xlim and i<ylim and j >= 0 ):
        i += 1
        j -= 1
        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          legalMoves.append((i,j))
        else:
          break

      i,j = posi,posj

      #Diagonal N-w
      while( i>=0 and j < xlim and i<ylim and j >= 0 ):
        i -= 1
        j -= 1
        if( i>=0 and j < xlim and i<ylim and j >= 0  and self._board[i][j] == -1):
          legalMoves.append((i,j))
        else:
          break
    return legalMoves

  def forecast_move(self, move):
      if move not in self.get_legal_moves():
        raise RuntimeError("Attempted forecast of illegal move")
      newBoard = deepcopy(self)
      newBoard._board[move[0]][move[1]] = 1
      newBoard._player_location[self._parity] = move
      newBoard._parity ^= 1
      return newBoard

  def _get_blank_spaces(self):
    """ Return a list of blank spaces on the board."""
    return [(x, y) for y in range(ylim) for x in range(xlim)
            if self._board[x][y] == -1]


def terminal_test(gameState):
  #get the legal moves if its empty then Return true else  False
  moves = gameState.get_legal_moves()
  if(len(moves) == 0):
    return True
  else:
    return False

def min_value(gameState):
  """ Return the value for a win (+1) if the game is over,
  otherwise return the minimum value over all legal child
  nodes.
  """
  if(terminal_test(gameState)):
    return 1
  moves = gameState.get_legal_moves()
  mi = 99999
  for i in moves:
    temp = gameState.forecast_move(i)
    v = min(mi,min_value(temp))
  return v
def max_value(gameState):
  """ Return the value for a loss (-1) if the game is over,
  otherwise return the maximum value over all legal child
  nodes.
  """
  if(terminal_test(gameState)):
    return -1
  moves = gameState.get_legal_moves()
  mi = -99999
  for i in moves:
    temp = gameState.forecast_move(i)
    v = max(mi,min_value(temp))
  return v

def minimax_decision(gameState):
  """ Return the move along a branch of the game tree that
  has the best possible value.  A move is a pair of coordinates
  in (column, row) order corresponding to a legal move for
  the searching player.
  
  You can ignore the special case of calling this function
  from a terminal state.
  """
  best_Score = -999999
  best_Move = None
  for i in gameState.get_legal_moves():
    temp = min_value(gameState.forecast_move(i))
    if(temp >best_Score):
      best_Score = temp
      best_Move = i

  return best_Move
  return max(gameState.get_legal_moves(),
          key = lambda m: min_value(gameState.forecast_move(m)))






if __name__ == "__main__":
    # This code is only executed if "gameagent.py" is the run
    # as a script (i.e., it is not run if "gameagent.py" is
    # imported as a module)
    emptyState = GameState()
    print(minimax_decision(emptyState))
    # create an instance of the object
    