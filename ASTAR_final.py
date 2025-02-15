import random
import numpy as np
import math

class Nodes:
    """
    Description:
    These are the objects that populate the grid or 'maze' on the board.  
    The constructor takes two parameters: the x and y positions where
    the node will reside.

    """
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.g = float('inf')
        self.h = float('inf')
        self.f = self.g + self.h
        self.start_point = False
        self.end_point = False
        self.adjacent = []
        self.adjacent_evaluated_arr = []
        self.previous_node = []
        self.blocked = False
        self.fully_checked = False

    def read_name(self):
        print(self.xpos, self.ypos)

    def read_adjacent(self):
        for i in range(len(self.adjacent)):
            self.adjacent[i].read_name()

    def read_ghf(self):
        print(self.g, self.h, self.f)

    def dist(self, next_node):
        return math.sqrt((self.xpos - next_node.xpos) ** 2 + (self.ypos - next_node.ypos) ** 2)


class Board:
    """
    Description:
    The board is a matrix of 'Node' objects previously defined.  
    This matrix will be navigated by the algorithm.
    """
    active = []
    def __init__(self, size, Ax, Ay, Zx, Zy):
        self.A = (Ax, Ay)
        self.Z = (Zx, Zy)
        self.size = size
        self.all_arr = []
        self.add()

    def add(self):
        # creating a board of nodes
        for i in range(self.size):
            for j in range(self.size):
                temp = Nodes(i, j)
                if i == self.A[0] and j == self.A[1]:
                    temp.start_point = True
                    temp.g = 0
                    self.active.append(temp)
                if i == self.Z[0] and j == self.Z[1]:
                    temp.end_point = True
                temp.h = math.sqrt((temp.xpos - self.Z[0]) ** 2 + (temp.ypos - self.Z[1]) ** 2)
                temp.f = temp.g + temp.h
                self.all_arr.append(temp)

        # adding adjacent nodes to each node
        for i in range(self.size):
            for j in range(self.size):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i + k >= 0 and i + k <= self.size - 1 and j + l >= 0 and j + l <= self.size - 1 and (k, l) != (0, 0):
                            self.all_arr[self.size*i + j].adjacent.append(self.all_arr[self.size*(i + k) + (j + l)])
                            self.all_arr[self.size * i + j].adjacent_evaluated_arr.append(False)

    # function to quickly call nodes
    def selector(self, x, y):
        return self.all_arr[self.size*x + y]

# --- MAIN FUNCTION ---
def Astar() -> None:
    """
    Description:
    Main executable function to run the algorithm.
    1. Take input from the user for the size of the maze (n x n).
    2. Generate a random maze to navigate through, with a start and end point.
    3. Initialize the board with the relevant objects.
    4. Follow the A* algorithm to find the shortest path 
    from the start to the end point. Display the maze and path to the user.

    """
    # Taking a valid input
    correct_input = False
    while correct_input == False:
        size = input("Please enter the size of maze you would like (3 to 18): ")
        try:
            int(size)
            if int(size) > 2 and int(size) < 19:
                correct_input = True
            else:
                print('Input out of range, please enter an integer between 3 and 18')
            size = int(size)
        except ValueError:
            print('Wrong input, please enter an integer between 3 and 19')

    # start and end points
    A = (random.randint(0, size - 1), 0)
    Z = (random.randint(0, size - 1), size - 1)

    # initialising the board of Nodes
    board = Board(size, A[0], A[1], Z[0], Z[1])

    # Creating the string array (the maze that we see)
    qmat1 = []
    for j in range(size):
        quickmat = ['-' for j in range(size)]
        qmat1 = qmat1 + [quickmat]
    maze = np.array(qmat1)

    # Creating the maze + setting the blocked nodes to blocked
    for j in range(int((size-1)/2)):
        for i in range(size):
            maze[i][2*j +1] = 'X'
            board.selector(i, 2*j +1).blocked = True
        rand_pos1 = random.randint(0, size - 1)
        board.selector(rand_pos1, 2*j+1).blocked = False
        maze[rand_pos1][2 * j + 1] = '-'
        rand_pos2 = random.randint(0, size - 1)
        board.selector(rand_pos2, 2*j+1).blocked = False
        maze[rand_pos2][2 * j + 1] = '-'
    maze[A[0]][A[1]] = 'S'
    maze[Z[0]][Z[1]] = 'E'

    print(f'Here is a randomly generated {size}x{size} maze:')
    print(maze)
    print("The path cannot travel though a point marked 'X'...")
    print(f"The start point 'S' is {A[0], A[1]}  and the end point 'E' is {Z[0], Z[1]}\n")

    # the running loop
    running = True
    while running:

        # finding, out of the active nodes, which one has the smallest f value (closest to the end)
        active_len_arr = []
        for i in range(len(board.active)):
            if board.active[i].blocked == False:
                if board.active[i].fully_checked == False:
                    active_len_arr.append(board.active[i].f)
        min_ind = active_len_arr.index(min(active_len_arr))
        # the closest active node called 'close'
        close = board.active[min_ind]

        # finding which of the adjacent nodes to 'close' are available
        available_adjacent = []
        for j in range(len(close.adjacent)):
            if close.adjacent[j].blocked == False:
                if close.adjacent[j].fully_checked == False:
                    if close.adjacent_evaluated_arr[j] == False:
                        available_adjacent.append(j)

        if len(available_adjacent) == 0:
            close.fully_checked = True
            board.active.remove(close)
        elif len(available_adjacent) >= 1:

            # finding the lowest h out of adjacent options
            temp_h_arr = []
            for u in range(len(available_adjacent)):
                temp_h_arr.append(close.adjacent[u].h)
            ind_min_2 = temp_h_arr.index(min(temp_h_arr))
            k = available_adjacent[ind_min_2]

            # updating g and f if closer than previously found
            if close.adjacent[k].g > close.g + close.dist(close.adjacent[k]):
                close.adjacent[k].g = close.g + close.dist(close.adjacent[k])
                close.adjacent[k].f = close.adjacent[k].g + close.adjacent[k].h
                close.adjacent[k].previous_node = close

            # adding to active if not before
            if close.adjacent[k] not in board.active:
                board.active.append(close.adjacent[k])

            close.adjacent_evaluated_arr[k] = True

        # updating status of node
        number_of_available_now = 0
        for j in range(len(close.adjacent)):
            if close.adjacent[j].blocked == False:
                if close.adjacent_evaluated_arr[j] == False:
                    number_of_available_now += 1
        if number_of_available_now == 0:
            close.fully_checked = True
            board.active.remove(close)

        # working out if shortest path has been found , ending the loop if so
        if board.selector(Z[0],Z[1]) in board.active:
            less_than_sum = 0
            for d in range(len(board.active)):
                if board.selector(Z[0],Z[1]).f <= board.active[d].f:
                    less_than_sum += 1

            # tracing back from the end to the start and displaying on the maze
            if less_than_sum == len(board.active):
                tracing = True
                current_node = board.selector(Z[0],Z[1])
                while tracing:
                    if current_node == board.selector(A[0],A[1]):
                        tracing = False
                    maze[current_node.xpos][current_node.ypos] = 'o'
                    current_node = current_node.previous_node
                return \
                print("After applying th ASTAR path finding algorithm... \nThe shortest path "
                      f"is {board.selector(Z[0],Z[1]).f} units long denoted by the string of o's \n", maze)
    # Pause
    input("Click enter to exit")


# Main executable
if __name__ == '__main__':
    Astar()