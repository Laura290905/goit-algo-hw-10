import pulp

# Define the optimization problem
production_problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Decision variables for the number of Lemonade and Fruit Juice to produce
lemonade_production = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice_production = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Add resource constraints
production_problem += 2 * lemonade_production + 1 * fruit_juice_production <= 100  # Water constraint
production_problem += 1 * lemonade_production <= 50                               # Sugar constraint
production_problem += 1 * lemonade_production <= 30                               # Lemon Juice constraint
production_problem += 2 * fruit_juice_production <= 40                            # Fruit Puree constraint

# Define the objective function to maximize production
production_problem += lemonade_production + fruit_juice_production

# Solve the optimization problem
production_problem.solve()

# Print the results
print(f"Status of the solution: {pulp.LpStatus[production_problem.status]}")
print(f"Optimal quantity of Lemonade to produce: {pulp.value(lemonade_production)}")
print(f"Optimal quantity of Fruit Juice to produce: {pulp.value(fruit_juice_production)}")
print(f"Maximum total production: {pulp.value(production_problem.objective)}")