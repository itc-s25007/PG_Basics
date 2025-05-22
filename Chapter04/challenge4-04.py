def division(a):
    """
    この関数は、整数を引数として受け取り、その整数を2で割る。
    その結果を出力してプログラムに返す。

    引数:
    a ----必須引数
    戻り値:
    result ---引数を2で割った(出力)結果
    """
    result1=a/2
    print("入力された整数を2で割った結果=",int(result1))
    return result1
    
def multiplication(b):
    """
    この関数は、整数を引数として受け取り、その整数を4でかける。
    その結果を出力してプログラムに返す。

    引数:
    b---必須引数
    戻り値
    result--- 引数を4でかけた（出力）結果
    """
    result=b*4
    print("入力された整数を4でかけた結果=",int(result))
    return result
a=6
b=division(a)
multiplication(b)
