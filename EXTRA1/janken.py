import random


#try:
while True: # ループ開始
    Phand = int(input("どの手を出しますか？(1:グー2:チョキ3:パー)")) # プレイヤーの出し手
    CPhand = random.randint(1,3) # CPの出し手
    
    # あいこの処理
    if Phand == CPhand:
        result = ("あいこ！")
   #プレイヤーの出し手がグーの時の処理
    elif Phand == 1:
        if CPhand == 2:
            result = "あなたの勝ち！"
        elif CPhand == 3:
            result = "あなたの負け！"
        #プレイヤーの出し手がチョキの時の処理
    elif Phand == 2:
        if CPhand == 1:
            result = "あなたの負け！"
        elif CPhand == 3:
            result = "あなたの勝ち！"
       #プレイヤーの出し手がパーの時の処理
    elif Phand == 3:
        if CPhand == 1:
            result = "あなたの勝ち！"
        elif CPhand == 2:
            result == "あなたの負け！"
        #じゃんけんを終了する時の処理
    elif Phand == 0:
        break


    #結果を表示
    print("あなたの手:{}コンピュータの手:{}".format(Phand,CPhand))
    print("{}".format(result))


#except(ValueError, NameError):
#    print("じゃんけんの手は'1,2,3'のどれかを入力してください。")
