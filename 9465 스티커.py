T = int(input())
for tc in range(T):
    n = int(input())
    point = [list(map(int,input().split())) for _ in range(2)]

    for i in range(1,n):
        if i == 1:
            point[0][1] += point[1][0]
            point[1][1] += point[0][0]
        else:
            point[0][i] = max(point[1][i-1],point[0][i-2],point[1][i-2])+point[0][i]
            point[1][i] = max(point[0][i-1],point[1][i-2],point[0][i-2])+point[1][i]
    print(max(point[0][-1],point[1][-1]))