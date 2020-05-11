from typing import Set

from logic_operators import *


# If you read this, you have the big gay
def disjunct(values):
    # Base step
    if len(values) == 1:
        return values[0]

    # Recursion step
    return Or(values[0], disjunct(values[1:]))


def get_literals(clause):
    if isinstance(clause, Not) or isinstance(clause, Proposition):
        return [clause]

    if isinstance(clause, Par):
        return get_literals(clause.formulas[0])
    else:
        return get_literals(clause.formulas[0]) + get_literals(clause.formulas[1])


def resolve(cl_i, cl_j):
    literals1 = get_literals(cl_i)
    literals2 = get_literals(cl_j)

    resolvents = []
    # Check for complimentary pairs
    for lit_i in literals1:
        for lit_j in literals2:
            if Not(lit_i) == lit_j or lit_i == Not(lit_j):
                # Remove complimentary pair
                new_lit1 = [x for x in literals1 if x != lit_i]
                new_lit2 = [x for x in literals2 if x != lit_j]

                # Factor
                combined = list(set(new_lit2 + new_lit1))
                combined.sort()

                # Combine results in disjunction
                if len(combined) != 0:
                    resolvents.append(disjunct(combined))
                # Add the empty set otherwise
                else:
                    resolvents.append(False)

    return resolvents


def entailment(kb, phi):
    """
    Figure 7.12 in the book
    """
    # Negate phi
    if isinstance(phi, Not):
        phi = phi.formulas[0]
    else:
        phi = Not(phi)

    clauses: Set = kb.union({phi})  # TODO: Insert CNF function here

    new = set()

    while True:
        # Pair all clauses and apply resolution
        for cl_i in clauses:
            for cl_j in clauses:
                res_clause = resolve(cl_i, cl_j)

                # If empty set is found (unsatisfiable) then entailment is true
                if False in res_clause:
                    return True

                # Add clause to resolution clauses
                for clause in res_clause:
                    new.add(clause)

        # No new clauses have been added
        if new.issubset(clauses):
            return False

        clauses = clauses.union(new)

