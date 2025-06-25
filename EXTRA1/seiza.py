seiza = {1:"水瓶",2:"魚",3:"牡羊",4:"牡牛",5:"双子",6:"蟹",7:"獅子",8:"乙女",9:"天秤",10:"蠍",11:"射手",12:"山羊"}

month = int(input("あなたの生まれた月を入力してください。:"))
day = int(input("あなたの生まれた日を入力してください。:"))


if  month == 1:
    if day > 20:
        result = seiza[1]
    else:
        result = seiza[12]
elif month == 2:
    if day > 19:
        result = seiza[2]
    else:
        result = seiza[1]
elif month == 3:
    if day > 21:
        result = seiza[3]
    else:
        result = seiza[2]
elif month == 4:
    if day > 20:
        result = seiza[4]
    else:
        result = seiza[3]
elif month == 5:
    if day > 21:
        result = seiza[5]
    else:
        result = seiza[4]
elif month == 6:
    if day > 22:
        result = seiza[6]
    else:
        result = seiza[5]
elif month == 7:
    if day > 23:
        result = seiza[7]
    else:
        result = seiza[6]
elif month == 8:
    if day > 23:
        result = seiza[8]
    else:
        result = seiza[7]
elif month == 9:
    if day > 23:
        result = seiza[9]
    else:
        result = seiza[8]
elif month == 10:
    if day > 24:
        result = seiza[10]
    else:
        seiza[9]
elif month == 11:
    if day > 23:
        result = seiza[11]
    else:
        result = seiza[10]
elif month == 12:
    if day > 22:
        result = seiza[12]
    else:
        result = seiza[13]


print(f"あなたの星座は{result}座です。")


