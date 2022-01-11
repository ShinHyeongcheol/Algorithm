N = int(input())
snack = [int(input()) for _ in range(N)]
dp = [snack[i] for i in range(N)]
cat = dp[0]
for i in range(N):
    for j in range(i):
        if snack[i] > snack[j]:
            if(dp[i] < dp[j] + snack[i]):
                dp[i] = dp[j] + snack[i]
    if(cat < dp[i]):
        cat = dp[i]
print(cat)