class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #we can make a deque and if we get a value that is greater than prev values in the window
        # we can delete those values
        # in our dequeue values are always decreasing
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove the left value from the window
            if l > q[0]:
                q.popleft()

            # window needs to be of size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output






        