color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
total = ''
for _ in range(3):
    t = input()
    for i in range(10):
        if color[i] == t:
            break
    if _ != 2:
        total += str(i)
    else:
        total = int(total)
        total *= 10**i
print(total)