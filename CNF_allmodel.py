# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver

# create a satisfiable CNF formula "(-x1 ∨ -x2 ∨ x3) ∧ (x1 ∨ -x3) ∧ (x2 ∨ -x3)":
cnf = CNF(from_clauses=[[-1, -2, 3], [1, -3], [2, -3]])

def get_all_models(cnf):
    models = []
    with Solver(bootstrap_with=cnf) as solver:
        while solver.solve():
            model = solver.get_model()
            models.append(model)
            # Add a clause to block the current model
            blocking_clause = [-lit for lit in model]
            solver.add_clause(blocking_clause)
    return models

# Get all models
all_models = get_all_models(cnf)
print(f'All models ({len(all_models)}):')
for i, model in enumerate(all_models):
    print(f'Model {i+1}: {model}')
