# Labyrinth Project
Build the Labyrinth and find the solution using BFS (Breadth-First Search) or DFS (Deep-First Search)

**Version 1.0** 

Contain basic opportunities:

  - to generate the Labyrinth with walls, tunnels, start point, finish point;
  - to write in a specific text file with the Labyrinth using the automation generation of the file name;
  - to find the solution to the Labyrinth using BFS (Breadth-First Search) or DFS (Deep-First Search). Show the path from the start point to the finish point, necessary steps and discovered nodes;
  - to read the Labyrinth from a specific text file without generation
  - to write the solution of the Labyrinth in a specific text file and an HTML file

**Version 2.0**

Added some new features:

- Different probability for  "walls" and "tunnels" is used  during the generation;
- Added constants: 
    METOD (to choose the generation method BFS or DFS);
    PROBABILITIES (to set the probability of "walls" and "tunnels" during the Labyrinth generation);
    BASIC_PART_FILENAME (to set the basic part of txt and html file name)

# HOW TO USE

Python 3 is needed for running this Labyrinth project 

**SolveLabyrinth.py**

Runing SolveLabyrinth.py file allows:

SolveLabyrinth.py contains some constants for control the running modes:

METOD: (value: "DFS" or "BFS")
CRETE_HTML: (value: True or False )
NEW_FILE: (value: True or False )
CLEAN_LABYRINTH: (value: True or False )
FILE_NAME = (value: string, for example "Labyrinth01.txt")
BASIC_PART_FILENAME: (value: string, for example "Labyrinth")
LABYRINTH_WIDTH = 40
LABYRINTH_HIGHT = 40
PROBABILITIES = [0.4, 0.6, 0, 0, 0, 0] # the same length as the number of LABYRINTH_SYMBOLS
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

BuildLabyrintWithWay.py

# Example of usage

Folder of the Labyrinth project contains some generated semples.

Example of txt and html files of the Labyrinth like as:


<img width="225" alt="Знімок екрана 2024-09-22 о 20 45 15" src="https://github.com/user-attachments/assets/e8c0690c-1db0-47b1-86f3-d4825cb481a4">

<img width="527" alt="Знімок екрана 2024-09-22 о 20 45 49" src="https://github.com/user-attachments/assets/61217e0d-4a4d-43ba-954e-2be5cb6ebec1">


Example of the result in the console:

<img width="560" alt="Знімок екрана 2024-09-22 о 21 20 23" src="https://github.com/user-attachments/assets/5d44d571-dcbf-4f79-830a-b77ec8410994">

or

<img width="175" alt="Знімок екрана 2024-09-22 о 21 20 36" src="https://github.com/user-attachments/assets/76edf9ca-2587-404d-b7a6-e9fb116108b3">

 
