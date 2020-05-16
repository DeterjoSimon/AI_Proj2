"""
This file shows an example on how to use the belief revision engine
"""

from engine import Belief
from engine import BeliefBase
from engine import parse


def select_largest_set(remainders):
    return [max(remainders, key=lambda x: len(x))]


def select_highest_total_order(remainders):
    return [max(remainders, key=lambda x: sum((belief.order for belief in x)))]


# Parse formulas
p = parse("p")
porq = parse("(p | q)")

# Create knowledge base from beliefs with a plausibility order
kb = {Belief(p, 0.3), Belief(porq, 0.4)}

# Create belief base from a knowledge base and specify the selection function for remainders
bb = BeliefBase(kb=kb, selection_function=select_largest_set)

# Change methods on the belief base
print("Adding: q, r & q, r | p")
bb.expand(Belief(parse("q"), 0.2))
bb.expand(Belief(parse("r and q"), 0.4))
bb.expand(Belief(parse("r or p"), 0.25))
print(bb)
print("Contracting: r")
bb.contract(Belief(parse("r"), 0.3))
print(bb)
print("Revising: ~(p & q)")
bb.revise(Belief(parse("~(p & q)"), 0.95))
print(bb)
print("Changing selection function to highest total order")
bb.selection_function = select_highest_total_order
print("Revising: ~p")
bb.revise(Belief(parse("~p"), 0.35))
print(bb)
