class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        #When you use a while loop like this with a variable, 
        #it will loop as long as the variable has any kind of 
        #value that isnt blank or 'None'.
        #If the variable never becomes None or blank, it will
        #loop forever.
        while temp:
            print(temp.data)
            temp = temp.next

def main():
    #Start with an empty list.
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #Connect the nodes together.
    llist.head.next = second
    second.next = third

    llist.printList()
main()
