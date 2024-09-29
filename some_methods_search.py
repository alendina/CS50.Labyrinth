from broad_ferst_search import LabyrinthBFS
from deep_first_search import LabyrinthDFS
from a_star_search import LabyrinthASS


# Constants 
FILE_NAME = "G02.txt"
CRETE_HTML = True

def main():
    # Search of the DMS method
    labyrinth = LabyrinthDFS(FILE_NAME)
    labyrinth.method = "DFS"
    labyrinth.read_from_txt_file()
    labyrinth.search()
    labyrinth.write_to_html(clean=True, numbers=None)
    
    # Search of the BMS method
    labyrinth = LabyrinthBFS(FILE_NAME)
    labyrinth.method = "BFS"
    labyrinth.read_from_txt_file()
    labyrinth.search()
    labyrinth.write_to_html(clean=False, numbers=None)

    # Search of the A* method
    labyrinth = LabyrinthASS(FILE_NAME)
    labyrinth.method = "ASS"
    labyrinth.read_from_txt_file()
    labyrinth.heuristics = labyrinth.get_heuristics(labyrinth.finish)
    labyrinth.search()
    labyrinth.write_to_html(clean=False, numbers=labyrinth.heuristics)


if __name__ == "__main__":
    main()
    