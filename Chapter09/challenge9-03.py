import csv
movie = [["Top Gun","The Revenant","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day", "Man on Fire", "Flight"]]

with open("challenge9-3.csv","w",newline="") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(movie[0])
    w.writerow(movie[1])
    w.writerow(movie[2])

