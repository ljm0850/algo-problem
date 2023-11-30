T = int(input())

for i in range(T):
    tx = input()
    
    for j in range(1,10):
        if tx[0] == tx[j]:
            if j == 1 or 2 or 3 :
                if tx[:j] == tx[j:2*j] == tx[2*j:3*j] == tx[3*j:4*j] ==tx[4*j:5*j] == tx[5*j:6*j]==tx[6*j:7*j]==tx[8*j:9*j]==tx[9*j:10*j] :
                    print(f'#{i+1} {j}')
                    break
            if j == 4 or 5 or 6 or 7 or 8 or 9 or 10:
                if tx[:j] == tx[j:2*j] == tx[2*j:3*j] :
                    print(f'#{i+1} {j}')
                    break
            

            
