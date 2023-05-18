### Programming Homework 3: TSP by Branch-And-Bound ###
### Cooper Hendrix ###
### CSC 370 - Dr. Bailey ###
import csv
import sys

### node class ###
class node:
    next = None
    priority = 0
    path = []
    def __init__(self, next, priority, path):
        self.next = next
        self.priority = priority
        self.path = path.copy()
    
### priority queue class ###
class PQ:
    len = 0
    head = None

    def isEmpty(self):
        return self.head == None and self.len == 0

    def push(self, path, total):
        newNode = node(None, total, path.copy())
        if self.isEmpty():
            self.head = newNode
        elif self.head != None and newNode.priority < self.head.priority:
                newNode.next = self.head
                self.head = newNode
        else:
            curr = self.head
            par = None
            while curr != None and newNode.priority >= curr.priority:
                par = curr
                curr = curr.next
            if par != None:
                par.next = newNode
            newNode.next = curr
        self.len += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from empty priority queue.")
        popNode = self.head
        self.head = self.head.next
        self.len -= 1
        return popNode.path, popNode.priority

### function which changes csv to a 2D array. made separate just to make code easier ###
def csvtoarray():
    array = list(csv.reader(open("city_distances.csv")))
    return array

### function which ensures that a city isn't already in the path ###
def notinpath(path, city):
    for i in range(len(path)):
        if path[i] == city:
            return True
    return False

# Determines if a partial solution is promising or not. 
# A partial solution (and all of its child solutions) are not promising if:
#   - the edge to get between two cities is 0 (invalid path)
#   - the current total + next edge > the current optimal solution (no way to be optimal)
#   - the path about to be added is already in the circuit (cannot use edges that have already been used)
def promising(array, nextcity, currcity, path, total, ototal):
    return int(array[currcity][nextcity]) != 0 and not (total + int(array[currcity][nextcity]) > ototal) and not notinpath(path, nextcity)

def tsp_bnb():
    cities = csvtoarray()
    numCities = len(cities[0]) - 1

    currpath = [1]  # array which keeps track of our current path; assuming start at first city as start doesn't matter in circuits
    currKM = 0    # current KM traveled
    bestpath = [] # array which keeps track of the best path; assuming start at first city
    bestKM = sys.maxsize # KM traveled in best case; begins as max int so it can decrease as algorithm runs
    tspPQ = PQ()    # priority queue for our algorithm :)
    tspPQ.push(currpath, currKM)

    # Begin algo
    while not tspPQ.isEmpty():
        # Pop top node
        currpath, currKM = tspPQ.pop()
        # Evaluate current path, if one edge from completion
        if len(currpath) == numCities:
            currpath.append(1)
            currKM += int(cities[currpath[len(currpath) - 2]][1])   # add edge from final city back to start
            if currKM < bestKM:
                bestKM = currKM
                bestpath = currpath.copy()
        # path isn't complete
        else:
            for i in range(2, numCities + 1):
                # push promising children
                if promising(cities, i, currpath[len(currpath) - 1], currpath, currKM, bestKM):
                    temppath = currpath.copy()
                    temppath.append(i)
                    temptotal = currKM + int(cities[i][currpath[len(currpath) - 1]])
                    tspPQ.push(temppath, temptotal)
    return bestKM, bestpath

def main():
    distance, circuit = tsp_bnb()
    print("Optimal Distance:", distance)
    print("Optimal Circuit:", circuit)
    
main()
