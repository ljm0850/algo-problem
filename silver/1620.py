import sys

N,M = map(int,sys.stdin.readline().split())      #100000 이하
poke1=[0]
poke2={}
for i in range(1,N+1):
    temp = sys.stdin.readline().rstrip()
    poke1.append(temp)
    poke2[temp] = i

for j in range(M):
    cmd=sys.stdin.readline().rstrip()
    if cmd.isdigit():
        print(poke1[int(cmd)])
    else:
        print(poke2[cmd])