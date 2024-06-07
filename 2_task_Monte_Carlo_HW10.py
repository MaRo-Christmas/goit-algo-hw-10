import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(func, a, b, num_samples):
    samples_x = np.random.uniform(a, b, num_samples)
    samples_y = func(samples_x)
    integral = (b - a) * np.mean(samples_y)
    return integral

# Кількість вибірок для методу Монте-Карло
num_samples = 100000
mc_result = monte_carlo_integration(f, a, b, num_samples)

# Обчислення інтеграла за допомогою SciPy
quad_result, error = spi.quad(f, a, b)

print("Інтеграл методом Монте-Карло: ", mc_result)
print("Інтеграл за допомогою SciPy quad: ", quad_result)

# Аналітичний розрахунок інтеграла
analytical_result = (b**3) / 3 - (a**3) / 3
print("Аналітичний розрахунок інтеграла: ", analytical_result)

# Висновки
conclusions = f"""
Метод Монте-Карло: {mc_result}
SciPy quad: {quad_result}
Аналітичний розрахунок: {analytical_result}
Абсолютна похибка методу Монте-Карло відносно аналітичного розрахунку: {abs(mc_result - analytical_result)}
Абсолютна похибка SciPy quad відносно аналітичного розрахунку: {abs(quad_result - analytical_result)}
"""

# Збереження висновків у файл readme.md
with open("readme.md", "w") as file:
    file.write(conclusions)

print(conclusions)
