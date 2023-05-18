### Programming Homework 4: TSP by Genetic Algorithm ###
### Cooper Hendrix ###
### CSC 370 - Dr. Bailey ###
import matplotlib.pyplot as plt
import numpy as np
import math

### Returns Euclidean Distance between two points ###
def euclid_dist(a, b):
    dist = math.sqrt(((b[0]-a[0])**2) + ((b[1]-a[1])**2))
    return dist

### Sorts all paths by their totals ###
def sortpaths(cities, paths):
    total = 0
    sortedpaths = []
    sortedtotals = []
    for path in paths:
        total = 0
        for i in range(len(path)):
            if i < len(path) - 1:
                total += euclid_dist(cities[path[i]], cities[path[i+1]])
            else:
                total += euclid_dist(cities[path[i]], cities[path[0]])
        sortedpaths.append(path)
        sortedtotals.append(total)
    
    ### Sort Paths! ###
    n = len(sortedpaths)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if sortedtotals[j] > sortedtotals[j + 1]:
                swapped = True
                sortedtotals[j], sortedtotals[j + 1] = sortedtotals[j + 1], sortedtotals[j]
                sortedpaths[j], sortedpaths[j + 1] = sortedpaths[j + 1], sortedpaths[j]
            
    # print("Sorted Paths:", sortedpaths)
    # print("Sorted Totals:", sortedtotals)
    return sortedpaths, sortedtotals[0]

#### Create the pool of parents ###
def make_pool(paths):
    pool = paths[:len(paths) // 2]
    ### remove bottom 50% ###
    paths = paths[:len(paths) // 2]
    for path in paths:   # 4 of each eligible path
        pool.append(path)
        pool.append(path)
        pool.append(path)
    return pool


### Adds in mutations by probability ###
def mutation(path1, mut):
    rand = np.random.randint(0, 100)
    if rand <= mut: # mutation occurs :0
        i = np.random.randint(0, len(path1))
        j = np.random.randint(0, len(path1))
        trans = path1[i]
        path1[i] = path1[j]
        path1[j] = trans
    return path1

### Performs Nearest Neighbor Crossover (NNX) with two paths. ###
def NNX(path1, path2, paths, mut, cities, pool):
    newpath = []
    currcity = -1
    cityp1 = -1
    cityp2 = -1
    for j in range(len(cities)):
        # print("start:", j)
        newpath.append(j)
        for i in range(len(cities)):
            nextcity = -1       # next city to be visited
            short = 2**31 - 1   # shortest path from currcity to the next city, set to a really big number
            currcity = newpath[i]
            # find location of currcity in other paths
            cityp1 = path1.index(currcity)
            cityp2 = path2.index(currcity)
            # find shortest path from currcity to next untouched city
            if cityp1 + 1 >= len(path1) and path1[0] not in newpath:    # last city in path before repeating first node
                short = euclid_dist(cities[currcity], cities[path1[0]]) # loop back to first node in path
                nextcity = path1[0]
            elif cityp1 + 1 < len(path1):  
                if euclid_dist(cities[currcity], cities[path1[cityp1 + 1]]) < short and path1[cityp1 + 1] not in newpath:    # edge from path 1 is short
                    short = euclid_dist(cities[currcity], cities[path1[cityp1 + 1]])
                    nextcity = path1[cityp1 + 1]
            if cityp2 + 1 >= len(path2) and path2[0] not in newpath:    # last city in path before repeating first node
                if euclid_dist(cities[currcity], cities[path2[0]]) < short:
                    short = euclid_dist(cities[currcity], cities[path2[0]])
                    nextcity = path2[0]
            elif cityp2 + 1 < len(path2):
                if euclid_dist(cities[currcity], cities[path2[cityp2 + 1]]) < short and path2[cityp2 + 1] not in newpath:    # edge from path 2 is short
                    short = euclid_dist(cities[currcity], cities[path2[cityp2 + 1]])
                    nextcity = path2[cityp2 + 1]
            if nextcity == -1 and len(newpath) == len(cities):  # reached a completed path!
                break
            if nextcity != -1:  # if it is, there isn't a good path from here and it's invalid
                newpath.append(nextcity)
                # print(newpath)
            else:
                # print("badpath!!!!!!")
                newpath.clear()
                break
        if len(newpath) == len(cities): # found valid path!
            break
    
    # Mutate paths
    if newpath != []:
        newpath = mutation(newpath, mut)

    # Add new paths to population, if a valid path was created
    if newpath != []:
        paths.append(newpath)
    else:
        if pool.index(path1) < pool.index(path2):
            paths.append(path1)
        else:
            paths.append(path2)

### Crossover paths until the pool is empty. :) ###
def crossover_time(paths, pool, mut, cities):
    while pool != []:
        i = np.random.randint(0, len(pool))
        j = np.random.randint(0, len(pool))
        while i == j:
            j = np.random.randint(0, len(pool))
        path1 = pool[i]
        path2 = pool[j]
        NNX(path1, path2, paths, mut, cities, pool)
        pool.remove(path1)
        pool.remove(path2)

### Main FCN ###
def main():
    ### Take in input from user, assuming friendly input ###
    print("Please enter the number of cities: ")
    num_cities = int(input())
    print("Please enter the number of iterations: ")
    num_iterations = int(input())
    print("Please enter the probability of mutations, between 0 and 100: ")
    prob_mut = int(input())
    while prob_mut > 100 or prob_mut < 0:
        print("Please enter the probability of mutations, **between 0 and 100**: ")
        prob_mut = int(input())
        if prob_mut <= 100 and prob_mut >= 0:
            print("Thanks :)")
    
    # Create a NumPy random generator object
    rng = np.random.default_rng() 

    # create variable to hold experimental data
    x_data = [] # generation number
    y_data = [] # tour distance
    toppath = 0 # shortest path of the current generation

    # Create an array of random cities
    cities = rng.normal(0, 1, (num_cities, 2))
    cities_index = []
    for i in range(num_cities):
        cities_index.append(i)
    
    ### Initialize random paths ###
    paths = []
    for i in range(100):
        curr = cities_index.copy()
        np.random.shuffle(curr)
        paths.append(curr)
    
    ### Run Algorithm ###
    for i in range(num_iterations):
        paths, toppath = sortpaths(cities, paths)
        x_data.append(i)
        y_data.append(toppath)
        pool = make_pool(paths)
        paths = []
        crossover_time(paths, pool, prob_mut, cities)

    #labels = ['']
    plt.plot(x_data, y_data, linestyle='-', marker='o')
    #plt.legend(labels)
    plt.xlabel('Generation number ($N$)')
    plt.ylabel('Total Tour Distance')
    plt.title('Solution Quality over Time')
    plt.ylim(0, num_cities * 2)
    fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!   
    # If you wish to save the figure
    fig.savefig('descriptive_file_name.png')    # I like this name so I kept it :)
    
    paths, toppath = sortpaths(cities, paths)
    print("BEST PATH:", paths[0])
    print("BEST DISTANCE:", toppath)


main()
