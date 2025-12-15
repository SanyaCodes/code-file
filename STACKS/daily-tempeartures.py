# Daily Temperatures
"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the key here is to maintain a stack such that:
        # it only contains the indices that have not been solved for
        # temp[stack[0]] > temp[stack[1]]>...

        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i-index
            stack.append(i)
        
        return answer
