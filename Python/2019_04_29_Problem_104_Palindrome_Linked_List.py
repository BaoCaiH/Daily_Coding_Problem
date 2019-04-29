#!/usr/bin/env python
# coding: utf-8
"""2019 April 29th - Daily_Coding_Problem #104."""
# <markdown>
# ## 2019 April 29th - Daily_Coding_Problem #104
#
# Problem: Determine whether a doubly linked list is a palindrome.
# What if it’s singly linked?
#
# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.


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
            if n.prev:
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

    def isPalindrome(self):
        """Check whether the list is a palindrome."""
        if not self.head:
            print("The list is empty")
        else:
            referenceList = self.copy()
            n = self.head
            while n:
                if n.value != referenceList.pop():
                    return False
                n = n.next
            return True


# %%
dll1 = doublyLinkedList()
dll1.addItemToTail(1)
dll1.addItemToTail(2)
dll1.addItemToTail(3)
dll1.addItemToTail(4)
dll1.printList()
dll1.isPalindrome()

# %%
dll2 = doublyLinkedList()
dll2.addItemToTail(1)
dll2.addItemToTail(4)
dll2.addItemToTail(3)
dll2.addItemToTail(4)
dll2.addItemToTail(1)
dll2.printList()
dll2.isPalindrome()
