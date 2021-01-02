class SudokuBoard:
    def __init__(self):
        self.solutions = []
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

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
        self.solutions = []

    def set_board(self, board):
        self.board = board
        self.solutions = []

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
        global solutions
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, (i, j)):
                            self.board[i][j] = num
                            if not self.solve():
                                self.board[i][j] = 0
                    return
        print("SOLUTION")
        #self.print_board()
        #print()
        solution = SudokuBoard()
        solution.set_board(self.board)
        solution.print_board()
        solutions.append(solution)
        #input("\nAlternate Solution?\n")
    '''
'''
solutions = []
board1 = [[0, 0, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 0, 0, 9],
          [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0],
          [0, 0, 1, 0, 5, 0, 9, 3, 0],
          [0, 0, 4, 0, 0, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2],
          [1, 2, 0, 0, 0, 7, 4, 0, 0],
          [0, 4, 9, 2, 0, 6, 0, 0, 0]]

board2 = [[7, 8, 5, 4, 3, 9, 1, 2, 6],
          [6, 1, 2, 8, 7, 5, 3, 4, 9],
          [4, 9, 3, 6, 2, 1, 5, 7, 8],
          [8, 5, 7, 9, 4, 3, 2, 6, 1],
          [2, 6, 1, 7, 5, 8, 9, 3, 4],
          [9, 3, 4, 1, 6, 2, 7, 8, 5],
          [5, 7, 8, 3, 9, 4, 6, 1, 2],
          [1, 2, 6, 5, 8, 7, 4, 9, 3],
          [3, 4, 9, 2, 1, 6, 8, 5, 0]]
b = SudokuBoard()
b.set_board(board1)
print("ORIGINAL")
b.print_board()
print()
b.solve()
print()
print(type(solutions))
print(type(solutions[0]))
solutions[0].print_board()
'''