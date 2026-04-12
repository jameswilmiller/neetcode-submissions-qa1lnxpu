class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #system of linear equations
        #time on 1 axes
        #position on the other

        #lets say one starts at 3 with speed of 3 i.e slope of 3
        #slopes that intersect become a car fleet

        #how do we know if cars intersect?
        #calculate what time each car reaches the destination,
        #if car iwth lower position reaches destination at same time 
        #or before a later car then it became a car fleet 
        #arrives at position - distance / speed

        #will need to sort by position so O(n)logn

        #creates array of pairs position, speed for each car
        pair = [[p,s] for p,s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: #Reverse sorted order
            stack.append((target - p) / s) #time of arrival
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        
        