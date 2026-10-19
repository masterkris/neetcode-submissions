class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        # BFS approach
        q = deque([("0000", 0)]) # starting combo, turns
        seen = set()
        seen.add("0000")
        
        while q:
           lock, turns = q.popleft()

           if lock == target:
              return turns
            
           # try rotating each of the 4 digits
           # skip deadends and seen
           # if queue empties and no match, return -1

           for i in range(4):
              digit = int(lock[i])

              for move in [-1, 1]:
                new_lock = [digit for digit in lock] # copy over old lock

                new_digit = (digit + move) % 10
                new_lock[i] = str(new_digit)
                new_lock = "".join(new_lock)

                if new_lock not in seen and new_lock not in dead:
                    q.append((new_lock, turns + 1))
                    seen.add(new_lock)
        
        return -1


           
        



        