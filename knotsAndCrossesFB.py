board =["0"," "," "," "," "," "," "," "," "," "]
board_d=["","1","2","3","4","5","6","7","8","9"]

from random import randint
import random
import time ,os,sys

def dis_board(board):

    print('     |     |  ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |  ')
    print('-----------------')
    print('     |     |  ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |  ')
    print('-----------------')
    print('     |     |  ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |  ')



def print_slow(line_in):
    for x in line_in:
        # print(x, end='')
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)


def place_marker(board, marker, position):
    board[position] = marker

# place_marker(board,'t', 6 )
# dis_board(board)

def player_marker():
    marker=''
    while marker != 'X' and marker != 'O':
        
        print_slow('you chose to play against the Gods\n')
        print_slow('Choose a symbol X or O \n')
        marker= input().upper()

        if marker == 'X':
            return ('X','O')
        elif marker =='O':
            return ('O','X')
    
def who_go_first():
    print_slow('lets flip a coin to see who goes first\n')
    print_slow('The Gods or you \n')
    print_slow('You better pray to Gods they let you go first\n')

    time.sleep(2)
    marker = random.randint(1,2)
    if marker == 1:
        # print ('X goes first')
        return ('X')
        
    else:
        # print ('O goes first')
        return ('O')
        
def check_win(board,mark ):
    if (board[7] == board[8] == board [9] == mark)or(board[4] == board[5] == board [6] == mark) or(board[1] == board[2] == board [3] == mark) or(board[7] == board[5] == board [3] == mark) or(board[1] == board[5] == board [9] == mark) or (board[1] == board[4] == board [7] == mark) or (board[2] == board[5] == board [8] == mark)or (board[3] == board[6] == board [9] == mark):
        
        return True 
    else:
        return False
    
def check_used_num(board):
   
    t=0
    for i in range(len(board)):
        if board[i] != ' ':
            t+=1
            # print(f'num of used sapace{t}')
            # return(t)
        else:
            pass
            # return(t)
    return(t)

def check_full_board(board):
    
    l= check_used_num(board)

    if l ==10 :
        # print_slow('its draw')
        # print_slow('Gods Have given you another chance to live ')
        return True
    elif l<10:
        return False

def game_choice():
    print_slow('Are you ready to play: yes or no \n ')
    choice = input().lower()
    if choice == 'yes':
        return True
    else:
        return False

# def check_vacancy()


# def check_vac_position(position):
#     while position not in [1,2,3,4,5,6,7,8,9]:
#         print ('enter valid position ')
#         position =int(input())
#         if board[position]==' ':
#             return (position)
#         else:
#             check_vac_position(position)
#     return (position)
        
def check_used_position_forplayer(position):
    if board[position] ==' ':
        return True 
    # else:
    #     print_slow('Dont Anger the gods ')
    
# def check_used_position(position):
#     if check_used_num(board)<10:
#         if board[position] == ' ':
#             return True
#     elif check_used_num(board)==10:
#         return False
    # else:
    #     print_slow('Dont Anger the gods ')


def check_correct_input(position):
    while position not in [1,2,3,4,5,6,7,8,9]:
        print_slow('Enter the spot between 1-9 you want to play\n')
        position = int(input())
    return(position)



def check_comp_position(position ):
    # while check_full_board
    # if check_used_num(board)<10:
    if board[position] == ' ':
#     # position = random.randint(1,9)
        return True
    else:
        position = random.randint(1,9)
        check_comp_position(position )
    # elif check_used_num(board) == 10:
    #     return False

def check_who_won(player_1,computer ):
    if check_win(board,player_1) == True :
        print_slow('You Won\n')
        print_slow('your code to next level is XYZ')
    elif check_win(board,computer) == True :
        print_slow('Gods won  ')
        print_slow('better luck next time')
    else:
        print ('draw')



    



def game_x_o():
    i=1
    print ('Complete The Temple ')
    # game_on = game_choice()
    
    dis_board(board_d)
    player_1, computer = player_marker()  # gives out (x,o) or( o,x)
    turn = who_go_first()  # returns x or o
    print(f'{turn} Goes First ')
    i = 0
    game_on = game_choice()
    
    while game_on is True:
        while i <= 9:
            if turn == player_1:    
                position1 = 0
                position=check_correct_input(position1)
                # while check_full_board(board):
                
                    # print('pick a spot between 1 to 9 ')
                    # position = int(input())
                while check_used_position_forplayer(position):
                    place_marker(board, player_1, position)
                    w_or_l = check_win(board, player_1)
                    full_board=check_full_board(board)
                    # if w_or_l == True:
                    #     dis_board(board)
                    #     print(f'{ player_1} Has won')
                    #     game_on = False
                    #     break

                    if w_or_l == False and full_board == True:
                         time.sleep(1)
                         dis_board(board)
                         print('Its Draw')
                         game_on= False
                         break

                    elif w_or_l == True:
                        time.sleep(1)
                        dis_board(board)
                        print(f'{ player_1} Has won')
                        game_on = False
                        break
            


                    else:
                        i += 1
                        # check_full_board(board)
                        time.sleep(1)
                        dis_board(board)
                        
                        turn = computer
                        print ("its God's turn")
                        game_on = True
                    # break       
                # game_on == False
            elif turn == computer:
               

                
              
                # print ("its God's turn")
                
                position1 = random.randint(1,9)
                # while check_full_board(board):
                
                while check_comp_position(position1):
                   
                # position= (check_comp_position(position1))

                    # position = random.randint(1,9)
                
                    place_marker(board, computer, position1)

                    time.sleep(1)
                    w_or_l = check_win(board, computer)
                    full_board=check_full_board(board)

                    if w_or_l == False and full_board == True:
                         time.sleep(1)
                         dis_board(board)
                         print('Its Draw')
                         game_on= False
                         break

                    elif w_or_l == True:
                        time.sleep(1)
                        dis_board(board)
                        print(f'{computer} Has won')
                        game_on = False
                        break

                    else:
                        time.sleep(1)
                        dis_board(board)
                        i += 1
                        turn = player_1
                        game_on = True
                    # break 
                # game_on==False       
            break
    check_who_won(player_1, computer)
    time.sleep(1)
    print_slow('\n Game over ')    
    #make condition for match

            # check_win(board,computer)
            # dis_board(board)
            # i+=1
            # turn=player_1
        

game_x_o()








