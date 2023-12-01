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
                    txt += ' '
                txt += str(self.puzzle[j+i])
            txt += '\n'
        return txt

    def move(self, direction):
        new_state = PuzzleState(list(self.puzzle))
        if direction == 'up' and new_state.blk >= 3:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk - 3] = (
                new_state.puzzle[new_state.blk - 3],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk -= 3
        elif direction == 'down' and new_state.blk < 6:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk + 3] = (
                new_state.puzzle[new_state.blk + 3],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk += 3
        elif direction == 'left' and new_state.blk % 3 != 0:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk - 1] = (
                new_state.puzzle[new_state.blk - 1],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk -= 1
        elif direction == 'right' and (new_state.blk + 1) % 3 != 0:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk + 1] = (
                new_state.puzzle[new_state.blk + 1],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk += 1
        else:
            return None
        return new_state

def depth_limit_search(initial_state, goal_state, limit = 5):
    stack = [(initial_state, [])]
    visited = set()

    current_state = initial_state
    path = []
    while stack:

        if current_state.puzzle == goal_state.puzzle:
            return path

        visited.add(tuple(current_state.puzzle))

        for direction in ['up', 'down', 'left', 'right']:

            if len(path) == limit:
                break

            new_state = current_state.move(direction)

            if new_state and tuple(new_state.puzzle) not in visited:
                stack.append((new_state, path + [direction]))            
        
        current_state, path = stack.pop()

        print(f'move {len(path)}', path)

    return None

if __name__ == '__main__':
    
    initial_puzzle = [1,2,3,0,4,6,7,5,8]
    goal_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    initial_state = PuzzleState(initial_puzzle)
    goal_state = PuzzleState(goal_puzzle)

    solution_path = depth_limit_search(initial_state, goal_state,10)
    print(('*'*100+'\n')*3)
    if solution_path:
        print(f"Solution Path {len(solution_path)} moves : \n{solution_path}")
        
        current_state = initial_state
        for step, direction in enumerate(solution_path):
            print(f"Step {step + 1}: Move {direction}")
            current_state = current_state.move(direction)
            print(current_state)
            print('*' * 30)
        
    else:
        print("No solution found.")