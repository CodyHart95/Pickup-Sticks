"""
Cody Hart
Pick Up Sticks
CSC 540
"""

import random
num_games = 1000
num_sticks = random.randint(10,100)
AI = []
def create_AI_bin(num_sticks):   
    AI.append([])
    for i in range(num_sticks + 1):
        AI.append([1,2,3])

def play_game(num_sticks):
    AI_turn = True
    if(random.randint(0,1) == 0):
        AI_turn = False
    sticks_left_in_game = num_sticks
    create_AI_bin(num_sticks)
    #initalize the game choices to be the size of the game
    game_choices = []
    game_choices.append(0)
    for i in range(num_sticks + 1):
        game_choices.append(-1)
    while(sticks_left_in_game > 1):       
        if(AI_turn):
            if(sticks_left_in_game == 3):
                choice = 2
                game_choices[sticks_left_in_game] = choice
                sticks_left_in_game = sticks_left_in_game - choice
            elif(sticks_left_in_game == 2):
                choice = 1
                game_choices[sticks_left_in_game] = choice
                sticks_left_in_game = sticks_left_in_game - choice
            else:
                choice = random.randint(1,len(AI[sticks_left_in_game])-1)
                game_choices[sticks_left_in_game] = AI[sticks_left_in_game][choice]
                sticks_left_in_game = sticks_left_in_game - AI[sticks_left_in_game][choice]            
            AI_turn = False
        else:
            if(sticks_left_in_game == 3):
                choice = 2
                sticks_left_in_game = sticks_left_in_game - choice
            elif(sticks_left_in_game == 2):
                choice = 1
                sticks_left_in_game = sticks_left_in_game - choice
            else:
                choice = random.randint(1,3)
                sticks_left_in_game = sticks_left_in_game - choice
            AI_turn = True
    if(AI_turn):
        return []
    else:
        return game_choices

def print_results():
    print('For a game of',num_sticks,'sticks the best moves are:')
    for i in range(num_sticks + 1):
        one = 0
        two = 0
        three = 0
        for j in range(len(AI[i])):
            if(AI[i][j] == 1):
                one = one + 1
            elif(AI[i][j] == 2):
                two = two + 1
            elif(AI[i][j] == 3):
                three = three + 1
        if(one > two and one > three):
            print("For",i,'sticks the best move is: 1')
        elif(two > one and two > three):
            print("For",i,'sticks the best move is: 2')
        elif(three > one and three > two):
            print("For",i,'sticks the best move is: 3')
            
#play the game num_games number of times to teach the AI
print("Training AI")
for i in range(num_games+1):  
    results = play_game(num_sticks)
    for j in range(len(results)-1):       
        if(results[j] > 0):
            AI[j].append(results[j])                   
print_results()
    

        
        
            
            
    
