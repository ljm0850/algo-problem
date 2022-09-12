import sys
input = sys.stdin.readline
def solve(n:int)->None:
    numbers = [input() for _ in range(n)]
    numbers.sort()
    for idx in range(n-1):
        length = len(numbers[idx])
        if numbers[idx][:length-1] == numbers[idx+1][:length-1]:
            print("NO")
            break
    else:
        print("YES")

t = int(input())
for tc in range(t):
    n = int(input())
    solve(n)