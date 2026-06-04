class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        n1=Node(data)
        if self.head is None:
            self.head=n1
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=n1
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print("None")


my_list=LinkedList()
(my_list.insert(10))
(my_list.insert("saif"))
(my_list.print_list())