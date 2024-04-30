# need to know how to build two singly-linked lists 
# iterate through all and reverse numbers 
# add values
# split each value 
# add each value to a third linked list 
# return data from linked list

# What I don't know
# how to make a linked list in python
# how to iterate through each value in linked list
# reverse a linked list
# add each value in linked list
# split the values 
# return linked list 

# actual pseudocode
# initialize current node to dummy head of the returning list
# initialize carry to 0
# initialize p and q to head of l1 and l2 respectively
# Loop through lists l1 and l2 until you reach both ends
    # set x to node p's value. if p has reached the end of l1, set to 0.
    # set y to node q's value. if q has reached the end of l2, set to 0.
    # set sum = x + y + carry
    # update carry = sum/10
    # create a new node with the digit value of (sum mod 10) and set it to current node's next, then advance 
    # current node to next.
    # advance both p and q. 
# Check if carry = 1, if so append a new node with digit 1 to the returning list.
# Return dummy head's next node.

# https://www.geeksforgeeks.org/linked-list-set-1-introduction/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0 
        
        while l1 or l2 or carry: 
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next