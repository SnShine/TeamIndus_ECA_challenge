from main import *
import sys

print "Usage: python experiments.py <start node> <remove nodes <= to>"
node_to_start = sys.argv[1]
remove_nodes_less_than = int(sys.argv[2])

graph_builder = GraphBuilder(BOARD, BOARD_SCORES)
graph = graph_builder.build_graph()

print graph

# remove poorly performing edges
for i in graph.dict.keys():
    for j in graph.dict[i].keys():
        if graph.dict[i][j][0] <= remove_nodes_less_than:
            print i, j
            graph.remove_connection(i, j)

print graph

graph.traverse(node_to_start)
