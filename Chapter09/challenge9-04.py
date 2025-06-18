import csv
movie = [["トップガン","リスキービジネス","マイノリティーレポート"],["タイタニック","レヴェナント","インセプション"],["トレーニングデイ","マイ・ボディガード","ファイト"]]

with open("challenge9-4.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(movie[0])
    w.writerow(movie[1])
    w.writerow(movie[2])

