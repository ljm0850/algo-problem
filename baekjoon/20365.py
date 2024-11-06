def solution(N:int,color:str)->int:
    cnt_ls = [0,0]
    beforeColor = color[0]
    for nowColor in color:
        if nowColor != beforeColor:
            match beforeColor:
                case 'B':cnt_ls[0] += 1
                case 'R':cnt_ls[1] += 1
            beforeColor = nowColor
    match nowColor:
        case 'B':cnt_ls[0] += 1
        case 'R':cnt_ls[1] += 1
    return 1+min(cnt_ls)

N = int(input())
color = input()
ans = solution(N,color)
print(ans)