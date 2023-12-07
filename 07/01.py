import functools
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().splitlines()

# contents = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''.splitlines()

hands = [contents[i].split()[0] for i in range(len(contents))]
bids = [contents[i].split()[1] for i in range(len(contents))]

print(hands, bids)

five = []
four = []
full = []
three = []
two_pair = []
one_pair = []
high = []

order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
order = order[::-1]

for hand in hands:
    dic = {}
    for i in range(5):
        if hand[i] in dic:
            continue
        else:
            dic[hand[i]] = len([j for j in hand if j == hand[i]])
    sorted_dic  = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dic)
    print(list(sorted_dic)[-1])
    if list(sorted_dic.values())[0] == 5: five.append(hand)
    elif list(sorted_dic.values())[0] == 4: four.append(hand)
    elif list(sorted_dic.values())[0] == 3 and list(sorted_dic.values())[1] == 2: full.append(hand)
    elif list(sorted_dic.values())[0] == 3: three.append(hand)
    elif list(sorted_dic.values())[0] == 2 and list(sorted_dic.values())[1] == 2: two_pair.append(hand)
    elif list(sorted_dic.values())[0] == 2: one_pair.append(hand)
    else: high.append(hand)
    print(five, four, full, three, two_pair, one_pair, high)

def lookup(elem):
    return order.index(elem)

def sort_for_high(a, b):
    for i in range(len(a)):
        difference = order.index(a[i]) - order.index(b[i])
        if difference is not 0:
            return difference

ranked = []
for lst in [five, four, full, three, two_pair, one_pair, high]:
    if len(lst) > 1:
        ranked += sorted(lst, key=functools.cmp_to_key(sort_for_high))
    else:
        ranked += lst

print(ranked)
bids = [int(bids[i])*(len(ranked)-ranked.index(hands[i])) for i in range(len(bids))]
print(sum(bids), bids)
