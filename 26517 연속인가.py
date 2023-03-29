k = int(input())
a,b,c,d = map(int,input().split())
left = a*k+b
right = c*k+d
if left == right:
    print(f'Yes {right}')
else:
    print("No")