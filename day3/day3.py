import re
import ast

input = open("input").read()

find = sum(map(lambda x: ast.literal_eval(x)[0]*ast.literal_eval(x)[1], re.findall(r"(?<=mul)\(\d+,\d+\)", input)))

print(find)

