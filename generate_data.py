

import random
import csv

random.seed(1)

N_PER_GROUP = 1000

rows = []

for i in range(N_PER_GROUP):
    bought = 1 if random.random() < 0.10 else 0
    rows.append(["A", bought])


for i in range(N_PER_GROUP):
    bought = 1 if random.random() < 0.13 else 0
    rows.append(["B", bought])

random.shuffle(rows)

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["group", "bought"])
    writer.writerows(rows)

print("Готово: data.csv создан")
