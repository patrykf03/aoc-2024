from more_itertools import flatten

print(sum([[(sorted_odd.count(y) * y for y in sorted_even) for sorted_even, sorted_odd in [(sorted(flat[::2]), sorted(flat[1::2])) for flat in [list(flatten(list(map(lambda x: list(map(int, x.split())), open("input").readlines()))))]]][0]][0]))