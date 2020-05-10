from logic_operators import *


def parse(formula: str):
    for i, char in formula:
        if char == " ":
            return parse(formula[1:])

        elif char == "(":
            return parse(formula[1:])

        elif char in ("and", "&"):
            return And()

        elif char == r'[a-zA-Z]':
            return Proposition(formula)