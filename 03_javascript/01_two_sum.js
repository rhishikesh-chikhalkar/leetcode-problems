/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const seen = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (seen.has(complement)) {
            return [seen.get(complement), i]
        }

        seen.set(nums[i], i);
    }

    return []; // unreachable as per problem guarantee
};

function runTest(nums, target) {
    const result = twoSum(nums, target);
    console.log(`nums=${JSON.stringify(nums)} target=${target} --> result=${JSON.stringify(result)}`);
}

// Sample LeetCode tests
runTest([2, 7, 11, 15], 9);
runTest([3, 2, 4], 6);
runTest([3, 3], 6);
