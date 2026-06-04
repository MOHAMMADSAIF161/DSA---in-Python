class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class SLL:
    def __init__(self):
        self.head=None
        self.last=None
    def is_empty(self):
        if self.head==None:
            return True
    def insert_at_first(self,data):
        new_node=Node(data,next=self.head)
        self.head=new_node
        if self.last is None:
            self.last=new_node
    def insert_at_last(self,data):
        new_node=Node(data,next=None)
        if self.head==None:
            self.head=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
    def insert_at_postion(self,postion,data):
        if postion <0:
            print("invalid postion")
            return
        new_node=Node(data)
        if postion==0:
            new_node.next=self.head
            self.head=new_node
        if self.last is not None:
            self.last=new_node
            return
        current=self.head
        index=0
        while current is not None and index<postion-1:
            current=current.next
            index +=1
            

        if new_node.next==None:
            self.last=new_node



    def display(self):
        current=self.head
        while current :
            print(current.data)
            current=current.next
        print("None")
        
        

s1=SLL()
(s1.insert_at_first(30))
(s1.insert_at_first(40))
(s1.insert_at_last(29))
s1.insert_at_postion(3,45)
s1.display()