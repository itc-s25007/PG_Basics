def FLOAT(a):
    """
    この関数は、文字列をfloat型に変換して、入力された文字列とfloat型に変換した結果を出力してプログラムに返す。
    例外処理として、NameErrorとValueErrorの時にメッセージを出力してプログラムに返す。
    引数:a---必須引数
    """
try:

    a=str("Hello, World")
    print("入力された文字列=",a)
    print("float型に変換した結果=",float(a))
except (ValueError,NameError):
    print("整数か浮動小数点数を入力してください")

FLOAT(a)
