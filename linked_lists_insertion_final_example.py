#A complete working program to demonstrate insertion methods of linked lists.

#Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked list head class
class LinkedList:
    def __init__(self):
        self.head = None

    #Function to insert a new node at the beginning.
    def push(self,new_data):

        #New node pupilated with data.
        new_node = Node(new_data)

        #Change next argument for new node to point to previous first node.
        new_node.next = self.head

        #Change head argument to reference new node
        self.head = new_node

    #Function to insert a new node after the given prev_node. 
    def insertAfter(self,new_data,prev_node):
        #Check if prev_node exists. (Only checking if input is None)
        if prev_node is None:
            print('prev_node must be in LinkedList')
            return
        #New node with data.
        new_node = Node(new_data)
        #Change new node to point to prev_node's next argument.
        new_node.next = prev_node.next
        #Change prev_node's next to point to new node.
        prev_node.next = new_node

    #Function to append a new node at end of linked list.
    def append(self,new_data):
        new_node = Node(new_data)
        #Treverse to end of linked list by following all the next arguments until you
        #hit one thay has the None value.

        #Check if linked list is empty. If it is, make the new_node the head.
        if self.head is None:
            self.head = new_node
            return
            
        while self.head != None:
            self.head = self.head.next
        self.head.next = new_node

    def printList(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

def main():
    #Initialize a linked list object.
    llist = LinkedList()
    #Fill list with first node using append.
    llist.append("falling in love")

    #Insert node in front/head of linked list.
    llist.push('I think')

    #Insert node between two existing nodes.
    #You need the previous node as an argument. Idk how tf you would get that without
    #treversing the whole list.
    target_n = llist.head
    while target_n.data != 'I think':
        target_n = target_n.next
    llist.insertAfter('im',target_n)

    llist.printList()

main()
        