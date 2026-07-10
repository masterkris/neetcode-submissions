class Solution:
    def climbStairs(self, n: int) -> int:

        # n = 2
        # 1 + 1 = 2

        one_step_behind = 1   # only 1 way for both to be at step 0
        two_steps_behind = 1

        for i in range(n - 1):
            current = one_step_behind + two_steps_behind

            two_steps_behind = one_step_behind
            one_step_behind = current
        
        return one_step_behind

    # At each step, current ways come from:
    # 1) taking one step from the previous stair
    # 2) taking two steps from two stairs back
    # so:
    # current = one_step_behind + two_steps_behind
        