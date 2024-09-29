import random
import util
from util import Labyrinth, generate_next_txt_filename

# Constants
LABYRINTH_WIDTH = 40
LABYRINTH_HEIGHT = 50
PROBABILITIES = [0.3, 0.7, 0, 0, 0, 0] # the same length as the number of LABYRINTH_SYMBOLS: wall, tunnel, start, finish, pass_finish, pass_all
NEW_FILE = False
BASE_FILENAME = "G"
FILE_NAME = "G01.txt" # "G01.txt" or "" or None
CLEAN_LABYRINTH = True
CRETE_HTML = True


def tunnel_generation(width, height):
    def get_neighbors(cell):
        neighbors = []
        # Check cell Up
        if cell[0]-1 >= 0:
            neighbors.append((cell[0]-1, cell[1]))
        # Check cell Down
        if cell[0]+1 <= height-1:
            neighbors.append((cell[0]+1, cell[1]))
        # Check cell Left
        if cell[1]-1 >= 0:
            neighbors.append((cell[0], cell[1]-1))
        # Check cell Right
        if cell[1]+1 <= width - 1:
            neighbors.append((cell[0], cell[1]+1))
        return neighbors

    wall_symbol = util.LABYRINTH_SYMBOLS["wall"]
    tunnel_symbol = util.LABYRINTH_SYMBOLS["tunnel"]
    start_symbol = util.LABYRINTH_SYMBOLS["start"]
    
    labyrinth = []
    
    for _ in range(height):
        row = [wall_symbol] * width
        labyrinth.append(row)

    start_a = (random.randint(0, height - 1), random.randint(0, width - 1))
    labyrinth[start_a[0]][start_a[1]] = start_symbol
    
    tunnels = [start_a]
    cell = start_a
    previous_cell = start_a
    leinght_full_tunnel = 0
    while True:
        num = 0
        leinght_peace_tunnel = random.randint(10, 15)
        while num < leinght_peace_tunnel:
            # Repeat for each peace of the tunnel 

            neighbors = get_neighbors(cell)
            if previous_cell in neighbors:
                neighbors.remove(previous_cell)

            # Add a cell to the neighbors list for the tunnel to continue in the same direction with more probability
            add_cell = []
            if previous_cell[0] == cell[0]:
                add_cell = (cell[0], cell[1] + 1)
            elif previous_cell[1] == cell[1]:
                add_cell = (cell[0] + 1, cell[1])
            if add_cell in neighbors:    
                neighbors.append(add_cell)
                # To increase the probability of the tunnel to continue in the same direction
                neighbors.append(add_cell)
                neighbors.append(add_cell)
                neighbors.append(add_cell)

            next_cell = random.choice(neighbors)
            tunnels.append(next_cell)
            #print(tunnels)
            labyrinth[next_cell[0]][next_cell[1]] = tunnel_symbol
            
            previous_cell = cell
            cell = next_cell
            num += 1
        
        # Check if the leinght of all tunnels is long enough
        leinght_full_tunnel += leinght_peace_tunnel
        if leinght_full_tunnel >= int(PROBABILITIES[1] * width * height):
            print(leinght_full_tunnel)
            break

        start = (random.randint(0, height - 1), random.randint(0, width - 1))
        tunnels = [start]
        cell = start
        previous_cell = start

    finish = tunnels[-1]
    labyrinth[finish[0]][finish[1]]= util.LABYRINTH_SYMBOLS["finish"]
    labyrinth[start_a[0]][start_a[1]]= start_symbol

    print(f"The Labyrinth generated successfully by Tunnels Method!")  
    return labyrinth
   
def main():
    labyrinth = Labyrinth(FILE_NAME) 
    labyrinth.width = LABYRINTH_WIDTH
    labyrinth.height = LABYRINTH_HEIGHT

    labyrinth.labyrinth = tunnel_generation(labyrinth.width, labyrinth.height)

    if NEW_FILE == True:
        labyrinth.filename = generate_next_txt_filename(BASE_FILENAME)
    labyrinth.write_to_txt_file()
    
    if CRETE_HTML == True:
        labyrinth.write_to_html(clean=True, numbers=None)
  

if __name__ == "__main__":
    main()  