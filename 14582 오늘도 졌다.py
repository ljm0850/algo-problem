Ateam = list(map(int,input().split()))
Bteam = list(map(int,input().split()))
Ascore,Bscore = 0,0
flag = False
for idx in range(9):
    Ascore += Ateam[idx]
    if Ascore > Bscore:
        flag = True
    Bscore += Bteam[idx]
if flag and Ascore < Bscore:
    print('Yes')
else:
    print('No')