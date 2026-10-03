class Solution:
    def climbStairs(self, n: int) -> int:

        two_steps_behind = 1
        one_step_behind = 1

        for i in range(n - 1):
            current = one_step_behind + two_steps_behind

            two_steps_behind = one_step_behind
            one_step_behind = current
        
        return one_step_behind
        