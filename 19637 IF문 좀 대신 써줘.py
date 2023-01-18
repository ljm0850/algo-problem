import sys
input = sys.stdin.readline
def findName(value:int)->str:
    s,e = 0,n-1
    while s <= e:
        mid = (s+e) // 2
        if value < arr[mid][1]:
            e = mid - 1
        elif value > arr[mid][1]:
            s = mid + 1
        else:
            return arr[mid][0]
    return arr[e+1][0]

N,M = map(int,input().split())
arr = [input().split()]
for _ in range(1,N):
    temp = input().split()
    if arr[-1][1] == temp[1]:
        continue
    arr.append(temp)
n = len(arr)
for idx in range(n):
    arr[idx][1] = int(arr[idx][1])

for _ in range(M):
    print(findName(int(input())))