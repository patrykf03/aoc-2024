from more_itertools import pairwise

input = [list(map(int,x.split()))  for x in open("input").readlines()]
result = [all(i) for i in zip([sorted(x, reverse= x[0] > x[1]) == x for x in input], [all(1<= y <= 3 for y in [abs(a-b) for a,b in pairwise(x)]) for x in input])]
input2 = [[x[:i] + x[i+1:] for i in range(len(x))] for x in input if result[input.index(x)] == False] 
result2: list[bool] = [any([all(i) for i in zip(a2_l, b2_l)]) for a2_l, b2_l in zip([[sorted(x, reverse= x[0] > x[1]) == x for x in a] for a in input2], [[all(1<= y <= 3 for y in [abs(a-b) for a,b in pairwise(x)]) for x in a] for a in input2])] 

print(result.count(True))
print(result.count(True) + result2.count(True))