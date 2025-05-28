musician={"amazarashi":["季節は次々死んでいく","アンチノミー","境界線","無題",
                        "未来になれなかったあの夜に","カシオピア係留所"],

          "平沢進":["金星","Big Brother","パレード","灰よ","地球ネコ","論理空軍",
                    "夢の島思念公園","白虎野の娘","TIMELINEの終わり"],

          "澤野弘之":["attack音D","Apple seed","K21","Call of Silence","Call your name",
                        "Baukloz","Barricades","Vogel im Kafig","The Reluctant Heroes"]
          }

print(musician)

i = input("amazarashi,平沢進,澤野弘之,のいずれかを入力してください:")

if i in musician:
    print(musician[i])
else:
    print("見つかりません。")
