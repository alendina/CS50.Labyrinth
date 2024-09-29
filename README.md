# Labyrinth Project
Build the Labyrinth in two different ways: Tunnel Method of Generation and Random Method of Generation and find the solution using BFS (Breadth-First Search), DFS (Deep-First Search), ASS (A* Search) Methods

**Version 1.0** 

Contain basic opportunities:

  - to generate the Labyrinth with walls, tunnels, start point, finish point;
  - to write in a special text file with the Labyrinth using the automation generation of the file name;
  - to find the solution to the Labyrinth using BFS (Breadth-First Search) or DFS (Deep-First Search) methods. Show the path from the start point to the finish point, necessary steps and discovered nodes;
  - to read the Labyrinth from a specific text file without generation
  - to write the solution of the Labyrinth in a specific text file and an HTML file

**Version 2.0**

Added some new features:

- Different probability for  "walls" and "tunnels" is used  during the generation;
- Added constants: 
    METOD (to choose the generation method BFS or DFS);
    PROBABILITIES (to set the probability of "walls" and "tunnels" during the Labyrinth generation);
    BASIC_PART_FILENAME (to set the basic part of txt and html file name)

**Version 3.0**

Added some new features:

- Add A* Search Method for solving the Labyrinth
- Add Tunnel Method of the Labyrinth generation

Done a big restructuring of the modules

# How to use

Python 3 is needed for running this Labyrinth project 

# Generation

**The generate_by_tunnels.py module**

The generate_by_tunnels.py module allows to generate of the Labyrint by combining some random tunnels with 10-15 steps of length. You can control some parameters of the generation by changing the constant value of this module:   
- you can set the width and height of the Labyrint by **LABYRINTH_WIDTH** and **LABYRINTH_HEIGHT** 
- you can control the ratio between walls and tunnels of the Labyrint using **PROBABILITIES** = [0.3, 0.7, 0, 0, 0, 0] - sets the probability of symbols from the **LABYRINTH_SYMBOLS** constant (from util module) as wall, tunnel, start, finish, pass_finish, pass_all
- you can write the generated Labyrinth to a new special txt file (**NEW_FILE** = True, **FILE_NAME** = None or «», **BASE_FILENAME** = «G») with automatically generated numbers like «G02.txt»; or you can rewrite a file that exists  (**NEW_FILE** = False, b = "G01.txt") 
- you can also create html file set  **CRETE_HTML** = True

**The generate_by_random.py module**

The generate_by_random.py module allows to generate of the Labyrint by randomly distributed symbols of walls and tunnels, and the  Start and Finish position.

You can control the same parameters as the tunnel generation module. 

In generate_by_random.py the main generation is repeated many times so far will be created the Labyrinth with at least one solution of a certain length. You can control this with **ATTEMPTS_OF_GENARATION** and **NEEDED_TUNNEL_LENGTH** constants.

The constant value can be changed for different needs before running the required module.


# Searching

You can find the solution to the Labyrinth using **BFS** (Breadth-First Search), **DFS** (Deep-First Search) or **ASS** (A* Search) Methods. Three modules are responsible for each method:
**deep_first_search.py**
**broad_ferst_search.py**
**a_star_search.py**

Each module reads the Labyrinth from a special txt file created using generate_by_random.py or generate_by_random.py modules or by hand. 
The name of this special txt file you can set in **FILE_NAME** constant.
The solution of the Labyrinth will be written in an appropriate txt file and html file (if set **CRETE_HTML** = True) and will show the path from the start point to the finish point, necessary steps, and discovered nodes.

Using the **some_methods_search.py** allows finding the solution of the Labyrint consecutively by three methods DFS, BFS, ASS, and the solution will be written in one html file.

After finding the solution the information will be shown in the console as the path from the start point to the finish point, the necessary steps, and discovered nodes.

# Other

The **util.py** module contains some service functions and constants like: 
- **LABYRINTH_SYMBOLS**: (value: dictionary, for example {"wall":"#", "tunnel":" ", "start":"A", "finish":"B", "pass_finish":"*", "pass_all":"."} the set of symbols used during the Labyrinth generation;
- **LABYRINTH_HTML_COLOR**: (value: dictionary, for example {"wall":"rgb(182, 180, 180)", "tunnel":"White", "start":"rgb(160, 160, 231)", "finish":"rgb(212, 159, 159)", "pass_finish":"rgb(149, 197, 149)", "pass_all":"rgb(243, 233, 156)"}) the set of colors used for html file;

It can be changed if it is needed


# Examples of usage

The folder Samples contains some generated samples of the Labyrinth project.

Examples of txt and html files of the Labyrinth like as:

<img width="506" alt="Знімок екрана 2024-09-29 о 21 29 26" src="https://github.com/user-attachments/assets/c23e1157-fa75-4dd3-bf03-412f2ac226a4">

Example of the result in the console:

<img width="560" alt="Знімок екрана 2024-09-22 о 21 20 23" src="https://github.com/user-attachments/assets/5d44d571-dcbf-4f79-830a-b77ec8410994">

or

<img width="175" alt="Знімок екрана 2024-09-22 о 21 20 36" src="https://github.com/user-attachments/assets/76edf9ca-2587-404d-b7a6-e9fb116108b3">

 
