# p138

# hangman game sort
# player2

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    
    rletters = list(word) 
    board = ["__"] * len(word)
    win = False

    print("Welcome to Hangman")
    print("player2")

    # game Winning or losing Keep turning
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter : "
        char = input(msg)
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            # wordに同じ文字がある場合、’$記号’に変換することで、
            # 同じ値を新たにindexメソッドで値を返してくれる
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        # format関数表示させる
        print("You lose! It was {}.".format(word))


