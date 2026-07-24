"""
Создаём простые тестовые данные: как будто у интернет-магазина
есть две группы пользователей — старая версия сайта (A) и новая (B).
Для каждого пользователя знаем только одно: купил он что-то или нет.
"""

import random
import csv

random.seed(1)

N_PER_GROUP = 1000

rows = []

# Группа A (старая версия) — покупает примерно 10 из 100
for i in range(N_PER_GROUP):
    bought = 1 if random.random() < 0.10 else 0
    rows.append(["A", bought])

# Группа B (новая версия) — покупает немного чаще, примерно 13 из 100
for i in range(N_PER_GROUP):
    bought = 1 if random.random() < 0.13 else 0
    rows.append(["B", bought])

random.shuffle(rows)

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["group", "bought"])
    writer.writerows(rows)

print("Готово: data.csv создан")
