num = [71,31,47,89]

while True:
    answer = input("数字を入力してください。終了はq:")
    
    if answer == "q":
        break

    try:
        answer = int(answer)

        if answer in num:
            print("正解")
            print(num)
        else:
            print("不正解")
    except ValueError:
        print("数字を入力するか、qで終了します")
