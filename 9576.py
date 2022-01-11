tc = int(input())
for i in range(tc):
    cnt = 0
    N,M = map(int,input().split())
    numab = [list(map(int,input().split())) for _ in range(M)]
    numab = sorted(numab, key = lambda x : x[1])
    prize = [0 for i in range(N)]
    for i in range(M):
        for j in range(numab[i][0],numab[i][1]+1):
            if prize[j-1] == 0:
                cnt += 1
                prize[j-1] = -1
                break
    print(cnt)