# Xavier's ultimate technical interview prep

Specially annotated with procedures and different options such as optimizations.

## Recommended course

<https://www.programiz.com/dsa/>

## Interview structure

An interviewer may as questions about you, your resume, what you like to do,
or what you hope to accomplish.  The interviewee should prepare for these
questions but this guide will focus on the purely technical interviews.  

### Prep

Use this repo to prepare for the Data Structures and Algorithms portion of
the interview.  

Read all of [*Cracking the Coding Interview by Gayle Laakmann McDowell*](https://engbookspdf.xyz/uploads/pdf/Cracking%20The%20Coding%20Interview%206th%20Edition%20by%20Laakmann.pdf)

Along with Data Structures and Algorithms, interviewer may also ask you about:

- Linux system administration commands
- How the internet works
- How a computer works
- How to structure a web server

These topics are not covered here.  

### During the interview

1. Get to know who's interviewing you.  
1. Listen carefully to the interviewer's question.  
1. IMPORTANT: Ask clarifying questions.  
    - "What are we optimizing for?  Time, space, speed?"

1. Speak your thoughts on how to structure the solution:
   Think upfront and get issues out of the way to avoid
   completely changing the solution you're coding halfway through.  

1. Clarify use cases, look for most obvious case, look for edge cases.  

1. Think of the most direct solution which could be a brute force solution.  

1. Optimize your solution.

1. Ask for feedback.  

TIPS: Feel free to ask for help.

## Data structures

Different ways to store data.

Visualizing sorting algorithms:

- <https://visualgo.net/en/bst?slide=1>
- <https://www.cs.usfca.edu/~galles/visualization/BST.html>

### Hashing

A Hash Table is a way to store data after being processed by a Hash Function.  
The Hash Table will contain data with a Key and Value pair.  

Hash collision:
When a Hash Function creates duplicate Keys and a conflict is created where that
Key is stored.

Resolve Hash collisions by choosing a technique:
    - resolve by "chaining"
    - resolve through "open addressing"
        - linear/quadratic probing
        - double hashing

Chaining:
When a collision is found, store the new data using a Doubly Linked List.

![Hash chaining](https://cdn.programiz.com/sites/tutorial2program/files/Hash-3_1.png)

Open addressing:
Instead of storing multiple values in one slot in the Hash Table, each slot
has one value or left NULL. Use either Linear probing or Double Hashing.

Linear probing:
If conflict is found, place value in next slot.  

```python
i = some index
m = some mod 
hash_function(key, value) = (hash_function_prime(key) + i) % m
```

If there is a conflict at i + 1, then check i + 2, and so on.  The value will
be placed until an open slot if found in a linear iteration.

Downfall of Linear addressing: If a cluster of slots are occupied, then the
whole cluster must be iterated on.

Quadratic probing:
Checks for an open slot like Linear probing but instead of +1 for increments,
each increment is larger.  

Double hashing:
If a collision is found, use another hash function to find next slot.

### Linear data structures

Arrays, linked lists, stacks, and queue are linear data structures where
performing operations increases in time complexity with the increase of input
data.

### Tree structures

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

## Big O

Big O notation is used as a metric to express efficiency for an algorithm.  

[![Big graph](https://miro.medium.com/max/700/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)](https://www.bigocheatsheet.com/)

<https://www.bigocheatsheet.com>

**NOTE:** This is an extremely important topic in interviews. You must understand
this concept.

> Imagine the following scenario: You've got a file on a hard drive and you need to send it to your friend who lives across the country. You need to get the file to your friend as fast as possible. How should you send it? Most people's first thought would be email, FTP, or some other means of electronic transfer. That thought is reasonable, but only half correct. If it's a small file, you're certainly right. It would take 5 - 10 hours to get to an airport, hop on a flight, and then deliver it to your friend. But what if the file were really, really large? Is it possible that it's faster to physically deliver it via plane? Yes, actually it is. A one-terabyte (1 TB) file could take more than a day to transfer electronically. It would be much faster to just fly it across the country. If your file is that urgent (and cost isn't an issue), you might just want to do that. What if there were no flights, and instead you had to drive across the country? Even then, for a really huge file, it would be faster to drive.

Excerpt from *Cracking The Coding Interview 6th Edition by Laakmann*.

Big O is useful since comparing an algorithm on a 2022 MacBook Pro will run
differently on a Commodore 64 from 1982.  Further, depending on what other
programs are running on your computer, the algorithm may perform differently
depending on the day and time you run it.  To eliminate as many variables
when measuring algorithms, Big O can be used since it measures an algorithm
on Time or Space Complexity, independent of uncontrolled variables.  

### Time complexity

[Asymptotic relationship](https://en.wikipedia.org/wiki/Asymptotic_analysis)
between inputs and growth outputs.  

### Space complexity

Recursive function add to Space complexity since each recursive call adds
to the call stack.  If a binary tree is traversed, then complexity would be
as large as the height of the tree since returning from a level would remove
the occupying space.  

### Dropping constants

A common mistake when calculating Big O is keeping constants as part of the
calculation.  Consider the two examples:

**Example 1**

```python
for x in range(len(some_array)):
    if x < 10: 
        print("some output")
    if x > 10:
        print("some output")
```

**Example 2**

```python
for x in range(len(some_array)):
    if x < 10: 
        print("some output")

for x in range(len(some_array)):
    if x > 10:
        print("some output")
```

Example 1 has one loop of some array which performs two comparison operations
where Example 2 has two loops of the same array and each loop performs a single
comparison operation.  

At first you might say Time Complexity of Example 1 is O(n) and Example 2 is
O(2n).  But Big O doesn't consider the constants and the 2 is dropped.  

Constants are dropped because the Big O measures the growth of results.  Once
the inputs grow to huge values, then the constants are insignificant.  That's
how Big O works.  

That's not to say Example 1 is more efficient, Example 1 is more efficient.  
Big O is concerned with the growth of inputs as opposed to overall efficiency.  

## Dynamic programming

Keep track of values to do less work.  

### Memoization

Example: Fibonacci sequence `f(x) = f(x - 1) + f(x - 2); f(1) = 1; f(2) = 1`

```python
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

This solution without memoization will compute the same value multiple times
such as `fib(3)`, `fib(1)`, etc.

**With memoization:**

```python
memo: dict[int, int] = dict()

def fib(n, memo):
    if memo[n]:  # O(1)
        return memo[n]
    if n == 1 or n == 2:  # O(1)
        return 1
    else:
        memo[n] = fib(n - 1) + fib(n - 2)  # O(2n)
```

Without memoization time complexity: O(2n + 1) since you call `fib()` twice
for every `n` value.

With memoization time complexity: O(2n + 1) * O(1) since each operation
takes O(1).  This results to O(n) since we drop constants.

<https://www.youtube.com/watch?v=P8Xa2BitN3I>

<https://www.youtube.com/watch?v=vYquumk4nWw>
