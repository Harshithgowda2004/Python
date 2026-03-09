from login import login, register
from leaderboard import update_score, show_leaderboard
from games import number_guess, quiz_game, tic_tac_toe

print("1.Register")
print("2.Login")

choice = input("Choice: ")

if choice == "1":
    register()

user = login()

while user:

    print("\n--- Arcade Menu ---")
    print("1.Number Guess")
    print("2.Quiz Game")
    print("3.Tic Tac Toe")
    print("4.Leaderboard")
    print("5.Exit")

    c = input("Select: ")

    if c == "1":
        s = number_guess.play()
        update_score(user,s)

    elif c == "2":
        s = quiz_game.play()
        update_score(user,s)

    elif c == "3":
        s = tic_tac_toe.play()
        update_score(user,s)

    elif c == "4":
        show_leaderboard()

    elif c == "5":
        break