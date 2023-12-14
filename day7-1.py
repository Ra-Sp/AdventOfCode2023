data = list(open('day7-input.txt'))

order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

ranked_hands = []

for hand in data:
    cards, bid = hand.split()
    counts = sorted([cards.count(card) for card in set(cards)])

    if counts == [5]:
        five_of_a_kind.append([cards, bid])
    elif counts == [1, 4]:
        four_of_a_kind.append([cards, bid])
    elif counts == [2, 3]:
        full_house.append([cards, bid])
    elif counts == [1, 1, 3]:
        three_of_a_kind.append([cards, bid])
    elif counts == [1, 2, 2]:
        two_pair.append([cards, bid])
    elif counts == [1, 1, 1, 2]:
        one_pair.append([cards, bid])
    else:
        high_card.append([cards, bid])


ranked_hands.extend(sorted(high_card, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))
ranked_hands.extend(sorted(one_pair, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))
ranked_hands.extend(sorted(two_pair, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))
ranked_hands.extend(sorted(three_of_a_kind, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))
ranked_hands.extend(sorted(full_house, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))
ranked_hands.extend(sorted(four_of_a_kind, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))
ranked_hands.extend(sorted(five_of_a_kind, reverse=True, key=lambda x: [order.index(card) for card in x[0]]))

rank = 1
tot_winnings = 0
for hand, bid in ranked_hands:
        tot_winnings += int(bid) * rank
        rank += 1

print(tot_winnings)