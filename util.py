class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def get_neighbors(self, labyrinth):
        neighbors = []
        # Check cell Up
        if self.state[0]-1 >= 0 and labyrinth.labyrinth[self.state[0]-1][self.state[1]] != labyrinth.symbols["wall"]:
            new_node = Node(state=(self.state[0]-1, self.state[1]), parent=self, action="Up")
            neighbors.append(new_node)
        # Check cell Down
        if self.state[0]+1 <= labyrinth.height-1 and labyrinth.labyrinth[self.state[0]+1][self.state[1]] != labyrinth.symbols["wall"]:
            new_node = Node(state=(self.state[0]+1, self.state[1]), parent=self, action="Down")
            neighbors.append(new_node)
        # Check cell Left
        if self.state[1]-1 >= 0 and labyrinth.labyrinth[self.state[0]][self.state[1]-1] != labyrinth.symbols["wall"]:
            new_node = Node(state=(self.state[0], self.state[1]-1), parent=self, action="Left")
            neighbors.append(new_node)
        # Check cell Right
        if self.state[1]+1 <= labyrinth.width - 1 and labyrinth.labyrinth[self.state[0]][self.state[1]+1] != labyrinth.symbols["wall"]:
            new_node = Node(state=(self.state[0], self.state[1]+1), parent=self, action="Right")
            neighbors.append(new_node)
        
        return neighbors

    


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

