class node:
    def __init__(self,data):
        self.val=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        n1=node(data)
        if self.head==None:
            self.head=n1
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=n1
    def printing(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print(None)
sl=linkedlist()
(sl.insert(10))
(sl.insert(20))
sl.printing()


