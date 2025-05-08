from collections import deque #deque basically has all the queue operations in the collections library

#a dictionary below is created via the map of Romania I used from the Lecture slides as a list
romania = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

#Created a definition or function to perform a Breadth-First Search to find the shortest path in terms of the number nodes
def bfsshortpath(graph, start, finish) :
    explored =[] #A list to track down the nodes that have been explored
    queue = deque([[start]]) #Queue to hold the paths that needs to be explored, and it initialised with city it has started from

    #If the start city is the same as the end city, the program returns to the start itself as the path.
    if start == finish :
        return [start]
    
    while queue :
        #Gets the first path from the queue when starting
        path = queue.popleft()
        #Gets the last node in the current path
        node = path[-1]

        #If the node is not explored yet
        if node not in explored :
            #Get all the cities neighbouring of the current node
            neighbours = graph[node]

            #Another loop trhough all neighbours of the current node
            for neighbour in neighbours :
                #Creates a new path including the neighbour
                newpath = list(path) #Copies the current path
                newpath.append(neighbour) #Add the neighbouring city to the new path
                queue.append(newpath) #Adds the new path to the queue

                #If the neighbour is the final city, it returns to the path
                if neighbour == finish :
                    return newpath
            
            #Marks the current node as explored
            explored.append(node)
    
    #If no path is found, a message is returned indicating that no path exists
    return "No path exists in between these cities."


# Get the start and end city from the user and the input is case-insesitive
startcity = input("Enter the city you want to start from: ").capitalize()
endcity = input("Enter the city you want to stop at: ").capitalize()

# Check if the input cities exist in the graph
if startcity not in romania or endcity not in romania :
    print("Error, these cities don't exist.")
else :
    # If the cities exist, call the BFS function to find the shortest path
    path = bfsshortpath(romania, startcity, endcity)
    if path:
        #Prints the shortest path from the start city to the end city and the number of cities it has traversed
        print(f"Shortest path from {startcity} to {endcity} is: {' -> '.join(path)}")
        print(f"Number of cities traversed: {len(path) - 1}")
    else:
        #If there is no path, a message is printed noting that there is no path between those two cites
        print(f"No path exists between {startcity} and {endcity}.")