import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }

            seen.put(nums[i], i);
        }

        return new int[] {};
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        runTest(solution, new int[] { 2, 7, 11, 15 }, 9);
        runTest(solution, new int[] { 3, 2, 4 }, 6);
        runTest(solution, new int[] { 3, 3 }, 6);
    }

    private static void runTest(Solution solution, int[] nums, int target) {
        int[] result = solution.twoSum(nums, target);
        System.out.printf("nums=%s target=%d --> result=%s%n",
                Arrays.toString(nums), target, Arrays.toString(result));
    }
}
