from logic_operators import *


def to_cnf(formula):
    res1 = to_cnf1(formula)
    print(res1)
    res2 = to_cnf2(res1)
    print(res2)
    res3 = cnf_to_clauses(res2)
    print(res3)
    return res3


def to_cnf1(formula):
    # Eliminate Biconditionals
    if isinstance(formula, Biconditional):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return to_cnf1(And(Implication(lhs, rhs), Implication(rhs, lhs)))

    # Eliminate Implications
    elif isinstance(formula, Implication):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return to_cnf1(Or(Not(lhs), rhs))

    # Move negation inwards, using double negation and De Morgan rules
    elif isinstance(formula, Not):
        val = formula.formulas[0]

        # Singular operations
        if isinstance(val, Proposition):
            return formula

        elif isinstance(val, Not):
            return val.formulas[0]

        # Two sided operations
        elif isinstance(val, And):
            lhs = val.formulas[0]
            rhs = val.formulas[1]
            return to_cnf1(Or(Not(lhs), Not(rhs)))

        elif isinstance(val, Or):
            lhs = val.formulas[0]
            rhs = val.formulas[1]
            return to_cnf1(And(Not(lhs), Not(rhs)))

        elif isinstance(val, Implication):
            lhs = val.formulas[0]
            rhs = val.formulas[1]
            return to_cnf1(Or(Not(lhs), rhs))

        return to_cnf1(val)

    elif isinstance(formula, Or):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return Or(to_cnf1(lhs), to_cnf1(rhs))

    elif isinstance(formula, And):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return And(to_cnf1(lhs), to_cnf1(rhs))

    elif isinstance(formula, Proposition):
        return formula

    # Special case for distributive law
    # return formula


def to_cnf2(formula):
    # Apply distributivity law by distributing disjunctions over conjunctions
    if isinstance(formula, Or):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]

        if isinstance(lhs, And):
            return to_cnf2(And(Or(lhs.formulas[0], rhs), Or(lhs.formulas[1], rhs)))

        if isinstance(rhs, And):
            return to_cnf2(And(Or(lhs, rhs.formulas[0]), Or(lhs, rhs.formulas[1])))

        return Or(to_cnf2(lhs), to_cnf2(rhs))

    elif isinstance(formula, And):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return And(to_cnf2(lhs), to_cnf2(rhs))

    elif isinstance(formula, Proposition) or isinstance(formula, Not):
        return formula
    # return formula


def cnf_to_clauses(cnf):
    if isinstance(cnf, And):
        lhs = cnf.formulas[0]
        rhs = cnf.formulas[1]
        return cnf_to_clauses(lhs).union(cnf_to_clauses(rhs))
    else:
        return {cnf}
