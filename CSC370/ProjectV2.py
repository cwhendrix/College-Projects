from copy import deepcopy
import networkx as nx
import time
import sys


class Node:
    def __init__(self):
        self.level = 0
        self.path =[]
        self.bound = 0
    
    def setLevel(self,level):
        self.level = level 
    
    def getLevel(self):
        return self.level 
    
    def addToPath(self,path):
        self.path = path
    
    def appendToPath(self,item):
        self.path.append(item)
    
    def getPath(self):
        return self.path
    
    def setBound(self,bound):
        self.bound = bound
    
    def getBound(self):
        return self.bound



def genAllPermutations(nodes):
	if len(nodes) == 0:
		return []
	if len(nodes) == 1:
		return [nodes]

	newPerm = []

	for i in range(0,len(nodes)):
		val = nodes[i]
		result = nodes[:i] + nodes[i+1:]
		for item in genAllPermutations(result):
			newPerm.append([val] + item)
	return newPerm


def searchForHamiltonianBF(allPermutations, adjMatrix,totalNodes):
    for permutation in allPermutations:
        #Start with 1 node being visited since we'll always have the starting node
        nodesVisited = 1
        visitedNodeNames = []
        for i in range(0,len(permutation)-1):
            #Get the available paths for the current node we're at
            #and record the node we've visited
            visitedNodeNames.append(permutation[i])
            currentEdges = adjMatrix[permutation[i]]
            #Check to make sure we haven't already been to the node called for next by the permutation
            #A path can't have duplicate nodes
            if(permutation[i+1] in visitedNodeNames):
                break
            #If there is an edge from the node we're at to the next node called for 
            #by the permutation, update the nodes we've visited 
            #We'll "travel" to that next node on the next iteration of the loop
            if(currentEdges[permutation[i+1]] == 1):
                nodesVisited = nodesVisited + 1
            else:
                #If there's not a path to the node called for next, then this 
                #path will never work, stop now
                break
        #If we've found a path that visits every node, stop and return this path
        if(nodesVisited == totalNodes):
            return permutation
    return False

def findPath(root, adjMatrix, totalNodes,nodeNames):
    if(len(root.getPath()) == totalNodes):
        return True, root
    for name in nodeNames: 
        if name not in root.getPath():
            if (adjMatrix[root.getPath()[len(root.getPath())-1]][name] == 1):
                childNode = Node()
                childNode.addToPath(deepcopy(root.getPath()))
                childNode.appendToPath(name)
                res,node = findPath(childNode,adjMatrix,totalNodes,nodeNames)
                if(res):
                    return res, node    
    return False, None
    
    

def pathHelper(nodeNames,adjMatrix,totalNodes):
    for name in nodeNames:
        root = Node()
        root.appendToPath(name)
        res,node = findPath(root,adjMatrix,totalNodes,nodeNames)
        if(res):
            print("Path found!")
            print("Path is: ")
            print(node.getPath())
            return True
    print("No path found!")
    return False


def generateGraphs(numNodes,numGraphs):
    allGraphs = []
    for i in range(0,numGraphs):
        #If observing a lot of graphs coming back with no paths found, 
        #increase the number in the last argument of the below line
        #If the opposite is true, decrease it
        G = nx.random_geometric_graph(numNodes, 0.5)
        D = G.to_directed()
        adj = nx.to_numpy_array(D)
        allGraphs.append(adj)
    return allGraphs

    


#Generate 50 adjacency matrices with number of nodes n
n= int(sys.argv[1])
print("Getting average times over 50 random graphs with "+str(n)+" nodes")
newGraphs = generateGraphs(n,50)
#Open CSV file for output
outputFile = open(sys.argv[2], "a")
outputString = sys.argv[1]
#Brute force method
nodes = []
for i in range(0,n):
    nodes.append(i)
allPerms = genAllPermutations(nodes)
totalTime = 0
for graph in newGraphs:
    startTime = time.time()
    result = searchForHamiltonianBF(allPerms,graph,n)
    totalTime = totalTime + (time.time()-startTime)
print("BF average time")
avgTime = totalTime/100
print(avgTime)
outputString = outputString + "," + str(avgTime)
#Backtracking method
totalTime = 0
for graph in newGraphs:
    startTime = time.time()
    result = pathHelper(nodes,graph,n)
    totalTime = totalTime + (time.time()-startTime)
print("Backtracking average time")
avgTime = totalTime/100
print(avgTime)
outputString = outputString + "," + str(avgTime) + "\n"
outputFile.write(outputString)
outputFile.close()

