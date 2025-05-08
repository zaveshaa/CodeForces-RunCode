# вводится массив чисел, и сумма каких то двух чисел даст таргет число

numbers = list(map(int, input().split()))
target = int(input())

sums = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        sums.append(numbers[i] + numbers[j])
# теперь осталось сдлеать проверку индекса подходящих чисел
