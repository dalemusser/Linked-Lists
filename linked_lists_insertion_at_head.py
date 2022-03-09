#Adding a node to the front/head of the list.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        #1 & 2: Allocate the Node & put in the data
        #(aka) Create a new Node object instance and feed
        #it the new value.
        new_node = Node(new_data)
        #3. set the 'next' property of the new Node as head.
        new_node.next = self.head

        #4. Move the head point to the new Node.
        self.head = new_node
    def printList(self):
        #Grab the first node in the linked list.
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next



def main():
    #initialize a linked list head
    llist = LinkedList()
    #Initialize first node.
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.push(10)

    llist.printList()
main()


