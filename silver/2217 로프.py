N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)
ans = rope[0]
for i in range(N):
    temp = (i+1)*rope[i]
    if temp > ans:
        ans = temp
print(ans)