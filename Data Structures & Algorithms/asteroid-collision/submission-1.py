class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # res stack
        # for asteroid in asteroids
        # by default, append (at the end)
        # right left get destroyed, so positive negative
        # key is destroy smaller one
        # return res

        res = []
        
        for asteroid in asteroids:
            while res and res[-1] > 0 and asteroid < 0: # while collision condition, right left
                if abs(asteroid) > res[-1]: # abs. value matters for size
                    res.pop()
                    continue
                elif abs(asteroid) == res[-1]:
                    res.pop()
                break # exit while loop
            
            else:
                res.append(asteroid)
        
        return res

            



        