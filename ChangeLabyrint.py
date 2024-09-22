import _labyrinth 

def main():
    # Create a new LabyrinthTXT object
    _labyrinth.labyrinth = _labyrinth.Labyrinth(_labyrinth.LABYRINTH_SYMBOLS, _labyrinth.FILE_NAME, _labyrinth.NEW_FILE, _labyrinth.LABYRINTH_WIDTH, _labyrinth.LABYRINTH_HIGHT)
    
    count = 0
    while count < 100000:
        # Generate the labyrinth
        _labyrinth.labyrinth.generate_labyrinth()
        solution = _labyrinth.find_solution(_labyrinth.labyrinth, _labyrinth.labyrinth.start, _labyrinth.labyrinth.finish)
        
        if solution != "No solution" and len(solution[0]) > 77:
            print(f"\nCount of generation: {count}")
            break
        count += 1

    # Write the labyrinth to a text file
    _labyrinth.labyrinth.write_to_txt_file()
    
    # Write the labyrinth to an HTML file
    if _labyrinth.CRETE_HTML == True:
        _labyrinth.labyrinth.write_to_html()


if __name__ == "__main__":
    main()