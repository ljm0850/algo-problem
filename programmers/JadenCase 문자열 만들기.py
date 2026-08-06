def solution(s):
    answer = ''
    S = len(s)
    start,end = 0,0
    while end <= S:
        if end==S or s[end] == ' ':
            text = s[start:end+1].lower()
            start = end+1
            if not text:pass
            elif text[0].isalpha():
                answer += text.capitalize()
            else:
                answer += text
        end += 1
    return answer
print(solution("3a b  c "))