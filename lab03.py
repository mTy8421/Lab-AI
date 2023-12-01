class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.blk = puzzle.index(0)
    
    def __str__(self):
        txt = ''

        for i in range(0, self.size, 3):
            for j in range(3):
                if j > 0:
                    txt += ''
                txt += str(self.puzzle[j+i])
            txt += '\n'
        return txt