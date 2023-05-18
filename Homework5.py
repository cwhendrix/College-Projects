### Programming Homework 5: Sequence Alignment with Dynamic Programming ###
### Cooper Hendrix ###
### CSC 370 - Dr. Bailey ###
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def trace_strings(table, s1, s2):
    i = 0
    j = 0
    sol1 = ""
    sol2 = ""
    while i != len(s1) or j != len(s2):
      penalty = 0
      ## Find Next Array Item ##
      if table[i][j+1] + 2 == table[i][j]: # gap in s1, move to right
        sol1 += " "
        sol2 += s2[j]
        j += 1
      elif table[i+1][j] + 2 == table[i][j]: # gap in s2, move down
        sol1 += s1[i]
        sol2 += " "
        i += 1
      else: # move diagonally; mismatch or identical character
        if s1[i] != s2[j]:  # mismatch
          penalty = 1
        if table[i+1][j+1] + penalty == table[i][j]:
          sol1 += s1[i]
          sol2 += s2[j]
          i += 1
          j += 1
      print("solution 1:", sol1)
      print("solution 2:", sol2)
    return (sol1, sol2)

def trav_table(table, i: int, j: int, s1: str, s2: str):
    opt = 0
    penalty = 0
    if i == len(s1):
        opt = 2*(len(s2) - j)
    elif j == len(s2):
        opt = 2*(len(s1) - i)
    else:
        if s1[i] == s2[j]:
          penalty = 0
        else:
          penalty = 1
        if table[i][j+1] != -1:
           min1 = table[i][j+1] + 2
        else:
           min1 = trav_table(table, i, j+1, s1, s2) + 2
        if table[i+1][j+1] != -1:
           min3 = table[i+1][j+1] + penalty
        else:
           min3 = trav_table(table, i+1, j+1, s1, s2) + penalty
        if table[i+1][j] != -1:
           min2 = table[i+1][j] + 2
        else:
           min2 = trav_table(table, i+1, j, s1, s2) + 2
        opt = min(min1, min2, min3)
    # print("Index", i, j, "=", opt)
    table[i][j] = opt
    return opt


def align_sequences_recursive(s1: str, s2: str) -> tuple[str, str]:
    table = [[-1 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    summ = trav_table(table, 0, 0, s1, s2)
    print(table)
    solutions = trace_strings(table, s1, s2)
    print(solutions)

def align_sequences_iterative(s1: str, s2: str) -> tuple[str, str]:
    table = [[-1 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
      comp1 = len(s1) - i
      for j in range(len(s2) + 1):
        comp2 = len(s2) - j
        if comp1 == len(s1):
          table[comp1][comp2] = 2*(len(s2) - comp2)
        elif comp2 == len(s2):
          table[comp1][comp2] = 2*(len(s1) - comp1)
        else:
          penalty = 0
          if s1[comp1] != s2[comp2]:
            penalty = 1
          table[comp1][comp2] = min(table[comp1+1][comp2+1] + penalty, table[comp1+1][comp2] + 2, table[comp1][comp2 + 1] + 2)
    
    solutions = trace_strings(table, s1, s2)
    print(solutions)


s1 = "AACAGTTACC"
s2 = "TAAGGTCA"

# Two test sequences. Call your functions on these!
#s1 = "GGGCAGTAAGAGACTCGACCCGTCTACACGATAAGGTCTACAGAAGATTATTTTTACCTAAGTGGACGACAACGTCACGGCATGCACCCGTTCTTGAA"
#s2 = "GATTAGCGGAGCAGTAAGAGACTCGACCCGTTACTCGATAAGGTCTACAGAAGATTATTTTACCTAAGTGGACGACAATGTCACTGGCATGCACCCGTTCTTGAA"

strings = align_sequences_recursive(s1, s2)
strings = align_sequences_iterative(s1, s2)



