"""
Surya Teja Cheedella
SnShine Industries
snshine.in


Rules:

Procedure:
1. Build a graph from the board with knight like moves.
2. Simple backtracking after that!
"""

"""
Board legend:
    type id: scores associated with the block (name)
    0: 0        Landing base
    1: None     Lunar mountain
    2: None     Lunar crevice
    3: -2       Lunar crater
    4: -1       Lunar rocks
    5: 0        Lunar terrain
    6: 1        Flat terrain
    7: 2        Rock-free terrain
    8: 4        Minerals
"""

import json
import sys
from collections import OrderedDict

BOARD = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 2, 6, 7, 4, 8, 6, 8, 7, 3, 1],
         [1, 3, 8, 6, 5, 3, 4, 5, 6, 7, 1],
         [1, 6, 7, 4, 6, 2, 8, 7, 4, 6, 1],
         [1, 5, 7, 5, 3, 7, 6, 2, 7, 4, 1],
         [1, 3, 6, 8, 6, 0, 4, 8, 6, 3, 1],
         [1, 4, 2, 6, 4, 5, 6, 7, 3, 5, 1],
         [1, 7, 8, 3, 6, 5, 7, 4, 2, 7, 1],
         [1, 6, 5, 7, 8, 4, 3, 6, 5, 6, 1],
         [1, 5, 3, 4, 6, 2, 6, 7, 4, 8, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

BOARD_SCORES = [0, None, None, -2, -1, 0, 1, 2, 4]



"""
Graph:
    Bi-directional graph, because scores gained from node1->node2 is different from scores
    gained from node2->node1.

Node:
    id: universal id
    score: score linked to this node

Edge:
    weight: scores gained from going to one node to other


"""

class Graph:
    def __init__(self):
        self.dict = {}
        self.score = -200

    def connect(self, A, B, weight, path_str):
        self.dict.setdefault(A, {})[B] = [weight, path_str]

    def remove_node(self, A):
        self.dict.pop(A, None)
        [self.dict[i].pop(A, None) for i in self.dict]

    def remove_connection(self, A, B):
        """ removes only one direction connection from A to B """
        self.dict[A].pop(B, None)

    def get(self, A, B=None):
        links = self.dict.setdefault(A, {})

        if B is None:
            return links
        else:
            return links.get(B)

    def nodes(self):
        return list(self.dict.keys())

    def __repr__(self):
        return "<Graph with {} nodes and {} total edges>".format(len(self.dict), sum([len(self.dict[i]) for i in self.dict]))

    def save_to_disk(self, file_name="graph.json"):
        for i in self.dict:
            self.dict[i] = OrderedDict(sorted(self.dict[i].items()))
        self.dict = OrderedDict(sorted(self.dict.items()))

        with open(file_name, "w") as dump_file:
            json.dump(self.dict, dump_file, indent=4)


    def get_score(self, destination, path):
        path = [destination] + path
        score = 0
        for i in range(len(path)-1):
            score += self.dict[path[i]][path[i+1]][0]

        return score


    def get_dir(self, destination, path):
        path = [destination] + path
        dirs = []
        for i in range(len(path)-1):
            dirs.append(self.dict[path[i]][path[i+1]][1])

        return " | ".join(dirs)


    def find_all_paths(self, node, destination, visited, path):
        # print node, destination, path
        visited[node] = True
        path.append(node)

        if node == destination:
            old_score = self.score
            self.score = max(self.score, self.get_score(destination, path))
            if old_score != self.score:
                print self.score
                print path
                print self.get_dir(destination, path)

        else:
            # Best   (ntns)  node_new_node_score = lambda x: self.dict[node][x][0]
            # Meh?   (name)  name_of_node = None # key=None sorts based on name of node
            # Good   (nns)   new_node_score = lambda x: BOARD_SCORES[BOARD[int(x.split("_")[0])][int(x.split("_")[1])]]
            # Maybe  (nnos)  new_node_outbound = lambda x: sum(zip(*self.dict[x].values())[0])
            # Maybe  (nnoa)  new_node_outbound_ave = lambda x: sum(zip(*self.dict[x].values())[0]) / float(len(self.dict[x]))
            for i in sorted(self.dict[node], key=lambda x: self.dict[node][x][0], reverse=True):
            # for i in self.dict[node]:
                # print i
                if visited[i] == False:
                    self.find_all_paths(i, destination, visited, path)

        path.pop()
        visited[node] = False


    def traverse(self, node_to_start, starting_node="5_5"):
        visited = {}
        path = []
        for i in self.dict.keys():
            visited[i] = False

        # for neighbour in self.dict[starting_node]:
        for neighbour in [node_to_start]:
            print(neighbour)

            self.find_all_paths(neighbour, starting_node, visited, path)


class GraphBuilder:
    def __init__(self, board, board_scores):
        self.board = board
        self.board_size = len(self.board)
        self.board_scores = board_scores
        self.graph = Graph()

    def is_graph_node(self, row_id, col_id):
        """ Returs True/False if a node can be in a graph. Mountains/Cervices rule. """
        if row_id >= 0 and row_id < self.board_size and col_id >= 0 and col_id < self.board_size:
            node_type = self.board[row_id][col_id]
            if node_type != 1 and node_type != 2:
                return True
        return False


    def build_graph(self):
        for row_id, row in enumerate(self.board):
            for col_id, node_type in enumerate(row):
                if self.is_graph_node(row_id, col_id):
                    node_id = str(row_id) + "_" + str(col_id)
                    node_score = self.board_scores[node_type]

                    connected_nodes = self.get_connected_nodes(row_id, col_id)
                    for connected_node in connected_nodes:
                        # connect node_1, node_2 with weight
                        new_row_id, new_col_id = connected_node[0]
                        weight = connected_node[1]
                        path_str = connected_node[2]
                        new_node_id = str(new_row_id) + "_" + str(new_col_id)

                        self.graph.connect(node_id, new_node_id, weight, path_str)

        return self.graph


    def get_connected_nodes(self, row_id, col_id):
        """
            Returns list of all connected nodes with weights like [([1,2], 7), ([1,0], -2)]
        """
        connected_nodes = []

        combinations = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

        for combination in combinations:
            new_row_id = row_id + combination[0]
            new_col_id = col_id + combination[1]

            if self.is_graph_node(new_row_id, new_col_id):
                best_score, best_score_str = self.get_best_score(row_id, col_id, new_row_id, new_col_id)
                if best_score is not None:
                    connected_nodes.append(([new_row_id, new_col_id], best_score, best_score_str))

        return connected_nodes


    def get_paths(self, row_id, col_id, new_row_id, new_col_id):
        """ Gets paths between two points.
        Cares about mountains/crevices and doesn't return those paths
        """
        path_1, path_2 = [], []
        path_1_str, path_2_str = "", ""
        path_1_flag, path_2_flag = False, False

        # path_1
        if row_id > new_row_id:
            for i in range(row_id, new_row_id-1, -1):
                if not self.is_graph_node(i, col_id):
                    path_1_flag = True
                path_1.append([i, col_id])
                path_1_str += "N"
        else:
            for i in range(row_id, new_row_id+1):
                if not self.is_graph_node(i, col_id):
                    path_1_flag = True
                path_1.append([i, col_id])
                path_1_str += "S"
        # print path_1
        if col_id > new_col_id:
            for i in range(col_id-1, new_col_id-1, -1):
                if not self.is_graph_node(new_row_id, i):
                    path_1_flag = True
                path_1.append([new_row_id, i])
                path_1_str += "W"
        else:
            for i in range(col_id+1, new_col_id+1):
                if not self.is_graph_node(new_row_id, i):
                    path_1_flag = True
                path_1.append([new_row_id, i])
                path_1_str += "E"
        # print path_1

        # path_2
        if col_id > new_col_id:
            for i in range(col_id, new_col_id-1, -1):
                if not self.is_graph_node(row_id, i):
                    path_2_flag = True
                path_2.append([row_id, i])
                path_2_str += "W"
        else:
            for i in range(col_id, new_col_id+1):
                if not self.is_graph_node(row_id, i):
                    path_2_flag = True
                path_2.append([row_id, i])
                path_2_str += "E"
        # print path_2
        if row_id > new_row_id:
            for i in range(row_id-1, new_row_id-1, -1):
                if not self.is_graph_node(i, new_col_id):
                    path_2_flag = True
                path_2.append([i, new_col_id])
                path_2_str += "N"
        else:
            for i in range(row_id+1, new_row_id+1):
                if not self.is_graph_node(i, new_col_id):
                    path_2_flag = True
                path_2.append([i, new_col_id])
                path_2_str += "S"
        # print path_2

        paths, path_strs = [], []
        if not path_1_flag:
            paths.append(path_1[1:])
            path_strs.append(path_1_str[1:])
        if not path_2_flag:
            paths.append(path_2[1:])
            path_strs.append(path_2_str[1:])

        if paths:
            return paths, path_strs
        return None, None


    def get_best_score(self, row_id, col_id, new_row_id, new_col_id):
        paths, path_strs = self.get_paths(row_id, col_id, new_row_id, new_col_id)
        if paths is None:
            return None, None

        if len(paths) == 1:
            score = sum([self.board_scores[self.board[i][j]] for i, j in paths[0]])
            return score, path_strs[0]
        else:
            score_1 = sum([self.board_scores[self.board[i][j]] for i, j in paths[0]])
            score_2 = sum([self.board_scores[self.board[i][j]] for i, j in paths[1]])
            if score_1 > score_2:
                return score_1, path_strs[0]
            return score_2, path_strs[1]


if __name__ == "__main__":
    args = sys.argv
    try:
        node_to_start = args[1]
    except Exception as e:
        print "Usage: python main.py <node_to_start like '4_3' zero indexed>"
        print e
        sys.exit()

    graph_builder = GraphBuilder(BOARD, BOARD_SCORES)
    graph = graph_builder.build_graph()

    graph.traverse(node_to_start)
