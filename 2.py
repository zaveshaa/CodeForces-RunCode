def solution(tasks):
    tasks.sort()
    total_time = 0
    count = 0
    for time in tasks:
        if total_time + time <= 480:
            total_time += time
            count += 1
        else:
            break
    return count