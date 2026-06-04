# """Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases."""
# n=[1,3,7,2,-3]
# def expand(o: list)->bool:
#     l=0
#     r=l+1
#     a=[]
#     while r<=len(n)-1:
#         a.append(abs(o[l]-o[r]))
#         l+=1
#         r+=1
#     if a==sorted(a) and len(a)==len(set(a)):
#         return True
#     else:
#         return False
# print(expand(n))
# """Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l."""
# p=[-1,-2,3,7]
# def sumsqare(nums:list)->list:
#     even_sum=0
#     odd_sum=0
#     for num in nums:
#         if num%2==0:
#             even_sum+=num**2
#         else:
#             odd_sum+=num**2
#     return [odd_sum,even_sum]
#print(sumsqare(p))
# """A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix"""
# l=[[3]]
# res=list(zip(l[0],l[1]))
# print(res)
l=[1,2,3]
print(l.extend(2))