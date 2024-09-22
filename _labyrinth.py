import os
import random
from util import Node, StackFrontier, QueueFrontier

CRETE_HTML = True
NEW_FILE = True
CLEAN_LABYRINTH = False
FILE_NAME = "Labyrinth07.txt"
LABYRINTH_WIDTH = 40
LABYRINTH_HIGHT = 40
PROBABILITIES = [0.4, 0.6, 0, 0]
LABYRINTH_SYMBOLS = {
    "wall"  : "#",
    "tunnel": " ",
    "start" : "A",
    "finish": "B",
    "pass_finish"  : "*",
    "pass_all"     : "."
}
LABYRINTH_HTML_COLOR = {
    "wall"  : "rgb(182, 180, 180)", 
    "tunnel": "White", 
    "start" : "rgb(160, 160, 231)", 
    "finish": "rgb(212, 159, 159)", 
    "pass_finish"  : "rgb(149, 197, 149)",
    "pass_all"     : "rgb(243, 233, 156)"
}

class Labyrinth:
    def __init__(self, symbols=LABYRINTH_SYMBOLS, filename=FILE_NAME, newfile=NEW_FILE, width=10, height=10):
        self.width = width
        self.height = height
        self.symbols = symbols
        self.newfile = newfile
        self.filename = filename
        self.labyrinth = []
        self.start = None
        self.finish = None
        
    
    def generate_labyrinth(self):
        self.labyrinth = []
        symbols = [self.symbols["wall"], self.symbols["tunnel"]]
        for _ in range(self.height):
            row = [random.choice(symbols) for _ in range(self.width)]
            self.labyrinth.append(row)

        start_pos = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
        self.labyrinth[start_pos[1]][start_pos[0]] = self.symbols["start"]
        self.start = (start_pos[1], start_pos[0])

        finish_pos = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
        self.labyrinth[finish_pos[1]][finish_pos[0]] = self.symbols["finish"]
        self.finish = (finish_pos[1], finish_pos[0])
        '''
        for row in self.labyrinth:
            print(*row)
        return self.labyrinth
        '''

    def generate_next_file_name(file_name="Labyrinth"):
        folder = os.getcwd()
        files = os.listdir(folder)
        labyrinth_files = [file for file in files if file.startswith(file_name) and file.endswith(".txt")]
        numbers = [int(file.strip(file_name).strip(".txt")) for file in labyrinth_files]
        next_number = max(numbers) + 1 if numbers else 1
        new_file_name = f"{file_name}{next_number:02}.txt"
        new_file_path = os.path.join(folder, new_file_name)
        return new_file_path


    def write_to_txt_file(self):
        if self.filename is None or self.filename == "":
            self.filename = Labyrinth.generate_next_file_name()

        if self.labyrinth is None:
            raise Exception("Labyrinth is not generated")
        else:
            with open(self.filename, "w") as new_file:
                for row in self.labyrinth:
                    new_file.write("".join(row) + "\n")
            print(f"\nText file {self.filename} created successfully.")


    def read_from_txt_file(self):
        if self.filename is None:
            raise Exception("Filename is not provided")

        if not os.path.exists(self.filename):
            raise Exception("File does not exist")
        
        #Clean the labyrinth from previous passes
        if CLEAN_LABYRINTH == True:
            with open(self.filename, "r+") as file:
                content = file.read()
                content = content.replace(".", " ")
                content = content.replace("*", " ")
                file.seek(0)
                file.write(content)
                #file.truncate()

        with open(self.filename, "r") as file:
            self.labyrinth = [list(line.strip("\n")) for line in file]

        self.width = len(self.labyrinth[0])
        self.height = len(self.labyrinth)
        
        # Find start and finish positions
        for y, row in enumerate(self.labyrinth):
            for x, symbol in enumerate(row):
                if symbol == self.symbols["start"]:
                    self.start = (y, x)
                elif symbol == self.symbols["finish"]:
                    self.finish = (y, x)

        
        print(f"\nText file {self.filename} read successfully.")
        return self.labyrinth


    def write_to_html(self):
        html_file_path = self.filename.replace(".txt", ".html")

        if self.labyrinth is None:
            raise Exception("Labyrinth is not generated")
        else:
            html_content = "<html>\n<body>\n<table style='border: 1px solid grey; border-spacing: 0px;'>\n"
            for row in self.labyrinth:
                html_content += "<tr>\n"
                for symbol in row:
                    text = ""
                    if symbol == self.symbols["start"]:
                        current_color = LABYRINTH_HTML_COLOR["start"]
                        text = self.symbols["start"]
                    elif symbol == self.symbols["finish"]:
                        current_color = LABYRINTH_HTML_COLOR["finish"]
                        text = self.symbols["finish"]
                    elif symbol == self.symbols["wall"]:
                        current_color = LABYRINTH_HTML_COLOR["wall"]
                    elif symbol == self.symbols["tunnel"]:
                        current_color = LABYRINTH_HTML_COLOR["tunnel"]
                    elif symbol == self.symbols["pass_finish"]:
                        current_color = LABYRINTH_HTML_COLOR["pass_finish"]
                        text = self.symbols["pass_finish"]
                    elif symbol == self.symbols["pass_all"]:
                        current_color = LABYRINTH_HTML_COLOR["pass_all"]
                    html_content += f"<td style='background-color: {current_color}; border: 1px solid rgb(240, 241, 242); width: 20px; height: 20px; text-align: center; vertical-align: middle;'>{text}</td>\n"
                html_content += "</tr>\n"
            html_content += "</table>\n</body>\n</html>"

        with open(html_file_path, "w") as html_file:
            html_file.write(html_content)

        print(f"HTML file {html_file_path} created successfully\n")    



