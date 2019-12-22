'''
Print all subsets (power set) of a given set

The input for this problem will be an array of numbers representing a set, which only contains unique numbers,
and your goal is to print every possible set combination, otherwise known as the power set.

For example:
input set = [1, 2, 3]
power set = [ [], [1], [2], [3], [1, 2], [2, 3], [1, 3] [1, 2, 3] ]

The power set contains every possible combination of numbers.
It also includes the empty set which contains no numbers from the original set.

https://coderbyte.com/algorithm/print-all-subsets-given-set
'''


'''
There will be 2N possible combinations of a set of length N,
because every element can either be in the set or not, which gives us 2 possibilities,
and we do this for N numbers, giving us 2 * 2 * 2 ... = 2^N.

(1) Loop from 0 to 2^N
(2) For each number get the binary representation of the number, example: 3 = 011
(3) Determine from the binary representation whether or not to include a number from the set, example: 011 = [exclude, include, include]
'''
def power_set(set):
    response = []

    # loop from 0 to 2^N
    for x in range(0, pow(2, len(set))):
        print('\nnumber:', x, '|| binary:', bin(x))

        # get the binary representation of the number
        # and put each digit in a list position
        binary = list(bin(x))

        # delete the first two characters which are '0b'
        del binary[0:2]

        # fill the list with left zeros
        # padding the binary number so 1 becomes 001 for example
        while len(binary) < len(set):
            binary.insert(0, 0)

        # convert all the elements to integers
        binary = list(map(int, binary))
        print('binary list:', binary)

        # determine from the binary representation whether or not to include a number from the set
        # building the combination that matches the 1's in the binary number
        res = []
        for index in range(len(binary)):
            if (binary[index]):
                res.append(set[index])

        # add the new combination to the response
        response.append(res)

    response.sort()
    return response


print(' Input Set: [1, 2, 3]\n Output:', power_set([1, 2, 3]))
