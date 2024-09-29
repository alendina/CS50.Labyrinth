from util import Labyrinth, Node, QueueFrontier

# Constants 
FILE_NAME = "Labyrinth01.txt"
CRETE_HTML = True


# Broad First Search
class LabyrinthBFS(Labyrinth):
    def __init__(self, filename):
        super().__init__(filename)
        self.method = "BFS"
   
    def search(self):
        #print(f"\nMethod ({self.method}):")
        #print(f"Start: {self.start}, Finish: {self.finish}")

        start_node = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start_node)
        
        while True:
            if frontier.empty():
                print(f"\nSOLUTION ({self.method}): No solution")
                print(f"Explored: {len(self.explored)}")
                return "No solution"

            node = frontier.remove()
            #print(f"\nNode: {node.state}")

            if node.state == self.finish:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                    if node.state != self.start and node.state != self.finish:
                        self.labyrinth[node.state[0]][node.state[1]] = self.symbols["pass_finish"]
                actions.reverse()
                cells.reverse()
                self.way = cells

                print(f"\nSOLUTION ({self.method}):")
                print(f"Way: {len(actions)}")
                print(f"Explored: {len(self.explored)}")
                print(f"Actions: {actions}")
                print(f"Nodes: {cells}")

                return actions, cells

            self.explored.append(node.state)
            if node.state != self.start:
                self.labyrinth[node.state[0]][node.state[1]] = self.symbols["pass_all"]
            
            neighbors = node.get_neighbors(self)
            #print(f"Neighbors: {[neighbor.state for neighbor in neighbors]}")

            for neighbor in neighbors:
                if not frontier.contains_state(neighbor.state) and neighbor.state not in self.explored:
                    frontier.add(neighbor)
            
            #print(f"Frontier: {[node_f.state for node_f in frontier.frontier]}")
            #print(f"Explored: {self.explored}")
        


def main():
    # Create a new LabyrinthTXT object
    labyrinth = LabyrinthBFS(FILE_NAME)
    
    # Read the labyrinth from a text file
    labyrinth.read_from_txt_file()

    # Find the solution
    labyrinth.search()

    # Write the labyrinth to a text file
    labyrinth.write_to_txt_file()

    # Write the labyrinth to an HTML file
    if CRETE_HTML == True:
        labyrinth.write_to_html(clean=True, numbers=None)


if __name__ == "__main__":
    main()