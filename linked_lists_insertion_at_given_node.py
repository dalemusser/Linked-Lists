#Add a node after a given node (5 steps)
#We are given a pointer to a node, and the new node is 
#inserted after the given node.


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #This function inserts a new node after the given prev_node.
    def insertAfter(self,prev_node,new_data):
        #1. Check if the given prev_node exists.
        if prev_node is None:
            print('The given previous node must be in LinkedList.')
            return
        #2 & 3. initialize a new node & populate it with new_data
        new_node = Node(new_data)
        #4 Make next of new Node as next of previous Node.
        new_node.next = prev_node.next
        #5 Make next of prev_node as new_node.
        prev_node.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
def main():
    #Initialize a LinkedList object. This becomes the head
    #of the linked list.
    llist = LinkedList()

    llist.head = Node('Joshua')
    second = Node('Richard')
    third = Node('Martinez')

    llist.head.next = second
    second.next = third

    llist.insertAfter(second,'Musser')
    llist.printList()
    
main()