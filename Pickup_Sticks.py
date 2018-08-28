import random
num_games = 1000
AI = []
def create_AI_bin(num_sticks):
    starting_choices = [1,2,3]
    AI.append([1,2])
    for i in range(num_sticks):
        AI.append(starting_choices)

def play_game(num_sticks):
    AI_turn = True
    if(random.randint(0,1) == 0):
        AI_turn = False
    sticks_left_in_game = num_sticks
    create_AI_bin(num_sticks)
    game_choices = []
    #initalize the game choices to be the size of the game
    for i in range(num_sticks):
        game_choices.append(0)
    
    while(sticks_left_in_game > 0):
        if(AI_turn):
            choice = random.randint(0,len(AI[sticks_left_in_game]))
            game_choices[sticks_left_in_game] = AI[sticks_left_in_game][choice]
            sticks_left_in_game = sticks_left_in_game - AI[sticks_left_in_game][choice]
        else:
            choice = random.randint(1,3)
            sticks_left_in_game = sticks_left_in_game - choice
    if(AI_turn):
        return []
    else:
        return game_choices


        
        
            
            
    
