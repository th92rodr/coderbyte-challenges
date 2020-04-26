'''
Two sum problem

The two sum problem is a common interview question, and it is a variation of the subset sum problem.
There is a popular dynamic programming solution for the subset sum problem, but for the two sum problem we can actually write an algorithm that runs in O(n) time.
The challenge is to find all the pairs of two integers in an unsorted array that sum up to a given S.

For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7,
your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

https://coderbyte.com/algorithm/two-sum-problem
'''


'''
For each array element, add the sum complement (sum - current element) in a hash map,
by doing so if this added value is found later in the array, then a result pair was found.

There is only need to loop through the array once, resulting in a running time of O(n),
since each lookup and insertion in a hash table is O(1).
'''
def two_sum(array, sum):
    sum_complement = set()
    pairs = []

    for number in array:
        # check if this number exists in the hash table
        # if so then we found a pair of numbers that sum to the desired value
        if number in sum_complement:
            pairs.append([number, sum - number])
        # add the sum complement of the current number to the hash table
        else:
            sum_complement.add(sum - number)

    return pairs


print(' Array: [3, 5, 2, -4, 8, 11]\n Sum: 7\n Pairs:', two_sum([3, 5, 2, -4, 8, 11], 7))

print('\n Array: [4, 5, 1, 8]\n Sum: 6\n Pairs:', two_sum([4, 5, 1, 8], 6))
