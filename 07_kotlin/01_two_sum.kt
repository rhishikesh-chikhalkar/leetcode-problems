
fun twoSum(nums: IntArray, target: Int): IntArray{
    val seen = HashMap<Int, Int>()

    for(i in nums.indices){
        val complement = target - nums[i]

        if (seen.containsKey(complement)){
            return intArrayOf(seen[complement]!!, i)
        }

        seen[nums[i]] = i
    }
    return intArrayOf() // unreachable as per problem
}


fun runTest(nums: IntArray, target: Int){

    val result = twoSum(nums, target)

    println("nums=${nums.contentToString()} target=$target --> result=${result.contentToString()}")
}

fun main(args: Array<String>) {
    // Sample LeetCode tests
    runTest(intArrayOf(2, 7, 11, 15), 9)
    runTest(intArrayOf(3, 2, 4), 6)
    runTest(intArrayOf(3, 3), 6)
}