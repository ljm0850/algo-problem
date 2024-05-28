H,W = map(int,input().split())
blocks = list(map(int,input().split()))
arr = [[0]*W for _ in range(H)]

for c in range(W):
    block = blocks[c]
    for r in range(block):
        arr[r][c] = 1

answer = 0
for r in range(H):
    s = -1
    for c in range(W):
        if arr[r][c] == 1:
            if s == -1:
                s = c
            else:
                answer += c - s -1
                s = c
print(answer)