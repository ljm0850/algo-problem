def solution(n):
    # 3진법 문제
    num_dict = {0:'4', 1:'1', 2:'2'}
    answer = ''
    while n > 0:
        answer = num_dict[n % 3] + answer
        n = (n - 1) // 3
    return answer