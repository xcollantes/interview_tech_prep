# Xavier's ultimate technical interview prep

Specially annotated with procedures and different options such as optimizations.

## Recommended course

<https://www.programiz.com/dsa/>

## Recommended reading

<https://engbookspdf.xyz/uploads/pdf/Cracking%20The%20Coding%20Interview%206th%20Edition%20by%20Laakmann.pdf>

## Sorting algorithms

Stable sort type:
Elements with identical values are sorted in the same order.  For example,
in an array `[4, 6, 4, 1, 0]`, the sorted form would be `[0, 1, 4, 4, 6]`.  
A stable algorithm would sort the array with the duplicate values in the same order
where the first 4 in the unsorted array also comes first in the sorted array.  

Usually in sorting, we don't differentiate with duplicate values.  But in
practice, the duplicate numbers could represent something (like being tied to
some address).  

Comparison based algorithm

Counting based algorithm

Big O

## Linear data structures

Arrays, linked lists, stacks, and queue are linear data structures where
performing operations increases in time complexity with the increase of input
data.

## Tree structures

Tree:
Collection of linked nodes.  Use a tree to perform operations in more efficient
time complexity than linear data structures.

Forest:
Collection of disjoint trees.

Node:
A single leaf in the tree which contains a key or value and pointers to the
child nodes.

Edge:
Link between two nodes.

Height of a Node:
Number of edges from the node to the deepest leaf.

Leaf:
Node of tree with no children.

### Binary tree

A tree where each node can possibly have up to 2 children.

Perfect binary tree:
All nodes have 0 or 2 children and all leaf nodes are at the same level.

Full binary tree:
All nodes have 0 or 2 children.

Complete tree:
Every level is filled, all leaf elements have 0, 1, or 2 children but if a node
has only one child, it's the left child.

Relationship between an array and trees:
A complete binary tree can have its children and parents with `2i + 1` to find the
left child and `2i + 2` to find the right child where `i` is the index of the
array.

The parent can be found with the opposite: `(i - 1) / 2`.

![programwiz.com](https://cdn.programiz.com/cdn/farfuture/yBcZxf7VSecOV66J8-kdwS0lX5mah3oLZzWcbRNqFog/mtime:1586942656/sites/tutorial2program/files/array-vs-heap-indices.png)

### n-nary tree

A tree where each node can possibly have 0 to infinitely many children.

### B-tree or Balanced tree

## Graphs

Graph:
Collection of nodes connected by edges.  

Vertex:
A single node in a graph.  

Edge:
Connection between two vertices.

Directed graph: Graph where the edges are in only one direction as opposed
to nodes where the edge is two way.  

Acylical graph:
