# College-Projects
Repository of sample code from projects completed while in college. Each class is given its own folder within the repository.

## CSC 370 - Design and Analysis of Algorithms, Dr. William Bailey - Spring 2023
An introduction to the theoretical and empirical evaluation of algorithms and to some fundamental concepts in algorithm design and implementation. Topics include best-, worst-, and average-case performance, complexity classes, problem-solving strategies, and NP-complete problems.

### Homework 1 - Brute-Force Algorithm for Knapsack Problem
Files: Homework1.py, knapsack_input.txt

Reads a file named knapsack_input.txt specifying an instance of the knapsack problem. The file will contain repeating blocks of three lines with this format:
- Item_name (a string of at most 32 characters)
- Item_weight (an integer)
- Item_value (an integer)

Your program may assume that the number of lines in the file is a multiple of three. A sample input file can be found on Moodle. Interactively ask the user for the knapsack’s weight limit. This should be an integer. Solve the knapsack problem using a brute force algorithm, testing all possible item combinations. To get credit for this, you must not use external libraries or packages (e.g. Python’s itertools) to generate these combinations. You should use the array incrementing method we discussed in class to generate the combinations. Write the information about each combination to a file named output.txt as a block
of three lines:
- Combination_string (a binary string describing combination, 1 means take the item, 0 means don’t take it)
- Combination_total_weight (an integer)
- Combination_total_value (an integer)

For example, a combination in which only the TV (2nd item) and penny collection (10th item) are taken, write this (see the sample file for the complete list of items
010000000100000
1480
420
As the last three lines, write the information about the optimal combination, in the format described above. Please don’t write anything else into the file.

### Homework 2 - Greedy Algorithm for Knapsack Problem
Files: Homework2.py, knapsack_input.txt

Reads a file named knapsack_input.txt specifying an instance of the knapsack problem. The file will contain repea=ng blocks of three lines with this format:
- Item_name (a string of at most 32 characters)
- Item_weight (an integer)
- Item_value (an integer)

Your program may assume that the number of lines in the file is a multiple of three. A sample input file can be found on Moodle. Interactively ask the user for an integer represen=ng the knapsack’s weight limit. Solve the knapsack problem twice using two different selecton procedures:
- selecting the most valuable feasible item, and
- selecting feasible item with the best value to weight ratio.

Print each solution to the standard output (the terminal) with labels on solutions, as well as the weights and values, like this:
High value heuristic:
w: 42
v: 320
Value to weight heuristic:
w: 40
v: 332
You do not need to write to a file.

### Homework 3 - Branch-and-Bound Algorithm for Traveling Salesperson Problem
Files: Homework3.py, city_distances.csv

Write a program in C/++, Java, or Python which Reads a file named city_distances.csv specifying an instance of the Travelling Salesperson problem. The file will contain an n-by-n table of distances between cities in this format:

city name,Toronto,Seattle,Santa Fe,Cleveland

Toronto,0,4147,2862,469

Seattle,4147,0,2325,3834

Santa Fe,2862,2325,0,2544

Cleveland,469,3834,2544,0

You can use this data as a test case; copy it into a .csv file. Solve the instance of TSP given by the file. Report both the number of kilometers travelled, and the tour (sequence of cities).

### Homework 4 - Genetic Algorithm for Traveling Salesperson Problem
Files: Homework4.py

In particular, your program should interactively gather:
- a number of cities, and
- a number of iterations to run, and optionally,
- a probability of random mutations (swapping adjacent cities).

Randomly generate the specified number of cities as points in a 2D grid according to a Normal 𝑁(𝜇=0,𝜎=1) distribution. Run the NNX algorithm for the specified number of iterations, tracking the quality of the best solution in the set at each generation. You do not need to introduce random mutations, but you can if you wish. Initialize the pool of solutions at random, and be careful to keep the population size constant from one generation to the next.
Output:
- the quality of the best know solution at the final generation, and
- a plot of the solution quality over time. This plot should have the generation number on the horizontal axis, and the total distance between all cities in the tour on the vertical axis.

### Homework 5 - Dynamic Programming and Iterative Algorithms for Sequence Alignment
Files: Homework5.py

This assignment asks you to implement the DNA sequence alignment algorithm we talked about earlier this semester. In particular, it asks for two versions. One which is completely iterative, and one which is recursive, but stores the result of each recursive call for later use.

### Project - (Directed) Hamiltonian Paths
Files: ProjectV2.py

This project asks you to write a program to solve and NP-complete problem. You are already somewhat familiar with the difficulties involved in solving NP-Complete problems-- at least in theory. This assignment will give you a deeper appreciation for these difficulties and allow you to apply the techniques you have learned this semester to overcome them. You have been assigned into teams for this project. You will write a brute force algorithm that will solve the problem, as well as at least one other algorithm. 

In the **Hamiltonian Path Problem**, you are given a directed graph *G*. Your job is to determine if there is a path in *G* which passes through each vertex exactly once. 
