A= int(input())
B= int(input())
C= int(input())
num = []
num.extend(str(A * B * C))

for i in range(9):
    print(num.count(f'{i}'))
