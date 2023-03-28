import sys
input = sys.stdin.readline

def findSize(num:int,arr:list[int])->int:
    s,e = 0,len(arr) - 1
    res = -1
    while s <= e:
        m = (s+e) // 2
        if num > arr[m]:
            s = m + 1
            res = m
        else:
            e = m - 1
    return res

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = sorted(list(map(int,input().split())))
    value = 0
    for num in A:
        value += findSize(num,B) + 1
    print(value)