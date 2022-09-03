N = int(input())
card_cnt = {}
for _ in range(N):
    card = int(input())
    if card_cnt.get(card):
        card_cnt[card] += 1
    else:
        card_cnt[card] = 1
cards = sorted(list(card_cnt.items()),key=lambda card:card[0], reverse=True)
cards.sort(key=lambda  card:card[1])
print(cards[-1][0])