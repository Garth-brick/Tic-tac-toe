# I still need to make a 1 player mode

import os
from time import sleep
import sys
from itertools import cycle


def cleanup(): # this function will clear the output and only print the title after that
    os.system('cls')
    print("T I C   T A C   T O E\n\n")


def clear2(): # this function will clear the output and also print the title and instructions to keep playing the game after every move
    os.system('cls')
    print("""T I C   T A C   T O E\n\n\nHere is what the grid looks like:\n
\t 1 | 2 | 3  # on hind-sight, I could make a for loop for printint the board instead, like I did for my Othello game later
\t---+---+---
\t 4 | 5 | 6
\t---+---+---
\t 7 | 8 | 9 \n""")


def check_win(board):
    winner = 0
    for i in range(3): # I could make a for loop to go through thise scenarios and check for wins as well
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == 1 or board[i][0] == 2:
                winner = board[i][0]
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[i][0] == 1 or board[i][0] == 2:
                winner = board[0][i]
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[i][0] == 1 or board[i][0] == 2:
                winner = board[1][1]
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[i][0] == 1 or board[i][0] == 2:
                winner = board[1][1]
    return winner


def letsgo():
    global ties_wins
    board = [[0 for i in range(3)] for i in range(3)] # board=[[0]*3]*3 led to glitch because of shallow copying
    play = 0
    symbols = {0: " ", 1: "X", 2: "O"}
    turn_num = 0
    win = 0
    for i in cycle((1, 2)):
        moved = False
        while not moved and turn_num != 9 and win == 0:
            clear2()
            print(f"Now, player-{i}, make your move:")
            print(f"""
\t {symbols[board[0][0]]} | {symbols[board[0][1]]} | {symbols[board[0][2]]}
\t---+---+---
\t {symbols[board[1][0]]} | {symbols[board[1][1]]} | {symbols[board[1][2]]}
\t---+---+---
\t {symbols[board[2][0]]} | {symbols[board[2][1]]} | {symbols[board[2][2]]} \n""")
            play = input()
            if str(play) in "123456789" and not(str(play) == ""): # ask for input until valid input is given
                if int(play) < 10 and int(play) > 0:
                    if board[(int(play)-1)//3][(int(play)-1) % 3] == 0:
                        board[(int(play)-1)//3][(int(play)-1) % 3] = i
                        # print(board)
                        turn_num = turn_num+1
                        # print("Turn: "+str(turn_num))
                        moved = True
                        # sleep(2)
                    else:
                        print("Sorry, but that spot is already filled.")
                        sleep(1.5)
                else:
                    print("The input must be between 1 and 9, both included.")
                    sleep(1.5)
            else:
                print("\n"+str(type(play)))
                print("Please input a valid integer")
                sleep(1.5)
            win = check_win(board)
            if turn_num == 9 or win != 0:
                cleanup()
                print(f"""The final board:\n
\t {symbols[board[0][0]]} | {symbols[board[0][1]]} | {symbols[board[0][2]]}
\t---+---+---
\t {symbols[board[1][0]]} | {symbols[board[1][1]]} | {symbols[board[1][2]]}
\t---+---+---
\t {symbols[board[2][0]]} | {symbols[board[2][1]]} | {symbols[board[2][2]]} \n""")
                if win == 0:
                    print("\tIt's a tie!")
                    ties_wins[0] += 1
                else:
                    print(f"Player-{win} wins!")
                    ties_wins[win] += 1
                print(f"\nScore: {ties_wins[1]} - {ties_wins[2]}")
                print(f"Ties: {ties_wins[0]}")
                break
        if win != 0 or turn_num == 9:
            break
    while True:
        again = input("\nWould you like to play again?\n(A) Yes    (B) No\n") # ask for input until valid input is given
        if again.lower() == "a" or again.lower() == "yes":
            cleanup()
            print("Let's play again then!")
            sleep(1.5)
            letsgo()
            break
        elif again.lower() == "b" or again.lower() == "no":
            print("")
            if ties_wins[1] > ties_wins[2]:
                print("Player-1 won the set!")
            elif ties_wins[1] < ties_wins[2]:
                print("Player-2 won this set!")
            else:
                print("This set has ended in a tie.")
            print("Hope to see you again soon!\n")
            break
        else:
            print("Invalid response, there are only two options.")


 # START OF CODE EXECUTION
cleanup()

while True:
    print("How many players?\n(A) 1\t(B) 2") # 
    players = input()
    if str(players) in "bB2":
        cleanup()
        print("Let's get started then! Each player just has to type the number corresponding to the position where they wish to make their mark.", end="")
        sys.stdout.flush()
        for i in range(5):
            print(".", end="")
            sleep(1)
            sys.stdout.flush()
        ties_wins = [0, 0, 0]
        letsgo()
        break
    else:
        cleanup()
        print("We only have 2 a player game right now, sorry for the inconvenience.")
