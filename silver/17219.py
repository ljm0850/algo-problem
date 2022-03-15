N,M =map(int,input().split())           # 100000 이하
solve= {}
for _ in range(N):
    temp=input().split()
    solve[temp[0]] = temp[1]
for _ in range(M):
    target = input()
    print(solve[target])