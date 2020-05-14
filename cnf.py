from logic_operators import *


def to_cnf(formula):
    # Eliminate Biconditionals
    if isinstance(formula, Biconditional):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return to_cnf(And(Implication(lhs, rhs), Implication(rhs, lhs)))

    # Eliminate Implications
    elif isinstance(formula, Implication):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return to_cnf(Or(Not(lhs), rhs))

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
            return to_cnf(Or(Not(lhs), Not(rhs)))

        elif isinstance(val, Or):
            lhs = val.formulas[0]
            rhs = val.formulas[1]
            return to_cnf(And(Not(lhs), Not(rhs)))

        elif isinstance(val, Implication):
            lhs = val.formulas[0]
            rhs = val.formulas[1]
            return to_cnf(And(lhs, Not(rhs)))

        elif isinstance(val, Biconditional):
            lhs = val.formulas[0]
            rhs = val.formulas[1]
            return to_cnf(Biconditional(Not(lhs), rhs))

        return to_cnf(val)

    elif isinstance(formula, Or):
        lhs = to_cnf(formula.formulas[0])
        rhs = to_cnf(formula.formulas[1])

        if isinstance(lhs, And):
            return to_cnf(And(Or(lhs.formulas[0], rhs), Or(lhs.formulas[1], rhs)))

        if isinstance(rhs, And):
            return to_cnf(And(Or(lhs, rhs.formulas[0]), Or(lhs, rhs.formulas[1])))

        return Or(lhs, rhs)

    elif isinstance(formula, And):
        lhs = formula.formulas[0]
        rhs = formula.formulas[1]
        return And(to_cnf(lhs), to_cnf(rhs))

    elif isinstance(formula, Proposition):
        return formula


def cnf_to_clauses(cnf):
    if isinstance(cnf, And):
        lhs = cnf.formulas[0]
        rhs = cnf.formulas[1]
        return cnf_to_clauses(lhs).union(cnf_to_clauses(rhs))
    else:
        return {cnf}
