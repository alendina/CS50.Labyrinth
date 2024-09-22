import os
import random

class Labyrinth:
    def __init__(self, width, height, symbols, probabilities):
        self.width = width
        self.height = height
        self.symbols = symbols
        self.probabilities = probabilities
        self.labyrinth = self.generate_labyrinth()
        self.filename = None

    def generate_labyrinth(self):
        # Generate the labyrinth with the specified probabilities
        labyrinth = [
            random.choices(
                population=list(self.symbols.values()),
                weights=self.probabilities,
                k=self.width
            )
            for _ in range(self.height)
        ]
        # Mark Start Labyrinth
        a = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
        labyrinth[a[0]][a[1]] = self.symbols["start"]
        # Mark Finish Labyrinth
        b = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
        labyrinth[b[0]][b[1]] = self.symbols["finish"]

        self.print_labyrinth(labyrinth)
        return labyrinth

    def print_labyrinth(self, labyrinth):
        for row in labyrinth:
            print(*row)
        print()  # Add an extra newline for better readability

    def generate_next_file_name(self, file_name="Labyrinth"):
        folder = os.getcwd()
        files = os.listdir(folder)
        txt_files = [f for f in files if f.startswith(file_name) and f.endswith(".txt")]
        next_number = len(txt_files) + 1
        new_file_name = f"{file_name}{next_number:02}.txt"
        return os.path.join(folder, new_file_name)

    def write_to_txt_file(self):
        if self.filename is None:
            self.filename = self.generate_next_file_name()
        
        if self.labyrinth is None:
            raise Exception("Labyrinth is not generated")
        else:
            with open(self.filename, "w") as new_file:
                for row in self.labyrinth:
                    new_file.write("".join(row) + "\n")
            print("\n", self.filename, "\n New text file created successfully. \n")

    def read_from_txt_file(self):
        if self.filename is None:
            raise Exception("Filename is not provided")
        with open(self.filename, "r") as file:
            content = file.read()
        return content

# Example usage
symbols = {
    "wall": "#",
    "tunnel": ".",
    "start": "A",
    "finish": "B"
}

# Define the probabilities for each symbol
probabilities = [0.4, 0.6, 0, 0]  # 30% for wall, 70% for tunnel, 0% for start, 0% for finish

labyrinth = Labyrinth(20, 20, symbols, probabilities)
labyrinth.filename = "Probability01.txt"
labyrinth.write_to_txt_file()

# Reading from the created file
file_content = labyrinth.read_from_txt_file()
print(file_content)

# Writing to the created file
labyrinth.write_to_txt_file()
