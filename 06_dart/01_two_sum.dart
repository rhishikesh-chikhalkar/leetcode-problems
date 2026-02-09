void main() {
  runTest([2, 7, 11, 15], 9);
  runTest([3, 2, 4], 6);
  runTest([3, 3], 6);
}

List<int> twoSum(List<int> nums, int target) {
  final Map<int, int> seen = {};

  for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];
    if (seen.containsKey(complement)) {
      return [seen[complement]!, i];
    }
    seen[nums[i]] = i;
  }
  return []; // unreachable as per problem guarantees
}

void runTest(List<int> nums, int target) {
  final result = twoSum(nums, target);
  print('nums=$nums target=$target --> result=$result');
}
