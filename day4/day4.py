import regex as re

input = open('input').read().splitlines()
rows,cols = len(input),len(input[0])

input_45 = [''.join(input[r][c] for r in range(rows) if 0 <= (c := diagonal - r) < cols) for diagonal in range(rows + cols - 1)]
input_135 = [''.join(input[r][c] for r in range(rows) if 0 <= (c := cols - 1 - (diagonal - r)) < cols) for diagonal in range(rows + cols - 1)]
input_90= [''.join(row) for row in zip(*input[::-1])]

input = input + input_45 + input_135 + input_90

print(sum([len(re.findall(r'XMAS', line) + re.findall(r'SAMX', line)) for line in input]))