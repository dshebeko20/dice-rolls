from die import Die

# Создание кубика D6

die = Die()

# Моделирование серии бросков с соханением результтатов в списке.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)