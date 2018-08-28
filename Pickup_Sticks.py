player = []
AI = []
def create_bins(num_sticks):
    starting_choices = [1,2,3]
    for i in range(num_sticks):
        player.append(starting_choices)
        AI.append(starting_choices)

