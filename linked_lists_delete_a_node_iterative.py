class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self,key):
        #Store the head node.
        temp = self.head

        #Check if list is empty.
        if temp is not None:
            #If list is not empty, check if the head contains the key.
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        #If not in head, treverse through list until we find the value and break out 
        # of the loop or we reach end of list. 
        #Keep track of previous node. It is needed to delete the desired node.
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #If end of list is reached without finding key, return nothing.
        if temp is None:
            return
        
        #Once found, Redirect the previous node's next argument to the 
        #target node's next argument.
        prev.next = temp.next

        #I think this removes the removed node from memory.
        temp = None

    def printList(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

def main():
    llist = LinkedList()
    llist.push('you')
    llist.push('with')
    llist.push('Justin Bieber')
    llist.push('love')
    llist.push('in')
    llist.push('Im')
    llist.deleteNode('Justin Bieber')
    llist.printList()
main()
        