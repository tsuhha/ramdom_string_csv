import csv
import random, string


def randomstr(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

file = open('random.csv', 'w')
w = csv.writer(file)
for i in range(1, 10000):
    w.writerow([randomstr(8)])

file.close()
