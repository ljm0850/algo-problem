# r = 31
M = 1234567891
L = int(input())
target = input()
total = 0
for i in range(L):
    total += ((ord(target[i])-96) * (31**i)) % M
print(total % M)