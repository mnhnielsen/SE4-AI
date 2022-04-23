class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, heuristic=0, pathcost=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.HEURISTIC = heuristic
        self.PATHCOST = pathcost

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''

global_cost = 0

def A_STAR():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = remove_first(fringe)
        if node.STATE in GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.HEURISTIC = child[2]
        s.PATHCOST = child[1]
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


def insertLifo(node, queue):
    queue.insert(0, node)
    return queue



'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for i in list:
        queue.append(i)
    return queue



'''
Removes and returns the first element from fringe
'''
def remove_first(fringe):
    heuristics = []
    for node in fringe:
        heuristics.append(node.HEURISTIC + node.PATHCOST)

    minimum_heuristic = 0
    for i in range(0, len(heuristics)):
        if heuristics[minimum_heuristic] > heuristics[i]:
            minimum_heuristic = i
    result = fringe[minimum_heuristic]
    fringe.remove(fringe[minimum_heuristic])
    return result


'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ('A', 0, 6)
GOAL_STATE = [('K', 6, 0), ('L', 5, 0), ('L', 3, 0)]
STATE_SPACE = {('A', 0, 6): [('B', 1, 5), ('C', 2, 5), ('D', 4, 2)],
               ('B', 1, 5): [('F', 5, 5), ('E', 4, 4)],
               ('C', 2, 5): [('E', 1, 4)],
               ('D', 4, 2): [('H', 1, 1), ('I', 4, 2), ('J', 2, 1)],
               ('E', 4, 4): [('G', 2, 4), ('H', 3, 1)],
               ('E', 1, 4): [('G', 2, 4), ('H', 3, 1)],
               ('F', 5, 5): [('G', 1, 4)],
               ('G', 1, 4): [('K', 6, 0)],
               ('G', 2, 4): [('K', 6, 0)],
               ('H', 3, 1): [('K', 6, 0), ('L', 5, 0)],
               ('H', 1, 1): [('K', 6, 0), ('L', 5, 0)],
               ('I', 4, 2): [('L', 3, 0)],
               ('J', 2, 1): [],
               ('K', 6, 0): [],
               ('L', 5, 0): [],
               ('L', 3, 0): []
               }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = A_STAR()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()

