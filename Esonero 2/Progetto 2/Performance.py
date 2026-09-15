from progetto2 import *
import random
from graph.Graph_AdjacencyList import *


def graphBuilder(n, cycle, multipleCycles=False):
    """
        :param n: number of node, Integer
        :param cycle: cyclic or acyclic, boolean
        :param multipleCycles: /
        :return: connected non-oriented graph
        """

    graph = GraphAdjacencyList()

    # add nodes
    nodes = []
    for i in range(n):
        node = graph.addNode(i)
        nodes.append(node)

    if cycle and n > 2:
        if multipleCycles:
            num = random.randint(n + 1, (n ** 2 - n)/2)
        else:
            num = n
    elif not cycle:
        num = n - 1
    else:
        raise Exception("You used an invalid inputType parameter!")

    # connect all nodes
    l = []  # list of already existing edges
    for node_src in nodes:
        for node_dst in nodes:
            if graph.numEdges() == 2 * num:
                break
            else:
                if node_src != node_dst and str(graph.getEdge(node_src.id, node_dst.id)) not in l \
                        and str(graph.getEdge(node_dst.id, node_src.id)) not in l:
                    graph.insertEdge(node_src.id, node_dst.id,
                                     node_src.id + node_dst.id)
                    graph.insertEdge(node_dst.id, node_src.id,
                                     node_src.id + node_dst.id)
                    l.append(str(graph.getEdge(node_dst.id, node_src.id)))
                    l.append(str(graph.getEdge(node_src.id, node_dst.id)))

    return graph


if __name__ == "__main__":
    hasCycle = True
    for i in range(1, 7):
        n = 2500 * i
        graph = graphBuilder(n, hasCycle)
        hasCycleUF(graph)
        hasCycleDFS(graph)
