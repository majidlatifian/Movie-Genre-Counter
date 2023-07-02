n = int(input())

Action = 0
Comedy = 0
History = 0
Horror = 0
Romance = 0
Adventure = 0

for i in range(0,n):
    nazar = input().split()
    if any("Action" in s for s in nazar):
        Action += 1
    if any("Comedy" in s for s in nazar):
        Comedy += 1
    if any("History" in s for s in nazar):
        History += 1
    if any("Horror" in s for s in nazar):
        Horror += 1
    if any("Romance" in s for s in nazar):
        Romance += 1
    if any("Adventure" in s for s in nazar):
        Adventure += 1

ara = [('Action',Action), ('Comedy',Comedy), ('History',History), ('Horror',Horror), ('Romance',Romance), ('Adventure',Adventure)]

sorted_ara = sorted (ara, key = lambda x : (-x[1],x[0]))

for j in range(0, len(sorted_ara)):
    st = ' : '.join(map(str, sorted_ara[j]))
    print(st)