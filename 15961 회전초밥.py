import sys
input = sys.stdin.readline
def solution(d:int,k:int,c:int,foods:list[int])->int:
    cnt_ls = [0]*(d+1)
    cnt_ls[c] += 1
    s,e = 0,0
    value = 1
    # 초기 세팅
    while e < k:
        food = foods[e]
        cnt_ls[food] += 1
        e += 1
        if cnt_ls[food] == 1:
            value += 1
    max_value = value
    
    while e < len(foods):
        removed_food = foods[s]
        new_food = foods[e]
        cnt_ls[removed_food] -= 1
        if cnt_ls[removed_food] == 0:
            value -= 1
        cnt_ls[new_food] += 1
        if cnt_ls[new_food] == 1:
            value += 1
        max_value = max(max_value,value)
        e += 1
        s += 1
    return max_value

N,d,k,c = map(int,input().split())
foods = [int(input()) for _ in range(N)]
foods = foods + foods[:k]
ans = solution(d,k,c,foods)
print(ans)