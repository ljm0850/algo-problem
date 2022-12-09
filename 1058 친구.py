def solve(N:int,arr:list[str])->int:
    value = 0
    for i in range(N):
        friend = 0
        for j in range(N):
            if i == j:
                continue
            elif arr[i][j] == 'Y':
                friend += 1
            else:
                for k in range(N):
                    if k==i or k==j:
                        continue
                    if arr[i][k] == 'Y' and arr[j][k] == 'Y':
                        friend += 1
                        break
        value = max(value,friend)
    return value

N = int(input())
arr = [input() for _ in range(N)]
ans = solve(N,arr)
print(ans)