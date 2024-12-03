import re, ast
from more_itertools import flatten

separatedinput = sum(flatten(list(map(lambda x: ast.literal_eval(x)[0]*ast.literal_eval(x)[1], re.findall(r"(?<=mul)\(\d+,\d+\)", instructions[1]))) for instructions in re.findall(r"(do\(\)|don't\(\))(.*?)(?=do\(\)|don't\(\))", "do()"+open("test2").read() + "don't()") if instructions[0] == "do()"))

print(separatedinput)
