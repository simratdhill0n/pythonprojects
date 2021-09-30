#function for players to choose either X or O.


def player_choices():
    marker=''
    
    while marker != 'X' and marker != 'O':
        
        marker= input('Player 1, Select between X and O: ').upper()
        
        if marker != 'X' and marker != 'O':
            
            print ('Invalid Input!')
    
    if marker== 'X':
        
        return ('X','O')
    
    if marker== 'O':
        
        return ('O','X')

#function to randomly choose, who would go first.

from random import randint
    
def choose_first():
    
    if randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'

# function to display the board.

def theboard(board):
    
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])
 
#function to check empty spaces.

def space_check(board,choice):
    
    return board[choice]==' '
    
#function taking player's input.

def player_choice(board):
    
    choice= 0 
    
    while choice not in range(1,10) or not space_check(board,choice):
        
        return int(input('Choose your position from 1 to 9: '))
        
# function to place marker on of the player on the selected position, he want to.

def place_marker(board,marker,position):
    board[position]=marker

#function to check the winner.

def win_check(board,marker):
    
    return ((board[1]==board[2]==board[3]==marker)or
            (board[4]==board[5]==board[6]==marker)or
            (board[7]==board[8]==board[9]==marker)or
            (board[1]==board[4]==board[7]==marker)or
            (board[2]==board[5]==board[8]==marker)or
            (board[3]==board[6]==board[9]==marker)or
            (board[1]==board[5]==board[9]==marker)or
            (board[3]==board[5]==board[7]==marker))

#function to check the board is full or not.

def full_board(board):
    
    for i in range(1,10):
        if board[i]== ' ':
            return False
    
    return True

#function asking players to replay the game.

def replay():
    
    choice= input('Do you want to play again? Yes or No: ').lower()
    
    return choice == 'yes'

print('WELCOME TO TICK TACK TOE GAME!')

while True:
    
    board=[' ']*10
    
    player1_choice, player2_choice = player_choices()
    
    turn= choose_first()
    
    ready= input('Are you ready? y for yes and n for no: ').lower()
    
    if ready=='y':
        
        game_on=True
    
    elif ready=='n':
        
        game_on=False
        break
    
    else:
        
        print('Invalid Input!')
    
    while game_on:
        
        if turn== 'Player 1':
            
            theboard(board)
        
            print("Player 1's turn!")
            
            position= player_choice(board)
            
            place_marker(board,player1_choice,position)
            
            if win_check(board,player1_choice):
                theboard(board)
                print('Player 1 won')
                game_on=False
            
            else:
                if full_board(board)==True:
                    theboard(board)
                    print('Tie Game!')
                    game_on=False
                else:
                    turn= 'Player 2'
        
        else:
            
            theboard(board)
        
            print("Player 2's turn!")
            
            position= player_choice(board)
            
            place_marker(board,player2_choice,position)
            
            if win_check(board,player2_choice):
                theboard(board)
                print('Player 2 won')
                game_on=False
            else:
                if full_board(board)== True:
                    theboard(board)
                    print('Tie Game!')
                    game_on=False
                else:
                    turn= 'Player 1'
    if not replay():
        
        break