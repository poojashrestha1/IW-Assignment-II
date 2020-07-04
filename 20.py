'''Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]'''

class SumZero:

    def check(self, numbers):
        length = len(numbers)
        result = []
        for i in range(0,length-2):
            for j in range(i+1,length-1):
                for k in range(j+1, length):
                    if (numbers[i] + numbers[j] + numbers[k] == 0):
                        result.append([numbers[i], numbers[j], numbers[k]])
        return result


numbers = [-25, -10, -7, -3, 2, 4, 8, 10]

print(SumZero().check(numbers))
