### Programming Homework 2: Greedy Solution to Knapsack Problem ###
### Cooper Hendrix ###
### CSC 370 - Dr. Bailey ###

### Make Arrays Function ###
# Creates and returns three parallel arrays; one representing the values,
# one representing the weights, and one with the value/weight ratio.
def makeArrays():
    inputFile = open("knapsack_input.txt", "r")
    i = 0
    values = []
    weights = []
    ratios = []
    currRatio = float(0)
    curr = inputFile.readline()
    # Enter while loop
    while (curr != ""):
        if i%3 != 0:    # skips if its a name of an item
            if i%3 == 1:    # number is a weight
                weights.append(int(curr))
                currRatio += float(curr)
            if i%3 == 2:    # number is a value
                values.append(int(curr))
                # calculate ratio and add to ratios array
                currRatio = float(curr) / currRatio 
                ratios.append(currRatio)
                currRatio = float(0)
        i += 1
        curr = inputFile.readline()
    # Close file
    inputFile.close()
    return values, weights, ratios

### Bubble Sort Function ###
# Performs Bubble Sort on the parallel arrays.
# I could've sorted the items as they were being inserted, but I wanted
# to break it up and make sure I wasn't making any huge mistakes.
# The toggle set to "true" indicates sorting by values and weights.
# The toggle set to "false" indicates sorting by value/weight ratios.
# Returns the sorted parallel arrays.
def bubbleSort(values, weights, ratios, toggle):
    length = len(values)
    if toggle:  # Sorting by greatest value
        for i in range(length):
            for j in range(0, length - i - 1):
                if values[j] <= values[j+1]:
                    # swap
                    values[j], values[j+1] = values[j+1], values[j]
                    weights[j], weights[j+1] = weights[j+1], weights[j]
                    ratios[j], ratios[j+1] = ratios[j+1], ratios[j]
    else:       # Sorting by largest value per unit of weight
        for i in range(length):
            for j in range(0, length - i - 1):
                if ratios[j] <= ratios[j+1]:
                    # swap
                    values[j], values[j+1] = values[j+1], values[j]
                    weights[j], weights[j+1] = weights[j+1], weights[j]
                    ratios[j], ratios[j+1] = ratios[j+1], ratios[j]
    return values, weights, ratios

### HVTest Function ###
# This tests the procedure of selecting the most valuable item
# which can fit in the knapsack.
# Returns the value and weight of the items in the knapsack
def HVTest(values, weights, limit):
    weightLeft = limit
    bValue = 0
    bWeight = 0
    i = 0
    # if we know we can't fit the smallest item in the bag, we know we've filled it as much as possible
    while limit - bWeight >= weights[len(weights) - 1] and i < len(weights) and weightLeft > 0:
        if weights[i] <= weightLeft:
            weightLeft -= weights[i]
            bValue += values[i]
            bWeight += weights[i]
        i += 1
    return bValue, bWeight

### VWTest Function ###
# This tests the procedure of selecting the item with the greatest value to weight ratio.
# Largely the same as HVTest, but removes a condition which allows the loop to end early
# if we know we can't fit anything else in the bag.
# Returns the value and weight of the items in the knapsack
def VWTest(values, weights, limit):
    weightLeft = limit
    bValue = 0
    bWeight = 0
    i = 0
    while i < len(weights) and weightLeft > 0:
        if weights[i] <= weightLeft:
            weightLeft -= weights[i]
            bValue += values[i]
            bWeight += weights[i]
        i += 1
    return bValue, bWeight

### Main Function ##
def main():
    limit = input("Please enter the weight limit of the knapsack. ")
    limit = int(limit)
    # Create Arrays #
    values, weights, ratios = makeArrays()
    
    # Sort Arrays by High Value Heuristic #
    values, weights, ratios = bubbleSort(values, weights, ratios, True)

    # Perform High Value Test #
    hvValue, hvWeight = HVTest(values, weights, limit)
    print("High value heuristic:")
    print("w:", hvWeight)
    print("v:", hvValue)

    # Sort Arrays by Value to Weight Heuristic #
    values, weights, ratios = bubbleSort(values, weights, ratios, False)

    # Perform Value to Weight Test #
    rValue, rWeight = VWTest(values, weights, limit)
    print("Value to weight heuristic:")
    print("w:", rWeight)
    print("v:", rValue)

### Main Function Call ###
main()
