"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.


"""

from typing import List
# Solution (wrong because adding before it exists)
# also not brute force because O(n) is the fastest this could ago.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n):
            if((i % 3 and i % 5) == 0):
                answer[i] == "FizzBuzz"
            elif((i % 5)):
                answer[i] == "Buzz"
            elif((i % 3)):
                answer[i] == "Fizz"
            else:
                answer[i] == i 
        return(answer)

# correct answer
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if(i % 3 == 0 and i % 5 == 0):
                answer.append("FizzBuzz")
            elif(i % 5 == 0):
                answer.append("Buzz")
            elif(i % 3 == 0):
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return(answer)