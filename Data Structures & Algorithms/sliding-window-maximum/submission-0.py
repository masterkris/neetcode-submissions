class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # final list
        # can use double ended queue

        final = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # [1]
            # [2]
            # [2,1]
            # [2,1,0]
            # [4]
            # [4,2]
            # [6]

            if q[0] <= r - k:  # remove front if no longer inside window
                q.popleft()

            if r >= k - 1:  #  is window size k yet?, record max for that window
                final.append(nums[q[0]])
                l += 1
            r += 1

        return final
