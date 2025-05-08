# pass
numbers = list(map(int, input().split()))
target = int(input())

sums = []

for i in range(len(numbers)):  # впринципе по всем
    for j in range(i + 1, len(numbers)):  # по повторениям
        sums.append(numbers[i] + numbers[j])  # в массив сумм добавляем все возможные
        if numbers[i] + numbers[j] == target:  # сравниваем суммы с таргетом
            print([i, j])


'''from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []''' # это для лита, но время выполнения конечно паршивое, щас будем исправлять