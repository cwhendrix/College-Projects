### Programming Homework 1: The Knapsack Problem ###
### Cooper Hendrix ###
### CSC 370 - Dr. Bailey ###

### Make Array Function ###
# Creates and returns an array with each line of the file.
# It also returns the number of possible items.
# We'll use these to test each combination of the items. 
def makeArray():
    inputFile = open("knapsack_input.txt", "r")
    itemArray = inputFile.readlines()
    numItems = len(itemArray) / 3
    inputFile.close()
    return itemArray, int(numItems)

### Test Combination Function ###
# Pass a combination string, the list of items, and the knapsack limit.
# This function tests the combination passed by the combination string.
# Returns the weight, value
def testCombo(combo, items, limit):
    weight = 0
    value = 0
    for i in range(len(combo)):
        if combo[i] == "1":
            weight += int(items[(i*3)+1])
            value += int(items[(i*3)+2])   
    return weight, value

### Increment Combination Function ###
# Pass a binary combination string.
# This function increments the combination function by one. If it becomes full, it overflows to all 0s.
# Returns the same combination string, now incremented by one.
def incrementCombo(combo):
    i = 0
    while i < len(combo):
        if combo[i] == "0":
            combo[i] = "1"
            break
        combo[i] = "0"
        i += 1
    return combo

### Main Function ###
def main():
    limit = input("Please enter the weight limit of the knapsack. ")
    limit = int(limit)
    itemArray, numItems = makeArray()
    combosTotal = 2**numItems
    
    # Initialize Combination String #
    # comboString is really an array of strings that we'll convert to a single string whenever we need to #
    # the name "string" is misleading but I wanted to be consistent with the assignment document # 
    comboString = []
    comboWeight = 0
    comboValue = 0
    for i in range(numItems):
        comboString.append("0")

    # Initialize Optimal Variables #
    optimalCombo = []
    for i in range(numItems):
        optimalCombo.append("0")
    optimalWeight = 0
    optimalValue = 0

    # Open Output File #
    outputFile = open("output.txt", "w")

    # Enter For Loop #
    for i in range(combosTotal):
        # Test Combo #
        comboWeight, comboValue = testCombo(comboString, itemArray, limit)
        
        # Write to Output File #
        outputFile.write("".join(comboString) + "\n")
        outputFile.write(str(comboWeight) + "\n")
        outputFile.write(str(comboValue) + "\n")
        
        # Compare With Optimal Solution #
        if comboWeight <= limit and comboValue >= optimalValue:
            # Reassign Optimal Solution if necessary #
            for i in range(numItems):
                optimalCombo[i] = comboString[i]
            optimalWeight = comboWeight
            optimalValue = comboValue

        # Increment Combo #
        comboString = incrementCombo(comboString)

    # Write Optimal Solution to Output File #
    outputFile.write("".join(optimalCombo) + "\n")
    outputFile.write(str(optimalWeight) + "\n")
    outputFile.write(str(optimalValue) + "\n")

    # Close Output File #
    outputFile.close()

### Main Function Call ###
main()
