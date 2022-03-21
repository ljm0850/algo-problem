T = int(input())                # 100이하
for tc in range(T):
    n = int(input())            # 의상수 30이하
    clothing = [input().split() for _ in range(n)]
    cloth_index = {}
    for i in clothing:
        if cloth_index.get(i[1]):
            cloth_index[i[1]] += 1
        else:
            cloth_index[i[1]] = 1
    temp = cloth_index.values()
    total = 1
    for j in temp:
        total *= (j+1)           # 선택의 개수, ex)a가 2개면 a1,a2,선택x로 3가지
    total -= 1                  # 모두 선택 안 할 경우
    print(total)