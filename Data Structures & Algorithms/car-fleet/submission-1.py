class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # fleet = same pos, same speed, also single car

        cars = []

        for i in range(len(position)): # save both pos. and speed
            cars.append([position[i], speed[i]])
        

        cars.sort(reverse = True) # closest to target to farthest

        stack = []

        for car in cars:

            pos = car[0]
            speed = car[1]

            # how long to reach target --> slope
            time = (target - pos) / speed

            # does car form fleet?
            if len(stack) > 0 and time <= stack[-1]: # catches up
                continue
            
            stack.append(time) # new fleet
        
        return len(stack)





        

        
        