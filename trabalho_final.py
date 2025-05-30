import random
import math
from statistics import mean, stdev
from operator import itemgetter

max_weight = 1550
max_instances = 100
random.seed(42)

global objfunc_counter
objfunc_counter = 0
values = []
weights = []


with open("knapsack-instance.txt") as f:
    for line in f:
        a = [int(num) for num in line.split()]
        values.append(a[0])
        weights.append(a[1])


def objective_function(solution):
    global objfunc_counter
    objfunc_counter += 1
    score = 0
    weight = 0
    for idx, decision in enumerate(solution):
        if decision:
            score += values[idx]
            weight += weights[idx]

    if weight > max_weight:
        # logging.info("Weight Exceeded! Unfeasible solution.")
        return 0

    return score


# ----- Construção Gulosa Randomizada -----
def construct_solution(alpha):
    solution = [0] * max_instances
    candidates = list(range(max_instances))
    total_weight = 0

    while candidates:
        component = []
        for i in candidates:
            component.append((i, values[i] / weights[i]))

        component.sort(key=itemgetter(1), reverse=True)

        maximo = component[0][1]
        minimo = component[-1][1]
        limite = maximo - alpha * (maximo - minimo)

        restricted_list = []
        for idx, val in component:
            if val >= limite:
                restricted_list.append(idx)

        if restricted_list:
            chosen = random.choice(restricted_list)

            if total_weight + weights[chosen] <= max_weight:
                solution[chosen] = 1
                total_weight += weights[chosen]

            candidates.remove(chosen)

    return solution


def neighbor(solution):
    changes = random.randint(1, 4)
    for _ in range(changes):
        idx = random.randint(0, max_instances - 1)
        solution[idx] = 1 - solution[idx]
    return solution


def simulated_annealing(
    best_solution: list[int], objfunc_iterations: int, temperature: float, beta: float
):
    best_score = objective_function(best_solution)

    diff = 0
    r = random.uniform(0, 1)
    iterations = 0

    while True:
        if objfunc_counter >= objfunc_iterations:
            # print(f"BEST SCORE: {best_score}.")
            return best_solution

        current_solution = neighbor(best_solution)

        current_score = objective_function(current_solution)
        diff = current_score - best_score
        if current_score == 0 or diff == 0:
            pass
        else:
            boltzman_decision = (math.exp(diff / temperature)) > r

            if (diff > 0) and (boltzman_decision):
                best_solution = current_solution
                best_score = current_score

        iterations += 1
        temperature = temperature / 1 + beta * iterations


# ----- GRASP -----
def grasp(iterations, alpha):
    best_solution = None
    best_score = 0

    for _ in range(iterations):
        sol = construct_solution(alpha)
        # Com Busca Local
        # sol = simulated_annealing(sol, 19901, 1000, 0.9)
        score = objective_function(sol)

        if score > best_score:
            best_score = score
            best_solution = sol[:]

    return best_solution, best_score


# ----- Execução -----
if __name__ == "__main__":
    # Com Busca Local
    # iterations = 50
    # Sem Busca Local
    iterations = 20000
    alpha = 0.25

    executions = []
    for _ in range(20):
        best_sol, best_val = grasp(iterations, alpha)
        executions.append(best_val)
        objfunc_counter = 0

    print(f"Mean: {mean(executions)}")
    print(f"Stdev: {stdev(executions)}")
    print(f"Melhor: {max(executions)}")
    print(f"Pior: {min(executions)}")
