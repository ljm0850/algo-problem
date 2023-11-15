import sys
N = int(input())

def change(ls):
    for i in ls:
        i[0],i[1]=i[1],i[0]
    return

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
change(arr)
arr.sort()
change(arr)
[print(*num) for num in arr]