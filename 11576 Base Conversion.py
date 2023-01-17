A,B = map(int,input().split())
m = int(input())
aNum = list(map(int,input().split()))
originNum = 0

for idx in range(m):
    originNum += aNum[idx] * A**(m-idx-1)
ans = []
while originNum:
    ans.append(originNum%B)
    originNum //= B
print(*ans[::-1])