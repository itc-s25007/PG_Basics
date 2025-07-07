import random


kuji = ["大吉","中吉","小吉","吉","凶","大凶"]
rate = [1,100,350,500,900,1000]
min = 1
max = 1000
r = random.randint(min,max)

if r <= rate[0]:
    result = kuji[0]
if r > rate[0] and r <= rate[1]:
    result = kuji[1]
if r > rate[1] and r <= rate[2]:
    result = kuji[2]
if r > rate[2] and r <= rate[3]:
    result = kuji[3]
if r > rate[3] and r <= rate[4]:
    result = kuji[4]
if r > rate[4]:
    result = kuji[5]

print(result)
