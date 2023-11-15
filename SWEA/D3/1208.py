import sys
sys.stdin=open('input.txt')

def max_num(arr):
    maximum = arr[0]
    numberh = 0
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
            numberh = i
    return numberh

def min_num(arr):
    minimum = arr[0]
    numberl = 0
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            numberl = i
    return numberl

for tc in range(1,11):
    dump = int(input())
    box = list(map(int,input().split()))
    for i in range(dump):
        box[max_num(box)] -= 1
        box[min_num(box)] +=1
    print(f'#{tc} {box[max_num(box)]-box[min_num(box)]}')