
import csv
import matplotlib.pyplot as plt

data = {"A": [], "B": []}

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        group = row["group"]
        bought = int(row["bought"])
        data[group].append(bought)

results = {}
for group, values in data.items():
    total = len(values)
    bought = sum(values)
    conversion = bought / total * 100
    results[group] = conversion
    print(f"Группа {group}: {bought} из {total} купили ({conversion:.1f}%)")

diff = results["B"] - results["A"]
print(f"\nРазница между B и A: {diff:.1f} процентных пункта")

if diff > 0:
    print("Вывод: у группы B (новая версия) конверсия выше. "
          "Новая версия выглядит лучше.")
elif diff < 0:
    print("Вывод: у группы A (старая версия) конверсия выше. "
          "Новая версия выглядит хуже.")
else:
    print("Вывод: разницы нет.")


groups = list(results.keys())
values = list(results.values())

plt.figure(figsize=(5, 4))
bars = plt.bar(groups, values, color=["#999999", "#4477cc"])
plt.ylabel("Конверсия, %")
plt.title("Сравнение конверсии: старая (A) vs новая (B) версия")

for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, value + 0.2,
              f"{value:.1f}%", ha="center")

plt.tight_layout()
plt.savefig("result.png", dpi=150)
print("\nГрафик сохранён -> result.png")
