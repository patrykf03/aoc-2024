from more_itertools import flatten

print(sum(map(lambda x: abs(x[0]-x[1]), zip(sorted((flat:= list(flatten((map(lambda x: (map(int, x.split())), open("input").readlines())))))[::2]), sorted(flat[1::2])))))