S,K,H = map(int,input().split())
total = S+K+H

if total >=100:
    print('OK')
else:
    if S<K and S<H :
        print('Soongsil')
    elif K<S and K<H:
        print('Korea')
    else:
        print('Hanyang')