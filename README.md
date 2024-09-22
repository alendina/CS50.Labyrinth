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

# How to use

Python 3 is needed for running this Labyrinth project 

**The SolveLabyrinth.py module**

Running the SolveLabyrinth.py module allows:

The SolveLabyrinth.py module contains some constants to control the running modes:

- **METHOD**: (value: "DFS" or "BFS") sets the search method for finding the way from the start point to the finish point. BFS (Breadth-First Search) or DFS (Deep-First Search) methods are available;
- **CRETE_HTML**: (value: True or False ) the True value sets creating html file with Labyrinth that is based on the appropriate txt file;
- **NEW_FILE**: (value: True or False ) the True value sets generation of the new Labyrinth; False value sets reading the Labyrinth from the special txt file with a name from the FILE_NAME constant;
- **CLEAN_LABYRINTH**: (value: True or False ) the True value sets cleaning a special txt file with the Labyrinth from the previous solution before finding a new solution;
- **FILE_NAME** = (value: string, for example "" or "Labyrinth01.txt") the "" or None value is used during the automatic generation of file names with a numeration, the basis is taken from the  BASIC_PART_FILENAME constant; the string value like "Labyrinth01.txt" fixes the name of txt file with the Labyrinth which will be created in the current folder;
- **BASIC_PART_FILENAME**: (value: string, for example "Labyrinth") sets the basic part of txt and html file names with a numeration;
- **LABYRINTH_WIDTH**: (value: number) sets the dimension of the Labyrinth width;
- **LABYRINTH_HEIGHT**: (value: number) sets the dimension of the Labyrinth height;
- **PROBABILITIES**: (value: set, for example [0.4, 0.6, 0, 0, 0, 0]) sets the probability of symbols from the LABYRINTH_SYMBOLS constant; this probability is used during the Labyrinth generation; the length of the PROBABILY constant must be the same as the length of LABYRINTH_SYMBOLS;
- **LABYRINTH_SYMBOLS**: (value: dictionary, for example {"wall":"#", "tunnel":" ", "start":"A", "finish":"B", "pass_finish":"*", "pass_all":"."} the set of symbols used during the Labyrinth generation;
- **LABYRINTH_HTML_COLOR**: (value: dictionary, for example {"wall":"rgb(182, 180, 180)", "tunnel":"White", "start":"rgb(160, 160, 231)", "finish":"rgb(212, 159, 159)", "pass_finish":"rgb(149, 197, 149)", "pass_all":"rgb(243, 233, 156)"}) the set of colors used for html file;

The constant value can be changed for different needs before running the SolveLabyrinth.py module.

**The BuildLabyrintWithWay.py module**

Running the BuildLabyrintWithWay.py module allows repeatedly generating the Labyrinth as long as at least one way from the start point to the finish point will be found. The BuildLabyrintWithWay.py module actively uses functions and all settings from the SolveLabyrinth.py module.

# Example of usage

The folder of the Labyrinth project contains some generated samples.

Examples of txt and html files of the Labyrinth like as:


<img width="225" alt="Знімок екрана 2024-09-22 о 20 45 15" src="https://github.com/user-attachments/assets/e8c0690c-1db0-47b1-86f3-d4825cb481a4">

<img width="527" alt="Знімок екрана 2024-09-22 о 20 45 49" src="https://github.com/user-attachments/assets/61217e0d-4a4d-43ba-954e-2be5cb6ebec1">


Example of the result in the console:

<img width="560" alt="Знімок екрана 2024-09-22 о 21 20 23" src="https://github.com/user-attachments/assets/5d44d571-dcbf-4f79-830a-b77ec8410994">

or

<img width="175" alt="Знімок екрана 2024-09-22 о 21 20 36" src="https://github.com/user-attachments/assets/76edf9ca-2587-404d-b7a6-e9fb116108b3">

 
