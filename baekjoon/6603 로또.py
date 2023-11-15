import sys

def solve(start,cur,path):
    if cur == 5:
        print(*path)
        return
    for i in range(start+1,len(target)):
        solve(i,cur+1,path+[target[i]])

while True:
    target = list(map(int,sys.stdin.readline().split()))
    if target == [0]:
        break
    target = target[1:]
    for i in range(len(target)-4):
        solve(i,0,[target[i]])
    print()
