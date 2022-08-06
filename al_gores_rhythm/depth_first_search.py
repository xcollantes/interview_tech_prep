"""Depth First Search or DFS.

Recursive algorithm for traversing a graph structure by
reaching each node until the end is found then returning to the previously
visited nodes until a new one is visited.

Time complexity is O(V + E) where V is the number of vertices in a
graph and E is the number of edges.

# Depth First vs Breadth First

There are two methods to traverse a graph data structure:
    - Depth First Search
    - Breadth First Search

Both will work with the same result to traverse a graph structure but a Depth
First Search is simpler if you want to visit every node in the tree.

Note that pre-order and other forms of tree traversal are a form of DFS.

If you want to find the shortest path in a graph, then BFS is preferred.  For
example, if using DFS, you'd have to traverse the length of the tree even
two nodes are near each other horizontally.

# Representation

To represent vertices, there are two options:
    - Adjacency list: tuples of vertices and their connection.  If Vertex A
    has an edge with Vertex B, then it would be represented with `(A,B)`.  If
    the edge is not directed or the edge is two way, then there would be two
    tuples, `(A,B)` and `(B,A)`.
    - Adjacency matrix: a table representation where the vertices are listed on
    the header and left side of the table and the values are true or false
    depending if there is an edge between the two vertices.  This is less
    efficient compared to the list since you'd have to traverse the table N*N
    times.

# Use cases

Topological sorting, scheduling problems, graph cycle detection,
and solving puzzles with one solution such as traverse a maze or
solve a sudoku puzzle all require the use of DFS.  Computer networking
uses DFS for example if a network is bipartite.

Recursive process:


Iterative process:
    1. Start on a node.
    2. Start with 2 stacks: stack A for tracking adjacent nodes and stack B
       for tracking visited nodes.
    3. Push all adjecent nodes onto stack A.
    4. For each node visited, push onto stack B.
    5. Visit each node on stack A.

Sources:
    https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm
    https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal.htm
    https://favtutor.com/blogs/depth-first-search-python
    https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
"""

import logging
from typing import Any

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    # Graph is undirected since e refers back to 1, 2, and 3.
    #
    #    0
    #  / | \
    # 1  2  3
    #  \ | /
    #    4
    graph: list(tuple(int, int)) = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 1),
        (4, 2),
        (4, 3),
    ]
    graph_two: dict(int, int) = {
        0: [1, 2, 3],
        1: [4],
        2: [4],
        3: [4],
        4: [1, 2, 3]
    }

    # Get all vertices in a single place
    # vertex_set: set(Any) = set()
    # for vertex1, vertex2 in graph_two:
    #     vertex_set.add(vertex1)
    #     vertex_set.add(vertex2)

    visited: dict(Any, bool) = {vertex: False for vertex in graph_two.keys()}

    logging.info("Visited tracker: %s", visited)
    logging.info("Graph: %s", graph_two)

    logging.info("DFS recursive")
    dfs_recusive(visited, graph_two, list(graph_two.keys())[0])

    logging.info("DFS iterative")

    # dfs_iterative(visited, graph_two, list(graph_two.keys())[0])


def dfs_recusive(visited: dict, graph: dict, node: Any):
    """Traverse the entire graph and print out values.

    Args:
        visited: Hash map of nodes and if we have visited it.
        graph: The entire graph.
        node: Current node.
    """
    if not visited[node]:
        logging.info("Visited new node: %s", node)
        visited[node] = True

        for adjacent_node in graph[node]:
            dfs_recusive(visited, graph, adjacent_node)


# def dfs_iterative(visited: dict, graph: dict, node: Any):
#     """Traverse the entire graph and print values using stacks.

#     Args:
#         See dfs_recursive().
#     """
#     adjacent_stack: list = []

#     for n in graph:
#         if not visited[n]:
#             visited[n] = True
#             logging.info("Visited new node: %s", n)
#             for adjacent_node in graph[n]:
#                 adjacent_stack.append(n)

#             while adjacent_node:


if __name__ == "__main__":
    main()
