import random
num_games = 2
num_sticks = 10
random.seed(1)
AI = []
def create_AI_bin(num_sticks):
    starting_choices = [1,2,3]
    AI.append([])
    for i in range(num_sticks + 1):
        AI.append(starting_choices)

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
    print(game_choices)
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
            print(i,': 1')
        elif(two > one and two > three):
            print(i,': 2')
        elif(three > one and three > two):
            print(i,': 3')
        else:
            print("no optimal move")
    #print(one,two,three)                 
#play the game num_games number of times to teach the AI
print("Training AI")
for i in range(num_games):  
    results = play_game(num_sticks)
    #Sprint(results)
    for j in range(len(results)):
        if(results[j] > 0):
            AI[i].append(results[j])
            
    #print(AI)                
print_results()
    

        
        
            
            
    
