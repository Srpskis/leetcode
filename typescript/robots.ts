const isValidTimeSeries = (grid: number[][], numRobots: number): boolean => {
    //STEP 1: Hadle empty time series
    if (grid.length === 0) return numRobots === 0;
    
    // Step2: Extract the occupied positions from every snapshot
    const allPositions: number[][] = [];
    for (const row of grid) {
        let positions: number[] = [];
        row.forEach((value, index) => {
            if (value === 1) positions.push(index);
        });

        // Step3: Verify the expected number of robots
        if (positions.length !== numRobots) return false;
        allPositions.push(positions);   
    }
    // STEP 4: Compare each snapshot with the next snapshot
    for (let t = 0; t < allPositions.length - 1; t++) {
        const currentPositions = allPositions[t];
        const nextPositions = allPositions[t+1];

        // STEP 5: Match robots by their left-to-right order
        for (let i = 0; i <numRobots; i++) {
            // STEP 6: Calculate how far this robot would move
            const distance = Math.abs(nextPositions[i] - currentPositions[i]);

            // STEP 7: Reject the series if distance is greater than 1
            if (distance > 1) return false;
        }
    }
    // STEP 8: Every robot passes every transition
    return true;
};

type TestCase = [string, [number[][], number], boolean];

const runTests = (
    fn: (grid: number[][], numRobots: number) => boolean,
    cases: TestCase[]
): void => {
    let failed = 0;

    cases.forEach(([name, args, expected], index) => {
        const actual = fn(...args);
        const passed = actual === expected;
        if (!passed) failed += 1;
        const status = passed ? "PASS" : "FAIL";
        console.log(
            `${status}  ${index + 1}. ${name}: got=${actual} expected=${expected}`
        );
    });

    const total = cases.length;
    console.log(`\n${total - failed}/${total} passed`);
    if (failed) {
        throw new Error(`${failed} test(s) failed`);
    }
};

runTests(isValidTimeSeries, [
    [
        "two robots move toward each other",
        [
            [
                [1, 0, 0, 1],
                [0, 1, 1, 0],
            ],
            2,
        ],
        true,
    ],
    [
        "second robot has no valid next position",
        [
            [
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0],
            ],
            2,
        ],
        false,
    ],
    [
        "robots stay in place",
        [
            [
                [1, 0, 1],
                [1, 0, 1],
            ],
            2,
        ],
        true,
    ],
    [
        "one robot moves too far",
        [
            [
                [1, 0, 0, 0],
                [0, 0, 0, 1],
            ],
            1,
        ],
        false,
    ],
    [
        "snapshot has the wrong robot count",
        [
            [
                [1, 0, 1],
                [1, 0, 0],
            ],
            2,
        ],
        false,
    ],
    [
        "zero robots on an empty row",
        [[[0, 0, 0]], 0],
        true,
    ],
]);
