T = int(input())

def judge(x) :
    x2 = []
    for i in range(9):
        #행 정렬시 아니면 0
        if sorted(x[i]) != [1,2,3,4,5,6,7,8,9] :
            return 0
        a = []
        
        # x의 행과 열이 바뀐 리스트 생성
        for j in range(9):
            a.append(x[j][i])
        x2.append(a)
    # 바뀐 행렬을 가진 x2 정렬시 아니면 0
    for k in range(9):
        if sorted(x2[k]) != [1,2,3,4,5,6,7,8,9] :
            return 0
    #가로3 세로3 측정
    for i in range(0,9,3):
        for j in range(0,9,3):
                x1 = []
                x1 += (x[j][i],x[j][i+1],x[j][i+2],
                x[j+1][i],x[j+1][i+1],x[j+1][i+2],
                x[j+2][i],x[j+2][i+1],x[j+2][i+2])
            
                if sorted(x1) != [1,2,3,4,5,6,7,8,9] :
                    return 0
    #그래도 안걸러지면 1 반환
    return 1

for i in range(1,T+1):
    puzzle = []
    #리스트 안에 리스트 형식으로 puzzle 형태 완성
    for _ in range(9):
        puzzle.append(list(map(int,input().split())))
    print(f'#{i} {judge(puzzle)}')
    