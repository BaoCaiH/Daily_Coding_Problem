#!/usr/bin/env python
# coding: utf-8
"""A doubly linked list object."""
# <markdown>
# For future use of course


# %%
class Node:
    """Node class for the linked list."""

    def __init__(self, value):
        """Initialize the node."""
        self.value = value
        self.next = None
        self.prev = None


class doublyLinkedList:
    """Doubly linked list."""

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
            node.prev = self.tail
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
            self.head.prev = node
            self.head = node

    def addItemAfterPosition(self, value, position):
        """Add new item after a selected location, count from 0."""
        if not self.head:
            print("The list is empty")
        else:
            n = self.head
            p = 0
            while n:
                if p == position:
                    break
                n = n.next
                p += 1
            if not n:
                print("The position is outside the list")
            else:
                node = Node(value)
                node.prev = n
                node.next = n.next
                if n.next:
                    n.next.prev = node
                n.next = node

    def printList(self):
        """Print the entire list, from head to tail."""
        if not self.head:
            print("The list is empty")
        else:
            n = self.head
            while n:
                print(n.value)
                n = n.next

    def pop(self, position=None):
        """Delete the last item or the item at the given position."""
        if not self.head:
            print('The list is empty')
        elif position:
            n = self.head
            p = 0
            while n:
                if p == position:
                    n.prev.next = n.next
                    if n.next:
                        n.next.prev = n.prev
                    return n.value
                n = n.next
                p += 1
            print("The index is outside the list")
        else:
            n = self.tail
            n.prev.next = None
            self.tail = n.prev
            return n.value

    def reverse(self):
        """Reverse the given list."""
        if not self.head:
            print("The list is empty")
        else:
            n = self.head
            next = n.next
            n.next = None
            n.prev = next
            self.tail = n
            while next:
                next.prev = next.next
                next.next = n
                n = next
                next = next.prev
            self.head = n

    def copy(self):
        """Return a copy of the list."""
        if not self.head:
            print("The list is empty")
        else:
            newList = doublyLinkedList()
            n = self.head
            while n:
                newList.addItemToTail(n.value)
                n = n.next
            return newList
