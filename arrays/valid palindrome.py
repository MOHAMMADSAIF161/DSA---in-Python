# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s=("A man, a plan,a canal:panama").lower()#raceacar     racaecar
i=0
ch=''
for i in s:
    if ord('a')<=ord(i)<=ord('z'):
        ch+=i
p=0
a=len(ch)-1
while p<len(ch):
    if ch[p]!=ch[a]:
        print(False)
        break
    p+=1
    a-=1
else:
    print(True)