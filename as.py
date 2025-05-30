import logging
import math
from statistics import mean, stdev
import random
from operator import itemgetter

logging.basicConfig(level=logging.INFO)

max_weight = 1550
max_instances = 100
random.seed(42)


def initialize(file_path):
    global objfunc_counter
    objfunc_counter = 0
    instances = []

    with open(file_path) as f:
        for line in f:
            a = [int(num) for num in line.split()]
            instances.append(a)
    return instances


def greedy_heuristic(instances):
    unit_value = []
    solution = [0] * max_instances
    total_weight = 0
    for idx, instance in enumerate(instances):
        value, weight = instance[0], instance[1]
        unit_value.append([idx, value / weight])
    unit_value = sorted(unit_value, key=itemgetter(1), reverse=True)
    for unit in unit_value:
        total_weight += instances[unit[0]][1]
        if total_weight < max_weight:
            solution[unit[0]] = 1
        else:
            return solution


def objective_function(instances, solution):
    global objfunc_counter
    objfunc_counter += 1
    score = 0
    weight = 0
    for idx, decision in enumerate(solution):
        if decision:
            score += instances[idx][0]
            weight += instances[idx][1]

    if weight > max_weight:
        # logging.info("Weight Exceeded! Unfeasible solution.")
        return 0

    return score


def neighbor(solution):
    changes = random.randint(1, 4)
    for _ in range(changes):
        idx = random.randint(0, max_instances - 1)
        solution[idx] = 1 - solution[idx]
    return solution


instances = initialize("knapsack-instance.txt")
values, weights = [], []
for instance in instances:
    values.append(instance[0])
    weights.append(instance[1])


def neighbor0(solution):
    a, b = random.sample(range(max_instances), 2)
    if a > b:
        a, b = b, a
    solution[a:b] = 1 - solution[a:b]
    return solution


def simulated_annealing(
    objfunc_iterations: int, temperature: float, neighbor_size: int, beta: float
):
    instances = initialize("knapsack-instance.txt")

    best_solution = [random.randint(0, 1) for _ in range(max_instances)]
    best_score = objective_function(instances, best_solution)
    logging.info(f"INITIAL SCORE: {best_score}\nINITIAL SOLUTION: {best_solution}")


    diff = 0
    r = random.uniform(0, 1)
    iterations = 0

    while True:
        if objfunc_counter >= objfunc_iterations:
            return best_score

        current_solution = neighbor(best_solution)

        current_score = objective_function(instances, current_solution)
        diff = current_score - best_score
        if current_score == 0 or diff == 0:
            pass
        else:
            boltzman_decision = (math.exp(diff / temperature)) > r

            if (diff > 0) and (boltzman_decision):
                best_solution = current_solution
                best_score = current_score
                if (best_score != 0):
                    logging.info(f"NEW BEST SCORE: {best_score}")

        iterations += 1
        temperature = temperature / 1 + beta * iterations


def main():
    bests = []
    for _ in range(20):
        bests.append(simulated_annealing(20000, 1000, 20, 0.2))
        print(objfunc_counter)

    print(f"Mean: {mean(bests)}")
    print(f"Stdev: {stdev(bests)}")
    print(f"Melhor: {max(bests)}")
    print(f"Pior: {min(bests)}")


if __name__ == "__main__":
    main()
