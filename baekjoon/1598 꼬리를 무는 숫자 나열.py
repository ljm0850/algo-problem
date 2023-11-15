def findRC(num:int)->tuple:
    return (num-1)//4,(num-1)%4

A,B = map(int,input().split())
Ar,Ac = findRC(A)
Br,Bc = findRC(B)
print(abs(Ar-Br)+abs(Ac-Bc))