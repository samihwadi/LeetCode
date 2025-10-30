class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Using hashmap to have sets of unique rows, columns and sub-boxes
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)

        # 9x9 individual cells, 9 rows and 9 columns
        # Check value for every row and every column, if duplicates present, return False
        # Break down 9x9 into 3x3 sub-boxes
        # Check if sub-boxes include duplicates
        for row in range(9):
            for column in range(9):
                # If cell is empty, move on to next cell
                if board[row][column] == ".":
                    continue
                if (board[row][column] in rows[row] or board[row][column] in columns[column] or board[row][column] in sub_boxes[row//3, column//3]):
                    return False
                else:
                    rows[row].add(board[row][column])
                    columns[column].add(board[row][column])
                    sub_boxes[row//3, column//3].add(board[row][column])
        return True


        