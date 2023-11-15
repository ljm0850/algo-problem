import sys
input = sys.stdin.readline

def solution(T:int,homeworks:list[tuple[int,int]])->int:
    check = [False]*(T+1)
    value = 0
    for final_day,point in homeworks:
        day = final_day
        while day > 0 and check[day]:
            day -= 1
        if day != 0:
            check[day] = True
            value += point
    return value

N = int(input())
homeworks = []
Day = 0
for _ in range(N):
    a,b = map(int,input().split())
    Day = max(Day,a)
    homeworks.append((a,b))
homeworks.sort(key=lambda homework:-homework[1])
ans = solution(Day,homeworks)
print(ans)