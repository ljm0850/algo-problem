import datetime
time1= datetime.datetime.now()

N = int(input())
strs=[[] for _ in range(50)]
for _ in range(N):
    a=input()
    if not a in strs[len(a)-1]:
        strs[len(a)-1].append(a)

for i in strs:
    if i != []:
        i.sort()
        for ii in i:
            print(ii)
time2=datetime.datetime.now()
print(time2-time1)