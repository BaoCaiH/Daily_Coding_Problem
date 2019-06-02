#!/usr/bin/env python
# coding: utf-8
"""2019 May 26th - Daily_Coding_Problem #131."""
# <markdown>
# ## 2019 May 26th - Daily_Coding_Problem #131
#
# Problem: Given the head to a singly linked list,
# where each node also has a “random” pointer that points to anywhere
# in the linked list, deep clone the list.


# %%
class Node:
    """Node class for the linked list."""

    def __init__(self, value):
        """Initialize the node."""
        self.value = value
        self.next = None
        self.rand = None


class singlyLinkedList:
    """Singly linked list."""

    def __init__(self):
        """Initialize the list with an empty head."""
        self.head = None
        self.tail = None

    def addItemToTail(self, value):
        """Add new item to the end of the list."""
        if not self.tail:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node

    def addItemToHead(self, value):
        """Add new item to the beginning of the list."""
        if not self.head:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def printList(self):
        """Print the entire list, from head to tail."""
        if not self.head:
            print("The list is empty")
        else:
            n = self.head
            while n:
                print(n.value)
                n = n.next

    def deepClone(self):
        """Return a clone of the list, even the random pointer."""
        if not self.head:
            print("The list is empty")
        else:
            newList = singlyLinkedList()
            n = self.head
            indexToNewItems = {}
            itemToIndex = {}
            i = 0
            while n:
                newList.addItemToTail(n.value)
                indexToNewItems[i] = newList.tail
                itemToIndex[n] = i
                n = n.next
                i += 1
            n = self.head
            m = newList.head
            while n:
                m.rand = indexToNewItems[itemToIndex[n.rand]]
                n = n.next
                m = m.next
        return newList


# %%
a = Node('a')
b = Node('b')
a.next = b
c = Node('c')
b.next = c
d = Node('d')
c.next = d
e = Node('e')
d.next = e
a.rand = a
b.rand = a
c.rand = e
d.rand = c
e.rand = c
linkedList = singlyLinkedList()
linkedList.head = a
linkedList.tail = e
linkedList.printList()
clonedList = linkedList.deepClone()

# %%
clonedList.head.next.next.rand.value
