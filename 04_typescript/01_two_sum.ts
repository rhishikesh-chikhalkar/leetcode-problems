/**
 * @param nums number[]
 * @param target number
 * @returns number[]
 */
function twoSum(nums: number[], target: number): number[] {
    const seen: Map<number, number> = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement: number = target - nums[i];

        if (seen.has(complement)) {
            return [seen.get(complement) as number, i];
        }

        seen.set(nums[i], i);
    }

    return []; // unreachable as per problem guarantee
}

function runTest(nums: number[], target: number): void {
    const result = twoSum(nums, target);
    console.log(`nums=${JSON.stringify(nums)} target=${target} --> result=${JSON.stringify(result)}`);
}

// Sample LeetCode tests
runTest([2, 7, 11, 15], 9);
runTest([3, 2, 4], 6);
runTest([3, 3], 6);

export {};
