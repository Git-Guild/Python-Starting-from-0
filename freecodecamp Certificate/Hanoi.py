def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []
    
    rods = [source, auxiliary, target]
    moves = []

    def record_move():
        moves.append(f'{rods[0]} {rods[1]} {rods[2]}')

    record_move()

    def solve(n, source, target, auxiliary):
        if n > 0:
            solve(n - 1, source, auxiliary, target)
            target.append(source.pop())
            record_move()
            solve(n - 1, auxiliary, target, source)

    solve(n, source, target, auxiliary)
    return '\n'.join(moves)