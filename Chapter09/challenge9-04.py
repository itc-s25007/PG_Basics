import csv
movie = [["トップガン","リスキービジネス","マイノリティーレポート"],["タイタニック","レヴェナント","インセプション"],["トレーニングデイ","マイ・ボディガード","ファイト"]]

with open("challenge9-4.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f,delimiter=",")
    for movies in movie:
        w.writerow(movies)
