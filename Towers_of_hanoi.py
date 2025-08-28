def tower_of_hanoi_moves(n, source, target, auxiliary):
    """
    Return a list of moves to solve Tower of Hanoi for n disks.
    Each move is a tuple: (disk_number, from_rod, to_rod).
    """
    moves = []

    def solve(k, s, t, a):
        # base case: one disk, move it directly
        if k == 1:
            moves.append((1, s, t))
            return
        # recursive case:
        # 1) move top k-1 disks from s to a, using t as helper
        solve(k - 1, s, a, t)
        # 2) move the largest disk k from s to t
        moves.append((k, s, t))
        # 3) move the k-1 disks from a to t, using s as helper
        solve(k - 1, a, t, s)

    solve(n, source, target, auxiliary)
    return moves


def simulate_and_print(n, source='A', target='C', auxiliary='B'):
    """
    Generate moves, then simulate them and print rod states step-by-step.
    """
    moves = tower_of_hanoi_moves(n, source, target, auxiliary)

    # Represent rods as lists where the last element is the top disk.
    rods = {
        source: list(range(n, 0, -1)),  # e.g. n=3 -> [3,2,1]
        auxiliary: [],
        target: []
    }

    def print_rods(step=None, move_desc=None):
        if step is not None:
            print(f"Step {step}: {move_desc}")
        for r in (source, auxiliary, target):
            print(f"  {r}: {rods[r]}")
        print()

    print("Initial state:")
    print_rods()

    for i, (disk, s, t) in enumerate(moves, start=1):
        popped = rods[s].pop()          # take top disk from source rod
        assert popped == disk, f"unexpected disk: {popped} vs {disk}"
        rods[t].append(disk)           # place it on target rod
        print_rods(step=i, move_desc=f"Move disk {disk} from {s} to {t}")

    print("Finished. All disks moved to target.\n")
    return moves


# Example run for 3 disks:
if __name__ == "__main__":
    simulate_and_print(3)

