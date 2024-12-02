from more_itertools import pairwise

input = [list(map(int,x.split()))  for x in open("input").readlines()]

c = [all(i) for i in zip([sorted(x, reverse= x[0] > x[1]) == x for x in input], [all(1<= y <= 3 for y in [abs(a-b) for a,b in pairwise(x)]) for x in input])]

print(c.count(True))