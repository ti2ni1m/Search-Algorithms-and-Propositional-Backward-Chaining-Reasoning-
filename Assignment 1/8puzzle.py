import heapq #Import heapq for priority queue operations (used in A* algorithm).

#Goal configuration for the eight-puzzle hassle
goals = [[1, 2, 3],
         [8, 0, 4],
         [7, 6, 5]]

#Function to calculate the Manhattan distance heuristic
def manhattan(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                xgoal, ygoal = divmod(goal.index(tile), 3)  # Find goal position of tile
                distance += abs(i - xgoal) + abs(j - ygoal)  # Add Manhattan distance
    return distance

#Function to create neighbouring situations by moving an empty tile
def neighbours(state):
    neighbour = []
    #Find the position of the empty tile (0)
    xempty, yempty = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right moves

    #Try all possible moves
    for dx, dy in moves:
        newx, newy = xempty + dx, yempty + dy
        #Check if the new position is within the board
        if 0 <= newx < 3 and 0 <= newy < 3:
            newstate = [row[:] for row in state]  # Copy current state
            #Swap the empty tile with the tile at the new position
            newstate[xempty][yempty], newstate[newx][newy] = newstate[newx][newy], newstate[xempty][yempty]  # Swap tiles
            neighbour.append(newstate)
    return neighbour

#A* search algorithm to solve the puzzle
def astar(start, end):
    goalflat = [num for row in end for num in row]  # Flatten goal only once
    openlist = [] #Priority queue for the open list (states to be explored)
    heapq.heappush(openlist, (0, start, [], 0))  # f=0 initially
    visited = set() #Set to store visited states

    #Main loop for the A* algorithm
    while openlist:
        f, current, path, g = heapq.heappop(openlist)  # Pop the state with the lowest f

        #If the current state is the goal, return the solution path and number of moves
        if current == end:
            return path + [current], g  # Return path and number of moves

        visited.add(tuple(map(tuple, current)))  # Add the current state to visited

        for neighbour in neighbours(current):
            if tuple(map(tuple, neighbour)) not in visited: #Only explore unvisited neighbours
                h = manhattan(neighbour, goalflat)  # Compute heuristic
                f = g + 1 + h  # f = g + h
                heapq.heappush(openlist, (f, neighbour, path + [current], g + 1))  # Push the new state

    return None, -1  # Return None if no solution found

#Function to print the 3x3 puzzle board
def printboard(board):
    for row in board:
        #Replace 0 with '_' for better visualization
        print(' '.join(str(x) if x != 0 else '_' for x in row))
    print()

# Test cases from 1 to 13
tests = [
    [[2, 8, 3], [1, 6, 4], [7, 0, 5]],  # Configuration 1
    [[2, 1, 6], [4, 0, 8], [7, 5, 3]],  # Configuration 2
    [[5, 7, 2], [0, 8, 6], [4, 1, 3]],  # Configuration 3
    [[0, 6, 5], [4, 1, 7], [3, 2, 8]],  # Configuration 4
    [[0, 6, 5], [4, 1, 8], [3, 7, 2]],  # Configuration 5
    [[6, 5, 7], [4, 1, 0], [3, 2, 8]],  # Configuration 6
    [[6, 5, 7], [4, 0, 1], [3, 2, 8]],  # Configuration 7
    [[6, 5, 7], [4, 2, 1], [3, 0, 8]],  # Configuration 8
    [[5, 6, 7], [0, 4, 8], [3, 2, 1]],  # Configuration 9
    [[6, 5, 7], [4, 2, 1], [3, 8, 0]],  # Configuration 10
    [[0, 5, 7], [6, 4, 1], [3, 2, 8]],  # Configuration 11
    [[5, 6, 7], [4, 0, 8], [3, 2, 1]],  # Configuration 12
    [[2, 0, 4], [1, 3, 5], [7, 8, 6]]   # Configuration 13
]

# User selects a test case
print("Choose an initial configuration by entering a number (1-13):")
for i, test in enumerate(tests, start=1):
    print(f"Initial configuration {i}:")
    printboard(test) #Print each initial configuration

#Get user input for the selected test case
choice = int(input()) - 1
if 0 <= choice < len(tests):
    start = tests[choice]
    print(f"\nInitial configuration {choice+1}:")
    printboard(start) #Print the chosen configuration
    solution, moves = astar(start, goals) #Run A* to solve the puzzle
    if solution:
        print(f"\nSolution found in {moves} moves:")
        for state in solution:
            printboard(state) #Print each step of the solution
    else:
        print("No solution was found.")
else:
    print("Invalid choice.") #An error message if any invalid selection
