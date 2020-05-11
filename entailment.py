from logic_operators import *

# If you read this, you have the big gay

def resolve(clause, phi):
    for formula in clause.formulas:
        pass

def res_entailment(kb, phi):
    # TODO: KB to CNF
    clauses = kb

    # Negate phi
    if isinstance(phi, Not):
        phi = phi.formulas[0]
    else:
        phi = Not(phi)

    for i in range(clauses):
        clauses[i] = resolve(clauses[i], phi)
