class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        nums = []

        for i in range(rows):
            for j in range(cols):
                elem = board[i][j]
                if elem != '.':
                    row = (elem, i)
                    column = (j, elem)
                    subgrid = (i // 3, j // 3, elem)

                    nums.append(row)
                    nums.append(column)
                    nums.append(subgrid)

        return len(nums) == len(set(nums))

"""
Time: O(N^M)
Space: O(N^M)
"""
