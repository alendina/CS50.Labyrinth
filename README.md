# Labyrinth
Build the Labyrinth and find the solution using BFS (Breadth-First Search) or DFS (Deep-First Search)

**Version 1.0** 

Contain basic opportunities:

  - Generate the Labyrinth with walls, tunnels, start point, finish point;
  - Write in a specific text file with the Labyrinth using the automation generation of the file name;
  - Find the solution to the Labyrinth using BFS (Breadth-First Search) or DFS (Deep-First Search). Show the path from the start point to the finish point, necessary steps and discovered nodes;
  - Can read the Labyrinth from a specific text file without generation
  - Write the solution of the Librarian in a text file and an HTML file

**Version 2.0**

Add some new fitches:

- Different probability for  "walls" and "tunnels" is used  during the generation;
- Add constants: 
    METOD (to choose the generation method BFS or DFS);
    PROBABILITIES (to set the probability of "walls" and "tunnels" during the Labyrinth generation;
    BASIC_PART_FILENAME (to set the basic part of txt and html file name)


**Example of usage**

Example of txt file of the Labyrinth:
<img width="225" alt="Знімок екрана 2024-09-22 о 20 45 15" src="https://github.com/user-attachments/assets/e8c0690c-1db0-47b1-86f3-d4825cb481a4">

Example of html file of the Labyrinth:
<img width="586" alt="Знімок екрана 2024-09-22 о 20 45 49" src="https://github.com/user-attachments/assets/a1f2f1e3-6e72-48dd-bad5-23a9ce3bc8ca">

Example of the result in the console:

SOLUTION:
Way: 8
Explored: 53
Actions: ['Right', 'Right', 'Up', 'Up', 'Up', 'Right', 'Right', 'Right']
Nodes: [(6, 8), (6, 9), (5, 9), (4, 9), (3, 9), (3, 10), (3, 11), (3, 12)]

SOLUTION: No solution
Explored: 339
