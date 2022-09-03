w,h = map(int,input().split())  #w = 너비, h = 높이
p,q = map(int,input().split())  #p = 개미의 x좌표, q= 개미의 y좌표
t = int(input())

xt=t%(2*w)
yt=t%(2*h)
if p + xt >w:
    if (2*w-p-xt) <0:
        p = -(2*w-p-xt)
    else:
        p = 2*w-p-xt
else:
    p = p+xt

if q + yt > h:
    if (2*h-q-yt)<0:
        q = -(2*h-q-yt)
    else:
        q = 2*h-q-yt
else:
    q = q+yt
print(p,q)