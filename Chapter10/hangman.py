def hangman(word):
    wrong = 0
    stages = ["",
              " _______     ",
              "|        ",
              "|    |   ",
              "|    0   ",
              "|   /|\\  ",
              "|   / \\  ",
              "|        "
              ]
    rletters = list(word)   #プレイヤーが入力した文字をリスト化する
    board = ["_"] * len(word)  #正解の文字列と同じ数の"_"を表示する
    win = False     #正解、不正解の判定をするための変数
    print("ハングマンへようこそ")
    print(" ".join(board))

    # ループ処理開始
    while wrong < len(stages) -1: #吊るされた人のイラストがすべて表示されたら終了
        print("\n")
        msg = "１文字を予想してね"
        char= input(msg)
        #解答の文字があっているときの処理
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind]='$'
            # 解答の文字が間違っているときの処理
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

# 勝ったときの処理
        if"_"not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        # ループ終了

        # 負けたときの処理
    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("あなたの負け！正解は{}.".format(word))
#　hangman関数実行
hangman("cat")
