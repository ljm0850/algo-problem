target = input().split()
A = int(target[0])
B = int(target[1])

if A > B :
    print('A')
elif B > A :
    print('B')
elif A == 3 and B ==1:
    print('B')
elif B == 3 and A ==1:
    print('A')