# ASTAR-path-finding
# 
# To use the function:
# 1. Enter an input into the function (between 3 and 18)
# 2. The fuction will then create a n by n  sized maze and generate a random start and end point on opposite sides
# 3. The ASTAR search algorithm will run until the end node is reached and it also has the lowest f value of the active nodes
# 4. The initial and final maze will be printed , with the shortest path printed on the final maze
#
# About the algorithm:
# To start with there is only one active node, the start node, the algorithm then finds the available adjacent nodes around it selects the one which is the closest to  the end node. This node is then added to the active nodes. This is then repeated with the active nodes availabe, choosing the active node which has the smallest f value (explained later). If an active node has explored all of its adjacent nodes then is is no longer active. This is repeated until the path to the end is completed. All nodes have a h value which is my progrem is the distance (pythagoras) directly between the node and the end node. If is or has been active it will have a g value (less than inf) which is the shortest way of getting there from the start that has been found so far. Then finally a all nodes have an f value which is the sum of g and h. This f value is what is used to determine which active node we evaluate next, always choosing the shortest. In my code a path can move diaginally as well as up/down/left/right (as long as not blocked by an 'X').
#
#
#
#
#
#
#
#
  
