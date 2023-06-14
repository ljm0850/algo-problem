def recur(me:int,cards:list[int],s:int,selected:list[int]):
    global ans,value
    if len(selected) == 3:
        v = sum(selected) % 10
        if value <= v:
            ans = me
            value = v
        return
    for i in range(s,5):
        recur(me,cards,i+1,selected + [cards[i]])

N = int(input())
ans,value = 0,0
for i in range(1,N+1):
    cards = list(map(int,input().split()))
    recur(i,cards,0,[])
print(ans)