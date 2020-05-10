from Belief_base.base import Base
from logic_operators.Variables import Variables
from logic_operators.And import And
from logic_operators.Or import Or
from logic_operators.Implication import Implication
from logic_operators.Biconditional import Biconditional
from logic_operators.Not import Not


def tests():
    # Two tests #
    B = Base()
    q = Variables("q", True)
    p = Variables("p", True)

    B.expansion(Or(p, q))
    B.expansion(Biconditional(p, q))

    print("Be4: ")
    B.print(subset=False)

    B.contraction(p)

    print("After: ")
    B.print(subset=True)
    # Works #
    print("Expected: {{p or q},{p BICOND q}}\n\n\n")


    B = Base()
    q = Variables("q", True)
    p = Variables("p", True)

    B.expansion(Or(p, q))
    B.expansion(Biconditional(p, q))
    B.expansion(p)
    B.expansion(And(p,q))

    print("Be4: ")
    B.print(subset=False)

    B.contraction(p)

    print("After: ")
    B.print(subset=True)
    print("Expected: {{p or q},{p BICOND q}}\n\n\n")

    # Can also deal with recursive arguments #

    B = Base()
    q = Variables("q", True)
    p = Variables("p", True)

    B.expansion(And(And(p, p), p))
    B.expansion(q)

    print("Before: ")
    B.print(subset=False)

    B.contraction(q)

    print("After: ")
    B.print(subset=True)








if __name__ == "__main__":
    tests()
