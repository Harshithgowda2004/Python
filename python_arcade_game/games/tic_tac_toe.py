def play():

    board = [" "] * 9
    player = "X"

    for turn in range(9):
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])

        pos = int(input("Choose position 1-9: ")) - 1

        if board[pos] == " ":
            board[pos] = player
            player = "O" if player == "X" else "X"
        else:
            print("Already taken")

    return 15