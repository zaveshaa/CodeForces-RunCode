def solution(nums, N):
    num_set = set(nums)
    missing = []
    for i in range(1, N + 1):
        if i not in num_set:
            missing.append(i)
    return missing