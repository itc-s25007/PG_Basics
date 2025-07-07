import random

kuji = ["大吉","中吉","小吉","吉","凶"]
rate = [0,150,400,550,950,1000]
r = random.randint(1,1000)

for i in range(0,6):
    if r>rate[i] and r<=rate[i+1]:
        result = kuji[i]

print(result)
