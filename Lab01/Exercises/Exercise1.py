A = 'A'
B = 'B'

percepts = []

table = {
    ((A, "Clean"),): 'Right',
    ((A, "Dirty"),): 'Suck',
    ((B, "Clean"),): 'Left',
    ((B, "Dirty"),): 'Suck',
    ((A, "Clean"), (A, 'Clean')): 'Right',
    ((A, "Clean"), (A, 'Dirty')): 'Suck',
    ((A, "Clean"), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, "Clean"), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, "Clean"), (A, 'Dirty'), (A, 'Clean')): 'Left',
}


def look_Up(percepts, table):
    action = table.get(tuple(percepts))
    return action


def table_driven_agent(percept):
    percepts.append(percept)
    action = look_Up(percepts, table)
    return action


def run():
    print('Action \tPercepts')
    print(table_driven_agent((A, 'Clean')), '\t', percepts)
    print(table_driven_agent((A, 'Dirty')), '\t', percepts)
    print(table_driven_agent((B, 'Clean')), '\t', percepts)


run()

# 2.3: We see the actions and the percept when entering a location and a state
# 3: 1
# 4: T³?
