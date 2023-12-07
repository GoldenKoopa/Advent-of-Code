import functools

contents = '''94J8A 16
JK59A 722
Q5QQQ 681
T99T2 39
595JQ 533
98299 550
T596T 971
JQ999 831
J3K39 340
K93T5 107
2999T 750
KQ4K4 603
TT6TT 778
QAQJQ 731
K2444 109
T87J4 984
72272 70
555QJ 266
44384 872
67768 140
555A9 322
Q9A52 14
6JTTT 994
66J7Q 360
6J966 170
74335 288
Q7QK7 318
T63K8 355
88Q38 612
TKKKK 291
8T295 608
77A77 312
3ATTA 861
6JJ66 866
82367 229
J86TQ 457
AJAAA 521
JTTTT 380'''.splitlines()

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
    print(a, b)
    for i in range(len(a)):
        difference = order.index(a[i]) - order.index(b[i])
        if difference is not 0:
            return difference

for lst in [five, four, full, three, two_pair, one_pair, high]:
    if len(lst) > 1:
        lst = sorted(lst, key=functools.cmp_to_key(sort_for_high))

ranked = high + one_pair + two_pair + three + full + four + five
print(ranked)
bids = [int(bids[i])*(ranked.index(hands[i])+1) for i in range(len(bids))]
print(sum(bids), bids)
