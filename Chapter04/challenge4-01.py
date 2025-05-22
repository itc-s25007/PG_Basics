def number():
    """
    この関数は、入力された整数の二条を求めます。
    また、メッセージと求めた結果を出力します。
    """
    num=input("二乗したい数字を入力してください")
    result=int(num)**2
    print("入力された整数を二乗した結果=",result)
number()
