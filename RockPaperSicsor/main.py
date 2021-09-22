import random

def is_win (player, oponent):
        if (player == 'r' and oponent =='s') or (player == 'p' and oponent == 'r') or (player == 's' and oponent == 'p'):
            return True

def play():
    user = input(f"pick rock(r), paper (p), sciscors (s)").lower()
    computer = random.choice(["r", "s", "p"])

    if user == computer:
        return 'tie'

    if is_win(user, computer ):
        return  'you won'

    return 'you lost'




print(play())