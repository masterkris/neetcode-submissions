class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # declare rows, cols
        # if i == len(word), we have found word, so return True
        # i is index of character MATCHED
        # check if within bounds. if not, return False.
        # mark current spot in grid
        # can use "#" for this
        # run dfs in all 4 dirs
        # restore cell after exploring (backtracking) - use temp variable for this
        
        # iterate through grid
        # run dfs from (r, c, 0)
        # if true, return True
        # else return False

        # Time: O(m*n*3^L) -> 3 choices per character
        # Space: O(L) -> word length

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "mark"

            run_one = dfs(r, c + 1, i + 1)
            run_two = dfs(r + 1, c, i + 1)
            run_three = dfs(r - 1, c, i + 1)
            run_four = dfs(r, c - 1, i + 1)

            board[r][c] = temp # backtracking
            return run_one or run_two or run_three or run_four
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False




        