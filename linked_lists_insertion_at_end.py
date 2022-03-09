#When adding a new node to the end, the new node is always added after 
#the last node of the given LnkedList. 
#ex. If the given LinkedList is 5->10->15->25 and we add item 30 at the 
#end, then the LinkedList becomes 5->10->15->25->30.
#Since linked lists are represented by their head, we have to treverse 
#the list till the end and then change the next to last node to a new node.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        #1 & 2. Create a new node & populate it with the new data.
        new_node = Node(new_data)
        #3. Set new_node's next property to None since it will be the last node.
        new_node.next = None
        #4.If the LinkedList is empty, then make new_node the head of the LinkedList.
        if self.head is None:
            self.head = new_node
            return
        #5. If the LinkedList isnt empty, treverse until the last node.
        last = self.head
        while last.next:
            last = last.next

        #6. Change the 'next' property of the second to last node (previously the last node) 
        #from 'None' to point to the new last node.
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
def main():
    #Initialize a LinkedList object.
    llist = LinkedList()

    llist.head = Node('Joshua')
    second = Node('Richard')

    llist.head.next = second
    llist.append('Martinez')

    llist.printList()
main()