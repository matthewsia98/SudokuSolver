class SudokuBoard:
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self):
        pass

    def clear_board(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def set_board(self, board):
        self.board = board

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - ")
            for j in range(len(self.board)):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(self.board[i][j], end=" ")
                if j == 8:
                    print()

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return (i, j)

        return False

    def is_valid(self, num, pos):
        row = pos[0]
        col = pos[1]

        for j in range(len(self.board)):
            if self.board[row][j] == num and j != col:
                return False

        for i in range(len(self.board)):
            if self.board[i][col] == num and i != row:
                return False

        quadrant_row = row // 3
        quadrant_col = col // 3

        for i in range(3 * quadrant_row, 3 * quadrant_row + 3):
            for j in range(3 * quadrant_col, 3 * quadrant_col + 3):
                if (self.board[i][j] == num) and ((i, j) != pos):
                    return False

        return True
    '''
    # One Solution
    def solve(self):
        empty = self.find_empty()

        if not empty:
            return True

        for num in range(1, 10):
            if self.is_valid(num, (empty[0], empty[1])):
                self.board[empty[0]][empty[1]] = num
                if self.solve():
                    return True
                self.board[empty[0]][empty[1]] = 0

        return False
    '''
    # Multiple Solutions
    def solve(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, (i, j)):
                            self.board[i][j] = num
                            self.solve()
                            self.board[i][j] = 0
                    return
        self.print_board()
        input("Alternate Solution?")


board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]
b = SudokuBoard()
b.set_board(board)
b.print_board()
print("\n SOLVING \n")
b.solve()

