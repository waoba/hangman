def hangman(word):
    wrong=0
    stages=["",\
    "______      ",\
    "      |     ",\
    "      o     ",\
    "     (|)    ",\
    "     / L     ",\
    "            "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to HANGMAN!! ")
    while wrong < len(stages)-1:
        print("\n")
        char=input("Type a character: ")
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win! ")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The word is {}".format(word))

#hangman("cat")
