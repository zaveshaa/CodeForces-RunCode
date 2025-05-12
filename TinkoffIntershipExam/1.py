# Python-разработчик (лето 2025)
import math

n = int(input())

stations = []
for _ in range(n):
    a, b = map(int, input().split())
    stations.append((a, b))

q = int(input())

for _ in range(q):
    t, d = map(int, input().split())
    a, b = stations[t - 1]
    
    k = math.ceil((d - a) / b)
    
    next_arrival_time = a + k * b
    
    print(next_arrival_time)
    