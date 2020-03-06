#!/usr/bin/env python
# coding: utf-8
"""2020 March 05 - Daily Coding Problem #182."""
# <markdown>
# ## 2020 March 05 - Daily Coding Problem #182
#
# This problem was asked by Facebook.
#
# A graph is minimally connected if it is connected and there is no edge that
# can be removed while still leaving the graph connected. For example,
# any binary tree is minimally-connected.
#
# Given an undirected graph, check if the graph is minimally-connected.
# You can choose to represent the graph as either an adjacency matrix or
# adjacency list.


# %%
from copy import deepcopy


# %%
class Node:
    """Node class of a graph."""

    def __init__(self, value):
        """Initiate a node with given value."""
        self.val = value


class Graph:
    """Graph class from multiple Nodes."""

    def __init__(self):
        """Initiate an empty graph."""
        # Keeping nodes and edges separately for easy access
        self.nodes = list()
        self.adjacent = dict()

    def add_edge(self, node_1, node_2):
        """Add the edge between node 1 and 2 to the graph."""
        for node in (node_1, node_2):
            # Add node to the list if it's not already existed
            if node not in self.nodes:
                self.nodes.append(node)
                self.adjacent[node] = list()

        # Avoid adding existing edge
        if node_2 in self.adjacent[node_1] or node_1 in self.adjacent[node_2]:
            print('This edge already exist.')
            return None

        # Add the 2 ways edges
        self.adjacent[node_1].append(node_2)
        self.adjacent[node_2].append(node_1)

    def are_connected(self, start, end, passed=list()):
        """Check if the 2 nodes are connected."""
        if start == end:
            return True

        # Recursively move along the graph
        # Any one of the path reach the end node is counted as connected
        return any(
            self.are_connected(next_node, end, passed + [next_node])
            for next_node in self.adjacent[start]
            if next_node not in passed
        )

    def is_connected(self):
        """Check if the graph is connected."""
        # Loop through a set of 2 nodes
        # If they are all connected then the graph is connected
        # We only need 2Cn comparison
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                if not self.are_connected(self.nodes[i], self.nodes[j]):
                    return False
        return True

    def is_minimally_connected(self):
        """Check if the graph is minimally-connected."""
        # Check connectivity at each pair
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                # If there is no edge, skip this pair
                if self.nodes[j] not in self.adjacent[self.nodes[i]]:
                    continue
                # Create a copy of the graph
                # so the orginal graph is not mutated
                # Delete each edge to see if the graph is still connected
                # If it is, immediately return False
                copied_graph = deepcopy(self)
                node_1 = copied_graph.nodes[i]
                node_2 = copied_graph.nodes[j]
                node_1_id = copied_graph.adjacent[node_2].index(node_1)
                node_2_id = copied_graph.adjacent[node_1].index(node_2)
                copied_graph.adjacent[node_2].pop(node_1_id)
                copied_graph.adjacent[node_1].pop(node_2_id)
                if copied_graph.is_connected():
                    return False
        return True


# %%
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

# %%
small_graph = Graph()
small_graph.add_edge(a, b)
small_graph.add_edge(b, d)
small_graph.add_edge(d, c)
small_graph.add_edge(a, c)

print('Given the following graph:')
for key, adjacent in small_graph.adjacent.items():
    print(key.val, [ad.val for ad in adjacent])

print(
    'The graph is minimally-connected:',
    small_graph.is_minimally_connected()
)
# %%
small_graph = Graph()
small_graph.add_edge(a, b)
small_graph.add_edge(b, d)
small_graph.add_edge(d, c)

print('Given the following graph:')
for key, adjacent in small_graph.adjacent.items():
    print(key.val, [ad.val for ad in adjacent])

print(
    'The graph is minimally-connected:',
    small_graph.is_minimally_connected()
)
