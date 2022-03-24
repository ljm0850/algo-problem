N = int(input())
P = list(map(int,input().split()))          # N,P 1000이하
P.sort()
total = 0
for i in range(N):
    total += (N-i)*P[i]
print(total)