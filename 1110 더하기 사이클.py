N = input()
cnt = 1
if int(N) < 10:
    N = '0'+N
num = N[-1]+str(int(N[0])+int(N[1]))[-1]

while num != N:
    if int(num) < 10:
        num = num[-1]+num[-1]
    else:
        num = num[-1]+str(int(num[0])+int(num[1]))[-1]
    cnt +=1
print(cnt)