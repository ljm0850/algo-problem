# n은 50이하, 들어오는 값도 길이가 50이하인 문자열 => 단순하게 구현해도 문제 없음
import sys
input = sys.stdin.readline

def solution(n:int,commands:list[list[str]])->list[int]:
    return_ls = list()
    total = list()
    for cmd,string in commands:
        if cmd == 'add':
            total.append(string)
        elif cmd == 'find':
            cnt = 0
            for name in total:
                if name.startswith(string): cnt += 1
            return_ls.append(cnt)
    return  return_ls

n = int(input())
commands = [input().split() for _ in range(n)]
ans = solution(n,commands)
print(*ans,sep='\n')