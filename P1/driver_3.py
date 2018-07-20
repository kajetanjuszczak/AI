import queue as Q
import time
import sys
import math
import heapq
#### SKELETON CODE ####
# The Class that Represents the Puzzle`


class PuzzleState(object):

    """docstring for PuzzleState"""

    def __init__(self, config, n=3, parent=None, action="", cost=0):

        if n * n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")

        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []
        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    
    def append_action(self, action):
        
        self.action = "{}{}".format(action, self.action)

        
    def get_action(self):
        
        return self.action
        
    def get_config(self):

        return self.config
    
    def get_cost(self):

        return self.cost

    def get_parent(self):

        return self.parent

    def get_path(self):
        action_list = []
        parent = self
        for i in range(self.get_cost() - 1):
            action_list.append(parent.get_action())
            parent = parent.get_parent()
        return action_list[::-1]

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):

                line.append(self.config[offset + j])

            print(line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left ", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right ", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up ", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down ", cost=self.cost + 1)

    def expand(self):
        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:

                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:

                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:

                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:

                self.children.append(right_child)

        return self.children

# Function that Writes to output.txt

# Students need to change the method to have the corresponding parameter

def writeOutput(path_to_goal, cost_of_path, nodes_expanded, search_depth, time):
    output = "C:/stuff/python/AI/P1/output.txt"
    with open(output, "w") as w:
        w.write("path_to_goal: {}\n".format(path_to_goal))
        w.write("cost_of_path: {}\n".format(cost_of_path))
        w.write("nodes_expanded: {}\n".format(nodes_expanded))
        w.write("search_depth: {}\n".format(cost_of_path))
        w.write("max_search_depth: {}\n".format(search_depth))
        w.write("running_time: {}".format(time))
    # Student Code Goes here


def bfs_search(initial_state):
    """BFS search"""
    time1 = time.time()
    frontier = Q.Queue()
    explored = set()
    frontier_set = set()
    frontier.put(initial_state)
    frontier_set.add(initial_state.get_config())
    current_highest = 0
    while not frontier.empty():
        state = frontier.get()
        if test_goal(state):
            action_list = [state.get_action()]
            parent = state.get_parent()
            for i in range(state.get_cost() - 1):
                action_list.append(parent.get_action())
                parent = parent.get_parent()
            time2 = time.time()
            return writeOutput(action_list[::-1], state.get_cost(), len(explored), current_highest, time2-time1)
        frontier_set.remove(state.get_config())
        explored.add(state.get_config())
        neighbors = state.expand()
        for neighbor in neighbors:
            if neighbor.get_config() not in explored and neighbor.get_config() not in frontier_set:
                frontier.put(neighbor)
                frontier_set.add(neighbor.get_config())
                if neighbor.get_cost() > current_highest:
                    current_highest = neighbor.get_cost()



def dfs_search(initial_state):
    """DFS search"""
    time1 = time.time()
    frontier = [initial_state]
    frontier_set = set()
    frontier_set.add(initial_state.get_config())
    explored = set()
    current_highest = 0
    while len(frontier) > 0:
    # for i in range(10):
        state = frontier.pop()
        frontier_set.remove(state.get_config())
        if test_goal(state):
            action_list = [state.get_action()]
            parent = state.get_parent()
            for i in range(state.get_cost() - 1):
                action_list.append(parent.get_action())
                parent = parent.get_parent()
            time2 = time.time()
            return action_list[::-1] ,state.cost, len(explored), current_highest, time2-time1
        explored.add(state.get_config())
        neighbors = state.expand()[::-1]
        for neighbor in neighbors:
            if neighbor.get_config() not in explored and neighbor.get_config() not in frontier_set:
                frontier.append(neighbor)
                frontier_set.add(neighbor.get_config())
                if neighbor.get_cost() > current_highest:
                    current_highest = neighbor.get_cost()


def A_star_search(initial_state):
    """A * search"""

    frontier_heap = []
    heapq.heappush(frontier_heap, (0, initial_state))
    frontier_set = set()
    frontier_set.add(initial_state.get_config())
    explored = set()
    current_highest = 0
    while len(frontier_heap) > 0:
        # change hype so that 2 same numbers can be compared
        state = heapq.heappop(frontier_heap)
        frontier_set.remove(state[1].get_config())
        if test_goal(state[1]):
            return "win"
        explored.add(state[1].get_config())
        neighbors = state[1].expand()
        for neighbor in neighbors:
            if neighbor.get_config() not in explored and neighbor.get_config() not in frontier_set:
                distance = calculate_total_cost(neighbor)
                heapq.heappush(frontier_heap, (distance, neighbor))
                frontier_set.add(neighbor.get_config())



def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    return calculate_manhattan_dist(state) + state.get_cost()
    ### STUDENT CODE GOES HERE ###


def calculate_manhattan_dist(state):
    """calculatet the manhattan distance of a tile"""
    config = state.get_config()
    total_dist = 0
    for i in range(1, 9):
        total_dist += (abs(i // 3 - config.index(i) // 3) + abs(i % 3 - config.index(i) % 3))
    return total_dist
    ### STUDENT CODE GOES HERE ###

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    goal_config = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    if puzzle_state.get_config() == goal_config:
        return True
    return False
    ### STUDENT CODE GOES HERE ###

def priority(state): 
    pass

# Main Function that reads in Input and Runs corresponding Algorithm


def main():

    sm = sys.argv[1].lower()

    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":

        bfs_search(hard_state)

    elif sm == "dfs":

        dfs_search(hard_state)

    elif sm == "ast":

        A_star_search(hard_state)

    else:

        print("Enter valid command arguments !")


if __name__ == '__main__':
    #print(dfs_search(PuzzleState((6,1,8,4,0,2,7,3,5))))
# =============================================================================
#     print(bfs_search(PuzzleState((1,2,5,3,4,0,6,7,8))))
# =============================================================================
    print(A_star_search(PuzzleState((6,1,8,4,0,2,7,3,5))))
    #print(calculate_manhattan_dist(PuzzleState((6,1,8,4,0,2,7,3,5))))
    # main()

