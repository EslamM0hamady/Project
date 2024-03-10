# File : CS112_A1_T2_Game2_20230061.py
# purpose : Two players will choose number from 1 to 9, the player who choose three numbers only whose sum is 15 wins.
# Author : Eslam Mohamady Abdelmoaty Mohamady.
# ID : 20230061
print ("""*****Number scrabble game*****
Game explanation: Two players will choose number from 1 to 9, the player who choose three numbers only whose sum is 15 wins.
============================================================================================================================""")
def game():
    list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # List of numbers the player will choose number from
    score_player1 = [] # List of numbers the player 1 has been chosen
    score_player2 = [] # List of numbers the player 2 has been chosen
    player1_is_win = False # Check if player 1 is win
    player2_is_win = False # Check if player 2 is win
    while True:
        while list_of_nums != []:
            player1_choice = input(f"Player 1: Choose a number from {list_of_nums}: ")
            if player1_choice == "1" or player1_choice == "2" or player1_choice == "3" or player1_choice == "4" or player1_choice == "5" or player1_choice == "6" or player1_choice == "7" or player1_choice == "8" or player1_choice == "9": # Check if number in the numbers from 1 to 9
                if int(player1_choice) in list_of_nums: # check if number in list_of_nums or not
                    list_of_nums.remove(int(player1_choice)) # Remove the number whose player chosen from list
                    score_player1.append(int(player1_choice)) # Add number the player 1 has been chosen to List
                    print (f"List of numbers player 1 is: {score_player1}")
                    for i in range(len(score_player1) - 2): # Loop to check if sum of any three numbers in the list equal 15
                        for j in range(i + 1, len(score_player1) - 1):
                            for k in range(j + 1, len(score_player1)):
                                if score_player1[i] + score_player1[j] + score_player1[k] == 15: # if sum of any three numbers are equal 15
                                    player1_is_win = True
                    break
                else:
                    print (f"{player1_choice} not in {list_of_nums}, please try again")
            else:
                print (f"{player1_choice} not in {list_of_nums}, please try again") 
        while list_of_nums != []:     
            player2_choice = input(f"Player 2: Choose a number from {list_of_nums}: ")
            if player2_choice == "1" or player2_choice == "2" or player2_choice == "3" or player2_choice == "4" or player2_choice == "5" or player2_choice == "6" or player2_choice == "7" or player2_choice == "8" or player2_choice == "9":
                if int(player2_choice) in list_of_nums:
                    list_of_nums.remove(int(player2_choice))
                    score_player2.append(int(player2_choice)) # Add number the player 2 has been chosen to list
                    print (f"List of numbers player 2 is: {score_player2}")
                    for i in range(len(score_player2) - 2): # Loop to check if sum of any three numbers in the list equal 15
                        for j in range(i + 1, len(score_player2) - 1):
                            for k in range(j + 1, len(score_player2)):
                                if score_player2[i] + score_player2[j] + score_player2[k] == 15:
                                    player2_is_win = True
                    break
                else:
                    print (f"{player2_choice} not in {list_of_nums}, please try agin")      
            else:
                print (f"{player2_choice} not in {list_of_nums}, please try agin")
        if player1_is_win and not player2_is_win: # Check if player 1 is winer
            print ("Player 1 is winer")
            return
        elif player2_is_win and not player1_is_win: # Check if player 2 is winer
            print ("Player 2 is winer")
            return 
        elif (player2_is_win and player1_is_win) or list_of_nums == []: # Check if two players are draw
            print ("Draw")
            return
game() # To run the game
while True: # Loop for the user It tells him whether he wants to play again or not
    massage = input("Do you want play again or exit (a/e): ").lower()
    if massage == "a":
        game()
    elif massage == "e":
        break
    else:
        print ("Wrong choice, please try again")
