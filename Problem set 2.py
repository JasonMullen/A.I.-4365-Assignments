#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ortools')


# In[ ]:





# In[36]:


# Import required libraries
from ortools.constraint_solver import pywrapcp
import csv

# Define function to solve problem using OR-Tools constraint solver
def solveProblem(problem, constraints, vconstraints, problemName):
    # Initialize OR-Tools solver
    solver = pywrapcp.Solver(problemName)
    # Create variables for the problem using IntVar method
    problemVars = [solver.IntVar(1, 125, f"X{i+1}") for i in range(len(problem))]
    # Create constraints using the provided constraint functions and add them to a list
    constraintVars = [c(solver, problemVars) for c in constraints] + [vc for vc in vconstraints]
    # Call getSolution function to solve problem and return the solution and the number of variable assignments
    solution, nva = getSolution(problemVars, constraintVars, vconstraints)
    # Return the solution and the number of variable assignments
    return solution, nva

# Define function to solve the problem using OR-Tools and return the solution and the number of variable assignments
def getSolution(problem, constraints, vconstraints):
    # Initialize OR-Tools solver
    solver = pywrapcp.Solver("Solver")
    # Define the search strategy as choosing the first unbound variable and assigning the minimum value
    db = solver.Phase(problem, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
    # Start a new search with the defined search strategy
    solver.NewSearch(db)
    # Initialize the number of variable assignments to 0
    nva = 0
    # If a solution is found, retrieve the solution and the number of variable assignments
    if solver.NextSolution():
        nva = solver.Branches()
        solution = [problem[i].Value() for i in range(len(problem))]
        # Return the solution and the number of variable assignments
        return solution, nva
    # If no solution is found, return None and the number of variable assignments
    else:
        return None, nva

constraintsA = [
    lambda solver, X: solver.Add(X[0] == X[1] + X[2] + X[4] + X[5]),
    lambda solver, X: solver.Add(X[5] > X[4] - X[1]),
    lambda solver, X: solver.Add(X[3] == X[4] + X[5] + 21),
    lambda solver, X: solver.Add(X[3] * X[3] == X[4] * X[4] * X[0] + 694)
]

# Problem B
constraintsB = [
    lambda solver, X: solver.Add(X[7] * X[9] + X[4] * 16 == (X[6] + X[8]) * (X[6] + X[8]) - 48),
    lambda solver, X: solver.Add(X[0] - X[2] == (X[7] - X[5]) * (X[7] - X[5]) + 4),
    lambda solver, X: solver.Add(4 * X[9] == X[6] * X[6] + 7),
    lambda solver, X: solver.Add(X[7] + X[8] < X[3]),
    lambda solver, X: solver.Add(X[4] * X[4] < X[6] * X[6] + X[9] * X[9])
]

# Problem C
constraintsC = [
    lambda solver, X: solver.Add(2*X[4] == X[3]*X[3] - X[0]*8),
    lambda solver, X: solver.Add((X[2]-X[3])(X[2]-X[3]) == X[5]*X[3]*2 + 360),
    lambda solver, X: solver.Add(X[2]*X[2] - 135 == X[4]*X[1] + X[0]*X[0]),
    lambda solver, X: solver.Add((X[6]+X[2])(X[6]+X[2]) + 445 == (X[1]+X[5])(X[3]+X[4]+X[2]+X[6]*X[0])),
    lambda solver, X: solver.Add(X[6]*X[2] + 2250 == X[0]*X[0](X[7]-X[5])),
    lambda solver, X: solver.Add(X[3]*X[3]*X[3] - 900 == X[5]*X[1]*X[0] + X[4]*X[4]),
    lambda solver, X: solver.Add((X[8]-X[2])(X[8]-X[2]) - (X[8]-X[3])(X[8]-X[3]) == X[0]*X[0] + X[3]*X[6] - X[4]*X[4] - 1425)
]

# Solve Problem A
solutionA, nvaA = solveProblem(range(6), constraintsA, [], "Problem A")
if solutionA is not None:
    print("*Solution for Problem A:", solutionA)
else:
    print("*No solution exists for Problem A")
print("nva for Problem A:", nvaA)



# Solve Problem B
solutionB, nvaB = solveProblem(range(10), constraintsB, [], "Problem B")
if solutionB is None:
    print("*No solution exists for Problem B")
else:
    print("*Solution for Problem B:", solutionB)
print("Number of variable assignments for Problem B:", nvaB)


# Solve Problem C
solutionC, nvaC = solveProblem(range(16), constraintsC, [], "Problem C")
if solutionC is None:
    print("*No solution exists for Problem C")
else:
    print("*Solution for Problem C:", solutionC)
print("Number of variable assignments for Problem C:", nvaC)

