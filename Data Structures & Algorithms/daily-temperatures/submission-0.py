class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic decreasing stack problem
        #first we initiliase a stack of length temperatures
        #in the stack we store pairs of temp and index
        #for each temp in temperatures we check if the temp is greater than the temp at the top of the stack
        # if it is we pop that temp and store that temps index - the popped items index in the output array
        # once we complete the loop we append the current temp and index to the stack
        # then the output will be an array holding all the i - stackindex 



        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


        






        
        