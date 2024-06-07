import pulp

problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

L = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
F = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

problem += L + F, "Total_Products"

problem += 2*L + 1*F <= 100, "Water_Constraint"
problem += 1*L <= 50, "Sugar_Constraint"
problem += 1*L <= 30, "LemonJuice_Constraint"
problem += 2*F <= 40, "FruitPuree_Constraint"
problem.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Lemonade: {L.varValue} units")
print(f"Fruit Juice: {F.varValue} units")
print(f"Total Products: {pulp.value(problem.objective)} units")
