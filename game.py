import random
total_user_score = 0
total_bot_score = 0
game = ["rock", "paper", "scissors"]
while True:
    games_needed_to_win = int(input(" Games Needed To Win"))
    if 0 < games_needed_to_win:
        break

print(" Pierre-papier-ciseaux. Le premier qui atteint le {", games_needed_to_win, ") est legangant !")
while total_user_score < games_needed_to_win or total_bot_score < games_needed_to_win:
    while True:

        user = int(input("1:rock 2: paper 3:scissors"))

        if 1 <= user <= 3:
            break

    bot = random.randint(1, 3)
    print("user", game[user - 1])
    print("bot", game[bot - 1])
    if (user == 1 and bot == 3) or (user == 3 and bot == 2) or (user == 2 and bot == 1):
        total_user_score += 1
    elif user == bot:
        print("draw")
    else:
        print("bot")
        total_bot_score += 1
    print("totalbot score", total_bot_score)
    print("total user score", total_user_score)
if total_bot_score > total_user_score:
    print("bot won")
else:
    print("user won")
    