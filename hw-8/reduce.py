# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""
-1 Restate the problem
    - take a number, divide by 2, count how many steps to get to 0. subtract 1 when odd

-2 Ask clarifying questions
    -

-3 State your assumptions
    - I need a counter
    - i can do this with a while loop

-4 Think out loud
  -4a Brainstorm solutions
        - use a while loop with if statements t
  -4b Explain your rationale
        - while the number is > 0 i can have the ifs check for even or odd, then do the division
  -4c Discuss tradeoffs
        - 
  -4d Suggest improvements
        - 


"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num % 2 == 1
                num = (num - 1)
            counter += 1
        return counter
