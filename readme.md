# Висновки

Результати обчислення інтегралів різними методами:

- Метод Монте-Карло дає результат, що залежить від кількості вибірок. При великій кількості вибірок результат наближається до аналітичного значення.
- Метод `quad` з бібліотеки SciPy дає дуже точний результат, який збігається з аналітичним розрахунком.

Таким чином, метод Монте-Карло є корисним для обчислення інтегралів, особливо в багатовимірних задачах, де інші методи можуть бути складними для застосування. Однак для одномірних інтегралів, таких як наш, методи на основі чисельного інтегрування, такі як `quad`, є більш точними та ефективними.

Метод Монте-Карло: 2.6582894570925837
SciPy quad: 2.666666666666667
Аналітичний розрахунок: 2.6666666666666665
Абсолютна похибка методу Монте-Карло відносно аналітичного розрахунку: 0.008377209574082833
Абсолютна похибка SciPy quad відносно аналітичного розрахунку: 4.440892098500626e-16
