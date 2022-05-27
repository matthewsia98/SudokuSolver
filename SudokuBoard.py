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
                    return i, j

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

    def is_valid_board(self):
        result = True

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] != 0:
                    result = result and self.is_valid(self.board[i][j], (i, j))

        return result

    def make_copy(self):
        copy = SudokuBoard()
        copy_board = [[],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      []]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                copy_board[i].append(self.board[i][j])

        copy.set_board(copy_board)
        return copy

    def is_solved(self):
        result = True

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                num = self.board[i][j]
                curr = (num != 0) and self.is_valid(num, (i, j))
                result = result and curr

        return result
    
    # One Solution
    def solve_one(self):
        empty = self.find_empty()

        if not empty:
            return True

        for num in range(1, 10):
            if self.is_valid(num, (empty[0], empty[1])):
                self.board[empty[0]][empty[1]] = num
                if self.solve_one():
                    self.solutions.append(self.make_copy())
                    return True
                self.board[empty[0]][empty[1]] = 0
        
        return False
       
    # Multiple Solutions
    def solve_all(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, (i, j)):
                            self.board[i][j] = num
                            for solution in self.solve_all():
                                yield solution
                            self.board[i][j] = 0
                    return

        yield self.make_copy()
        