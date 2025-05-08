# Решение зачтено

n1, n2= map(int, input().split())

matrix = []

for _ in range(n1): # штрафы
    row = list(map(int, input().split()))
    matrix.append(row)

dp = [[0] * n2 for _ in range(n1)] # вот вам и динамическое программирование
dp[0][0] = matrix[0][0]

for j in range(1, n2):
    dp[0][j] = dp[0][j-1] + matrix[0][j]

for i in range(1, n1):
    dp[i][0] = dp[i-1][0] + matrix[i][0]

for i in range(1, n1):
    for j in range(1, n2):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

print(dp[n1-1][n2-1])