import functools
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

contents = [line for line in open('input.txt')]

# contents = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''.splitlines()

order = 'J23456789TQKA'
hands = [contents[i].split()[0] for i in range(len(contents))]
bids = [contents[i].split()[1] for i in range(len(contents))]

def get_pairs(hand):
    dic = {}
    for i in range(5):
        if hand[i] in dic:
            continue
        else:
            dic[hand[i]] = len([j for j in hand if j == hand[i]])
    jokers = dic.pop('J', 0)
    if jokers == 5: return 10
    sorted_dic  = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    sorted_dic[0] = (sorted_dic[0][0], (sorted_dic[0][1], sorted_dic[0][1]+jokers))
    match sorted_dic[0][1][1]:
        case 5: return 10
        case 4: return 9
        case 3: return 8 if sorted_dic[1][1] == 2 else 7
        case 2: return 6 if sorted_dic[1][1] == 2 else 5
        case 1: return 4

def sort_for_high(a, b):

    if (difference := get_pairs(a) - get_pairs(b)) != 0:
        return difference

    for i in range(len(a)):
        difference = order.index(a[i]) - order.index(b[i])
        if difference is not 0:
            return difference

ranked = sorted(hands, key=functools.cmp_to_key(sort_for_high))
bids = [int(bids[i])*(ranked.index(hands[i])+1) for i in range(len(bids))]
print(sum(bids))