from typing import Set

from logic_operators import *


# If you read this, you have the big gay

def get_literals(clause):
    if isinstance(clause, Not) or isinstance(clause, Proposition):
        return [clause]

    if isinstance(clause, Par):
        return get_literals(clause.formulas[0])
    else:
        return get_literals(clause.formulas[0]) + get_literals(clause.formulas[1])


def resolve(clause1, clause2):
    literals1 = get_literals(clause1)
    literals2 = get_literals(clause2)

    def disjunct(values):
        if len(values) == 1:
            return values[0]

        return Or(values[0], disjunct(values[1:]))

    new_clauses = []

    # Check for complimentary pairs
    for lit1 in literals1:
        for lit2 in literals2:
            if Not(lit1) == lit2 or lit1 == Not(lit2):
                # Remove complimentary pair
                new_lit1 = [x for x in literals1 if x != lit1]
                new_lit2 = [x for x in literals2 if x != lit2]

                # Factor
                combined = list(set(new_lit2 + new_lit1))
                combined.sort()

                # Combine results in disjunction
                new_clauses.append(disjunct(combined))

    return new_clauses


def entailment(kb, phi):
    clauses: Set = kb  # TODO: Insert CNF function here

    # Negate phi
    if isinstance(phi, Not):
        phi = phi.formulas[0]
    else:
        phi = Not(phi)

    clauses.add(phi)

    # Pair all clauses
    for clause1 in clauses:
        for clause2 in clauses:
            res_clause = resolve(clause1, clause2)

            # If empty set is found (unsatisfiable) then entailment is true
            if not res_clause and isinstance(res_clause, Set):
                return True

            clauses.add(res_clause)

    # Fail safe, does not entail
    return False
