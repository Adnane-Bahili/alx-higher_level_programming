#!/usr/bin/python3
"""defines classes for singly-linked list"""


class Node:
    """represents a node in singly-linked list"""
    def __init__(self, data, next_node=None):
        """initializes new Node
        arguments:
            data (int): new Node data
            next_node (Node): new Node next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set the data of Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get/set the next_node of Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """represents singly-linked list"""
    def __init__(self):
        """initalizes new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts new Node to SinglyLinkedList
        node is going to be inserted into list at a specific
        position(numerically ordered)
        argument:
            value (Node): new Node, to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """defines "print()" representation of SinglyLinkedList"""
        vals = []
        temp = self.__head
        while temp is not None:
            vals.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(vals))
