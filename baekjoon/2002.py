import sys
input = sys.stdin.readline

def solution(N:int,ls1:list[str],ls2:list[str])->int:
    input_dict = dict()
    for i in range(N):
        input_dict[ls1[i]] = i

    cnt = 0
    for i in range(N):
        now_car = input_dict[ls2[i]]
        for j in range(i+1,N):
            if now_car>input_dict[ls2[j]]:
                cnt += 1
                break
    return cnt
N = int(input())
in_ls = [input().rstrip() for _ in range(N)]
out_ls = [input().rstrip() for _ in range(N)]
ans = solution(N,in_ls,out_ls)
print(ans)