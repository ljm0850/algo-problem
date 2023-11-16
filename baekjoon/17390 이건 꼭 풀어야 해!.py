import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
arr = sorted(map(int,input().split()))
sum_arr = [0]
total = 0
for num in arr:
    total+= num
    sum_arr.append(total)
for _ in range(Q):
    s,e = map(int,input().split())
    print(sum_arr[e]-sum_arr[s-1])