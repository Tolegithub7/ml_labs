# Searching Algorithm : DFS
global_node_id = 0


def get_next_node_id():
    global global_node_id
    global_node_id += 1
    return global_node_id


import heapq


def DepthFirstSearch(problem):
    D = {}
    Q = []

    init_state = problem.initial_state()
    node_id = global_node_id

    D[init_state] = [None, 0]
    heapq.heappush(Q, (node_id, init_state, priority_function(D, init_state)))

    while Q:
        node_id, current, priority = heapq.heappop(Q)

        if problem.isGoal(current):
            path = []
            while current is not None:
                path.insert(0, current)
                current = D[current][0]
            return path

        print("Processing:", node_id, current, priority)
        print("Dictionary (D):", D)
        print("Priority Queue (Q):", Q)
        print()

        for child in problem.children(current):
            cost = D[current][1] + problem.actionCost(current, child)

            if child not in D or cost < D[child][1]:
                node_id = get_next_node_id()
                D[child] = [current, cost]
                priority = priority_function(D, child)
                heapq.heappush(Q, (node_id, child, priority))

    return None


def priority_function(D, state):
    return 0 if state == "Arad" else priority_function(D, D[state][0]) - 1


class RomaniaProblem:
    def __init__(self, graph):
        self.graph = graph

    def initial_state(self):
        return "Arad"

    def isGoal(self, state):
        return state == "Bucharest"

    def children(self, state):
        return self.graph[state]

    def actionCost(self, state, next_state):
        return 1


graph = {
    "Arad": ["Sibiu", "Timisoara", "Zerind"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Rimnicu Vilcea": ["Sibiu", "Pitesti", "Craiova"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
    "Pitesti": ["Craiova", "Rimnicu Vilcea", "Bucharest"],
    "Bucharest": ["Pitesti", "Fagaras", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Vaslui", "Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
}

problem = RomaniaProblem(graph)
result = DepthFirstSearch(problem)

path_str = " -> ".join(result)
print("The path found using DFS Algorithm :", path_str)
