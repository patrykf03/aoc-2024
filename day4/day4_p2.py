from more_itertools import flatten
import regex as re


input = open('input').read()
cols = len(input.splitlines()[0])

pattern = [
    fr"(?=(M.{{{1}}}M.{{{cols-1}}}A.{{{cols-1}}}S.{{{1}}}S))", fr"(?=(M.{{{1}}}S.{{{cols-1}}}A.{{{cols-1}}}M.{{{1}}}S))",
    fr"(?=(S.{{{1}}}S.{{{cols-1}}}A.{{{cols-1}}}M.{{{1}}}M))", fr"(?=(S.{{{1}}}M.{{{cols-1}}}A.{{{cols-1}}}S.{{{1}}}M))"
]

print(len(list(flatten([re.findall(pat, input, re.DOTALL, overlapped=True) for pat in pattern]))))
