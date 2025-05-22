def decimal(a):
    """
    この関数は、文字列を浮動小数点数に変換する。
    その結果を出力してプログラムに返す
    例外処理として、NameErrorとValueErrorのときにメッセージを出力してしてプログラムに返す

    引数:
    a ----必須引数
    戻り値:
    result ---引数を4でかけた(出力)結果
    """
    try:
        print("入力された文字=",a)
        print("入力された文字も小数点化した結果=",float(a))
        return a
    except ValueError:
        print("整数、または、少数点数を入力してください。")
a=str("あ")
decimal(a)
