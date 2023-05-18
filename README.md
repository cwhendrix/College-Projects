# College-Projects
Repository of sample code from projects completed while in college. Each class is given its own folder within the repository.

## CSC 370 - Design and Analysis of Algorithms, Dr. William Bailey - Spring 2023
An introduction to the theoretical and empirical evaluation of algorithms and to some fundamental concepts in algorithm design and implementation. Topics include best-, worst-, and average-case performance, complexity classes, problem-solving strategies, and NP-complete problems.

### Homework 1 - Brute-Force Algorithm for Traveling Salesman Problem
Files: Homework1.py, knapsack_input.txt
Reads a file named knapsack_input.txt specifying an instance of the knapsack problem. The file will contain repeating blocks of three lines with this format:
- Item_name (a string of at most 32 characters)
- Item_weight (an integer)
- Item_value (an integer)
Your program may assume that the number of lines in the file is a multiple of three. A
sample input file can be found on Moodle. Interactively ask the user for the knapsack’s weight limit. This should be an integer. Solve the knapsack problem using a brute force algorithm, testing all possible item combinations. To get credit for this, you must not use external libraries or packages (e.g. Python’s itertools) to generate these combinations. You should use the array incrementing method we discussed in class to generate the combinations. Write the information about each combination to a file named output.txt as a block
of three lines:
- Combination_string (a binary string describing combination, 1 means take the item, 0 means don’t take it)
- Combination_total_weight (an integer)
- Combination_total_value (an integer)
For example, a combination in which only the TV (2nd item) and penny collection (10th item) are taken, write this (see the sample file for the complete list of items
010000000100000
1480
420
As the last three lines, write the information about the optimal combination, in the format described above. Please don’t write anything else into the file.

### Homework 2 - Greedy Algorithm for Traveling Salesman Problem
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
