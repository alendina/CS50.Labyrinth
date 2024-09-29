import random
from a_star_search import LabyrinthASS
import util 

# Constants
ATTEMPTS_OF_GENARATION = 100000
NEEDED_TUNNEL_LENGTH = 100

LABYRINTH_WIDTH = 40
LABYRINTH_HEIGHT = 30
PROBABILITIES = [0.45, 0.55, 0, 0, 0, 0] # the same length as the number of LABYRINTH_SYMBOLS: wall, tunnel, start, finish, pass_finish, pass_all
NEW_FILE = False
BASE_FILENAME = "G"
FILE_NAME = "G02.txt" # "G01.txt" or "" or None
CLEAN_LABYRINTH = True
CRETE_HTML = True


def random_generation(labyrinth):
        labyrinth.labyrinth = []
        
        labyrinth.labyrinth = [
            random.choices(
                population=list(labyrinth.symbols.values()),
                weights=PROBABILITIES,
                k=labyrinth.width
            )
            for _ in range(labyrinth.height)
        ]

        start_pos = [random.randint(0, labyrinth.width - 1), random.randint(0, labyrinth.height - 1)]
        labyrinth.labyrinth[start_pos[1]][start_pos[0]] = labyrinth.symbols["start"]
        labyrinth.start = (start_pos[1], start_pos[0])

        finish_pos = [random.randint(0, labyrinth.width - 1), random.randint(0, labyrinth.height - 1)]
        labyrinth.labyrinth[finish_pos[1]][finish_pos[0]] = labyrinth.symbols["finish"]
        labyrinth.finish = (finish_pos[1], finish_pos[0])

        return labyrinth.labyrinth
        

def main():
    count = 0
    while count < ATTEMPTS_OF_GENARATION:
        labyrinth = LabyrinthASS(FILE_NAME) 
        labyrinth.method = "ASS"
        labyrinth.width = LABYRINTH_WIDTH
        labyrinth.height = LABYRINTH_HEIGHT
        labyrinth.labyrinth = random_generation(labyrinth)
        labyrinth.heuristics = labyrinth.get_heuristics(labyrinth.finish)

        solution = labyrinth.search() # by A* Mathod
        
        if solution != "No solution" and len(solution[0]) > NEEDED_TUNNEL_LENGTH:
            print(f"\nCount of generation: {count+1}")
            break
        count += 1

    if NEW_FILE == True:
        labyrinth.filename = util.generate_next_txt_filename(BASE_FILENAME)
    labyrinth.write_to_txt_file()
    
    if CRETE_HTML == True:
        labyrinth.write_to_html(clean=True, numbers=None)


if __name__ == "__main__":
    main()