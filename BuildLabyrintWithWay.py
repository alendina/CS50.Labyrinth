import SolveLabyrinth 

def main():
    # Create a new LabyrinthTXT object
    SolveLabyrinth.labyrinth = SolveLabyrinth.Labyrinth(SolveLabyrinth.LABYRINTH_SYMBOLS, SolveLabyrinth.FILE_NAME, SolveLabyrinth.NEW_FILE, SolveLabyrinth.LABYRINTH_WIDTH, SolveLabyrinth.LABYRINTH_HIGHT)
    
    count = 0
    while count < 100000:
        # Generate the labyrinth
        SolveLabyrinth.labyrinth.generateSolveLabyrinth()
        solution = SolveLabyrinth.find_solution(SolveLabyrinth.labyrinth, SolveLabyrinth.labyrinth.start, SolveLabyrinth.labyrinth.finish)
        
        if solution != "No solution" and len(solution[0]) > 100:
            print(f"\nCount of generation: {count}")
            break
        count += 1

    # Write the labyrinth to a text file
    SolveLabyrinth.labyrinth.write_to_txt_file()
    
    # Write the labyrinth to an HTML file
    if SolveLabyrinth.CRETE_HTML == True:
        SolveLabyrinth.labyrinth.write_to_html()


if __name__ == "__main__":
    main()