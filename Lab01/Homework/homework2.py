import random

A = "A"
B = "B"
C = "C"
D = "D"
rooms = [A, B, C, D]
state = {}
action = None
model = {
    A: None,
    B: None,
    C: None,
    D: None
}

ruleAction = {
    1: "Suck",
    2: "Right",
    3: "Left",
    4: "NoOp"
}

rules = {
    (A, "Dirty"): 1,
    (B, "Dirty"): 1,
    (A, "Clean"): 2,
    (B, "Clean"): 3,
    (C, "Dirty"): 1,
    (C, "Clean"): 2,
    (D, "Dirty"): 1,
    (D, "Clean"): 3,

    (A, B, C, D, "Clean"): 4,
}

Environment = {
    A: "Dirty",
    B: "Dirty",
    C: "Dirty",
    D: "Dirty",
    "Current": random.choice(rooms)
}


def interpret_input(input):
    return input


def rule_match(state, rules):
    rule = rules.get(tuple(state))
    return rule


def update_state(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == model[C] == model[D] == 'Clean':
        state = (A, B, C, D, 'Clean')

    model[location] = status
    return state


def reflex_agent_with_state(percept):
    global state, action
    state = update_state(state, action, percept)
    rule = rule_match(state, rules)
    action = ruleAction[rule]
    return action


def sensors():
    location = Environment['Current']
    return (location, Environment[location])


def actuators(action):
    location = Environment['Current']
    if action == "Suck":
        Environment[location] = "Clean"
    elif action == "Right" and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment["Current"] = C
    elif action == 'Right' and location == C:
        Environment['Current'] = D
    elif action == 'Left' and location == D:
        Environment['Current'] = A


def run(n):
    print('    Current                New')
    print('Location   status   action   location   status')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:12s}{:8s}".format(location, status), end="")
        action = reflex_agent_with_state(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))


run(20)
