import re
import ast

from sqlalchemy import literal


input = open("test2").read()

find = re.findall(r"((?<=mul)\(\d+,\d+\))|(do\(\)|don't\(\))", input)

count = True
sum = 0

for i in find:
    if (i[0] != "" and count):
        ituple = ast.literal_eval(i[0])
        sum += ituple[0] * ituple[1]
    elif (i[1] == "do()"):
        count = True
    else:
        count = False
print(sum)




#print(find)