def find_solution(labyrinth, start, finish):
    start_node = Node(state=start, parent=None, action=None)
    frontier = QueueFrontier() #StackFrontier()
    #print(f"\nStart: {start_node.state}")

    frontier.add(start_node)
    explored = set()
    #print(f"Frontier: {[node_f.state for node_f in frontier.frontier]}")
    #print(f"Explored: {explored}")

    while True:
        if frontier.empty():
            print("\nSOLUTION: No solution")
            print(f"Explored: {len(explored)}")
            return "No solution"

        node = frontier.remove()
        #print(f"\nNode: {node.state}")
        if node.state == finish:
            actions = []
            cells = []
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
                if node.state != start and node.state != finish:
                    labyrinth.labyrinth[node.state[0]][node.state[1]] = LABYRINTH_SYMBOLS["pass_finish"]
            actions.reverse()
            cells.reverse()

            print("\nSOLUTION:")
            print(f"Way: {len(actions)}")
            print(f"Explored: {len(explored)}")
            print(f"Actions: {actions}")
            print(f"Nodes: {cells}")

            return actions, cells

        explored.add(node.state)
        if node.state != start:
            labyrinth.labyrinth[node.state[0]][node.state[1]] = LABYRINTH_SYMBOLS["pass_all"]
        
        neighbors = node.get_neighbors(labyrinth)
        #print(f"Neighbors: {[neighbor.state for neighbor in neighbors]}")

        for neighbor in neighbors:
            if not frontier.contains_state(neighbor.state) and neighbor.state not in explored:
               frontier.add(neighbor)
        
        #print(f"Frontier: {[node_f.state for node_f in frontier.frontier]}")
        #print(f"Explored: {explored}")
        


def main():
    # Create a new LabyrinthTXT object
    labyrinth = Labyrinth(LABYRINTH_SYMBOLS, FILE_NAME, NEW_FILE, LABYRINTH_WIDTH, LABYRINTH_HIGHT)

    if labyrinth.newfile == True:
        # Generate the labyrinth
        labyrinth.generate_labyrinth()
        # Write the labyrinth to a text file
        labyrinth.write_to_txt_file()
    else:
        # Read the labyrinth from a text file
        labyrinth.read_from_txt_file()

    # Find the solution
    find_solution(labyrinth, labyrinth.start, labyrinth.finish) 

    # Write the labyrinth to a text file
    labyrinth.write_to_txt_file()

    # Write the labyrinth to an HTML file
    if CRETE_HTML == True:
        labyrinth.write_to_html()


if __name__ == "__main__":
    main()