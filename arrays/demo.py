class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=None
    def is_empty(self):
         return self.start==None
    def insert_at_start(self,data:int):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data:int):
        n=Node(data,next=None)
        if not self.is_empty():
            temp =self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def insert_at_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n 
    def search(self,data:int):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next






        


             


        

#driver code:
my_list=SLL()
my_list.insert_at_start(20)
my_list.insert_at_last(40)
my_list.print_list()
