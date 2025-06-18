import csv
movie = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day", "Man on Fire", "Flight"]]

with open("challenge9-3.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    for movies in movie:
        w.writerow(movies)
