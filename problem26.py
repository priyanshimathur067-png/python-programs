# Coding Content
problem_a = set(input("Enter users who solved Problem A: ").split(","))
problem_b = set(input("Enter users who solved Problem B: ").split(","))
problem_c = set(input("Enter users who solved Problem C: ").split(","))

problem_a = {x.strip() for x in problem_a}
problem_b = {x.strip() for x in problem_b}
problem_c = {x.strip() for x in problem_c}

all_three = problem_a & problem_b & problem_c

a_b = problem_a & problem_b

all_users = problem_a | problem_b | problem_c

print("\nSolved all three:", all_three)
print("Solved A and B:", a_b)
print("Total participants:", len(all_users))