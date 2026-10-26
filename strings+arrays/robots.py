# Given a grid of robot positions, indicate if it is a valid time series for the number if robots specified if robots can only travel up to 1 index further their position 1 step before.
# Input format: an array of arrays, of which each index can be 0 or 1.
# An index corresponds to the physical location which is either occupied by a robot (1) or empty (0).

# Examples: 
# Grid= [[1,0,0,1],[0,1,1,0]] is a valid time series for 2 roots because the first robot moved from index 0 to index 1 and robot 2 moved from idex 3 to index 2.
# Grid=[[1,0,0,0,1],[1,0,1,0,0]] is not valid because the second robot started at index 4 but did not have a valid position on the next step.

# Assumptions:
# - You will be given the number of robots as well as the grid.
# - Number of robots can be 0 or greater.
# - Minimum length of these arrays will be 1.
# - Robots cannot collide or occupy the same index.

# Example:
# Number of robots = 2
# Grid = [[1,0,0,1],[0,1,1,0]]
# Output: True

# Number of robots = 2
# Grid = [[1,0,0,0,1],[1,0,1,0,0]]
# Output: False


# Solution ------------------------------------------------------------------------------------------------

# Key observation: Robots cannot collide, so they cannot pass one another. Their left-to-right order must remain the same. That means that we can match the first robot in one snapshot to the first robot in the next snapshot, the second to the second, and so on.
# [[1,0,0,1],[0,1,1,0]] -> current_position = [0, 3], next_position = [1, 2] -> compare corresponding positions to see if the distance is at most 1. If it is, then the time series is valid.

# Algorithmic technique: Linear scan

# Implementation:

def is_valid_time_series(grid, num_robots):
    # STEP 1: Handle an empty time series.
    if not grid:
        return num_robots == 0

    # STEP 2: Extract the occupied positions from every snapshot.
    # Each list is automatically sorted because we scan left to right.
    all_positions = []

    for row in grid:
        positions = []
        for index, value in enumerate(row):
            if value == 1:
                positions.append(index)

        # STEP 3: Verify the expected number of robots.
        if len(positions) != num_robots:
            return False

        all_positions.append(positions)

    # STEP 4: Compare each snapshot with the next snapshot.
    for t in range(len(all_positions) - 1):
        current_positions = all_positions[t]
        next_positions = all_positions[t + 1]

        # STEP 5: Match robots by their left-to-right order.
        # Since robots cannot collide or pass each other,
        # the first robot stays first, the second stays second, etc.
        for i in range(num_robots):

            # STEP 6: Calculate how far this robot would move.
            distance = abs(
                next_positions[i] - current_positions[i]
            )

            # STEP 7: Reject the series if a robot moves too far.
            if distance > 1:
                return False

    # STEP 8: Every robot passed every transition.
    return True


def run_tests(fn, cases):
    failed = 0
    for i, (name, args, expected) in enumerate(cases, 1):
        actual = fn(*args)
        passed = actual == expected
        if not passed:
            failed += 1
        status = "PASS" if passed else "FAIL"
        print(f"{status}  {i}. {name}: got={actual!r} expected={expected!r}")

    total = len(cases)
    print(f"\n{total - failed}/{total} passed")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    run_tests(
        is_valid_time_series,
        [
            (
                "two robots move toward each other",
                ([[1, 0, 0, 1], [0, 1, 1, 0]], 2),
                True,
            ),
            (
                "second robot has no valid next position",
                ([[1, 0, 0, 0, 1], [1, 0, 1, 0, 0]], 2),
                False,
            ),
            (
                "robots stay in place",
                ([[1, 0, 1], [1, 0, 1]], 2),
                True,
            ),
            (
                "one robot moves too far",
                ([[1, 0, 0, 0], [0, 0, 0, 1]], 1),
                False,
            ),
            (
                "snapshot has the wrong robot count",
                ([[1, 0, 1], [1, 0, 0]], 2),
                False,
            ),
            (
                "zero robots on an empty row",
                ([[0, 0, 0]], 0),
                True,
            ),
        ],
    )


