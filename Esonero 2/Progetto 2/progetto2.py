from random import choice
from time import time
from Iterator import edgeIter
from datastruct.Stack import PilaArrayList as Stack
from graph.Graph_AdjacencyList import *
from unionfind.quickFind import *
from Performance import *

# decorator
def timer(func):
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)
        elapsed = time() - start
        edges = int(args[0].numEdges())
        print(f'Function {func.__name__}: {edges} edges, {elapsed} seconds')
        return value

    return wrapping_function


@timer
def hasCycleUF(graph):
    """
    :param graph: connected graph
    :return: boolean
    """
    qf = QuickFindBalanced()
    nodes = graph.getNodes()
    l = []
    if graph.numEdges() == 0:
        return False
    for i in nodes:
        qf.makeSet(i.id)
    for e in edgeIter(graph):
        if str(e) in l:
            continue
        else:
            head = e.head
            tail = e.tail
            l.append(str(graph.getEdge(tail, head)))
            l.append(str(graph.getEdge(head, tail)))
            if qf.find(qf.nodes[tail]) == qf.find(qf.nodes[head]):
                return True
            else:
                qf.union(qf.findRoot(qf.nodes[tail]), qf.findRoot(qf.nodes[head]))
    return False


@timer
def hasCycleDFS(graph):
    """
    :param graph: connected graph
    :return: boolean
    """
    if graph.numEdges() == 0:
        return False
    root = choice(graph.getNodes())
    rootId = root.id
    return hasCycleDFSiter(graph, rootId)


def hasCycleDFSiter(graph, nodeId):
    s = Stack()
    s.push(nodeId)

    explored = {nodeId}

    while not s.isEmpty():
        node = s.pop()
        explored.add(node)
        for adj_node in graph.getAdj(node):
            if adj_node not in explored:
                s.push(adj_node)
                for adj in graph.getAdj(adj_node):
                    if adj in explored and adj != node:
                        return True
    return False


if __name__ == "__main__":

    numNodes = 10
    hasCycle = True
    multipleCycles = True

    graph = graphBuilder(numNodes, hasCycle, multipleCycles)
    graph.print()

    print(hasCycleDFS(graph))
    print(hasCycleUF(graph))

    # Output should be True in both cases
