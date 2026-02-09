package main

import "fmt"

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for i, num := range nums {
		complement := target - num

		if idx, ok := seen[complement]; ok {
			return []int{idx, i}
		}

		seen[num] = i
	}

	return []int{} // unreachable as per problem
}

func runTest(nums []int, target int) {
	result := twoSum(nums, target)
	fmt.Printf("nums=%v target=%d --> result=%v\n", nums, target, result)
}

func main() {
	runTest([]int{2, 7, 11, 15}, 9)
	runTest([]int{3, 2, 4}, 6)
	runTest([]int{3, 3}, 6)
}
