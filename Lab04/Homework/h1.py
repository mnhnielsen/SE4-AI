import queens_fitness
import random

mut = 0.2
gen = 75


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(gen):
        print(generation)
        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < mut:
                child = mutate(child)

            new_population.add(child)

        population = population.union(new_population)
        population = trim_population(population, fitness_fn)
        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def trim_population(population, fitness_fn):
    new_population = set()
    for individual in population:
        if fitness_fn(individual) > -7:
            new_population.add(individual)
    return new_population


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    number = random.randrange(1, len(father))
    child = [1] * len(father)
    for i in range(0, number + 1):
        child[i] = mother[i]
    for j in range(number, len(father)):
        child[j] = father[j]
    return tuple(child)




def mutate(individual):
    if len(individual) > 0:
        number = random.randrange(len(individual))
        mutation = [1] * len(individual)

        for i in range(0, len(individual)):
            if i != number:
                mutation[i] = individual[i]
            else:
                mutation[i] = random.randrange(1, 9)

        return tuple(mutation)



def random_selection(population, fitness_fn):
    ordered_population = list(population)
    fitness_population = []

    fitness_sum = 0

    for individual in ordered_population:
        fitness = fitness_fn(individual)
        fitness_sum += fitness
        fitness_population.append(fitness)

    selection = []

    for i in range(0, len(ordered_population)):
        probability = fitness_population[i] / fitness_sum
        if len(selection) >= 2:
            break
        if random.randint(0, 100) <= probability * 100 or random.randint(0, 100) > 80:
            selection.append(i)

    while len(selection) < 2:
        best = max(fitness_population)
        selection.append(fitness_population.index(best))
        fitness_population.remove(best)

    return ordered_population[0], ordered_population[1]




def fitness_function(individual):
    fitness = 0
    reversed_individuals = individual[::-1]
    for i in range(0, len(reversed_individuals)):
        fitness += (2 ** i) * reversed_individuals[i]
    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    initial_population = {
        (1, 3, 7, 5, 2, 4, 6, 8),
        (5, 7, 3, 1, 8, 2, 4, 6)
    }
    fittest = genetic_algorithm(initial_population, queens_fitness.fitness_fn_negative, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " fitness: " + str(queens_fitness.fitness_fn_negative(fittest)))


if __name__ == '__main__':
    pass
    main()