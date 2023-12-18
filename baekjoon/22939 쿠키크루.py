def short_cut(start:tuple,end:tuple,target:list[tuple])->int:
    value = 1000
    T = len(target)
    for idx in range(T):
        l = recur(T-1,target,distance(start,target[idx]),{idx},target[idx],end)
        value = min(value,l)
    return value

def recur(cur,target,length,path:set,now:tuple,end):
    if cur == 0:
        return length + distance(now,end)
    value = 1000
    for i in range(len(target)):
        if i in path:
            continue
        l = recur(cur-1,target,length+distance(now,target[i]),path|{i},target[i],end)
        value = min(l,value)
    return value


def distance(p1:tuple,p2:tuple)->int:
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


N = int(input())
topping = {'J':[],'C':[],'B':[],'W':[]}
job = {'J':'Assassin','C':'Healer','B':'Mage','W':'Tanker'}
arr = [input() for _ in range(N)]

for r in range(N):
    for c in range(N):
        alpha = arr[r][c]
        if alpha == 'X':
            continue
        if alpha == 'H':
            home = (r,c)
        elif alpha == '#':
            castle = (r,c)
        else:
            topping[alpha].append((r,c))
short_length,short_alpha = 1000,''
for alpha in topping:
    length = short_cut(home,castle,topping[alpha])
    if length < short_length:
        short_alpha = alpha
        short_length = length
print(job[short_alpha])