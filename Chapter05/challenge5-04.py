myself={"好きな色":"緑、白","学校":"ITカレッジ沖縄"}
i=input("キーを入力してください:")
if i in myself:
    print(myself[i])
else:
    print("見つかりません。")
