import sys
input = sys.stdin.readline

def FillGlobalRecord(N:int)->None:
    for num in range(10):
        record[1][num] = 1
    for i in range(2,N):
        for j in range(10):
            record[i][j] = sum(record[i-1][:j+1])
    return None

T = int(input())
arr = [int(input()) for _ in range(T)]
maximum_N = max(arr)
record = [[0]*10 for _ in range(maximum_N+2)]
FillGlobalRecord(maximum_N+2)
for num in arr:
    print(record[num+1][9])