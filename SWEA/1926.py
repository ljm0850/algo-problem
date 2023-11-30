N = input()

for i in range(1,int(N)+1):
    three = str(i).count('3')
    six = str(i).count('6')
    nine = str(i).count('9')
    
    total = three + six + nine
    if total == 0 :
        print(i,end=' ')
    
    else:
        bar = '-'*total
        print(bar,end=" ")