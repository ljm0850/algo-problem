def solution(genres, plays):
    genres_dict = {}
    S = len(genres)
    for i in range(S):
        genre, play = genres[i], plays[i]
        if genres_dict.get(genre):
            genres_dict[genre].append((play, i))
        else:
            genres_dict[genre] = [(play, i)]
    total = []
    for genre,value in genres_dict.items():
        cnt = 0
        value.sort(reverse=True,key=lambda x:(x[0],-x[1]))
        temp = []
        for v,i in value:
            cnt += v
            temp.append(i)
        total.append((cnt,temp))
    total.sort(reverse=True)
    answer = []
    for _,ls in total:
        answer += ls[:2]
    return answer

ans = solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])
print(ans)