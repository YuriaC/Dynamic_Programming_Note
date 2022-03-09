import copy  # emable deep copy 
""" cominatoric problem of the original problem """

def howSum(targetSum, numbers):
    """ return any combintation of number within numbers that can sum up to the targetSum 
    size of array = n
    size of targetSum = m
    time complexity: O((n^m)*m) (exponential time)
    since the return value (array) can store up to m object 
    space complexity: O(m^2)

    """
    if targetSum == 0:
        return []
    
    elif targetSum < 0:
        return None

    else:
        for number in numbers:
            differences = targetSum - number
            result = howSum(differences, numbers)
            if isinstance(result, list):
                result_copy = copy.deepcopy(result)
                result_copy.append(number)
                return result_copy
        
        return None

def howSum_memoized(targetSum, numbers, memo = {}):
    """ return any combintation of number within numbers that can sum up to the targetSum 
    size of array = n
    size of targetSum = m
    time complexity: O(n*m^2) (polynomial time)
    since the return value (array) can store up to m object 
    space complexity: O(m^2)
    
    """
    if targetSum in memo:
        return memo[targetSum]

    elif targetSum == 0:
        return []
    
    elif targetSum < 0:
        return None

    else:
        for number in numbers:
            differences = targetSum - number
            result = howSum_memoized(differences, numbers, memo)
            if isinstance(result, list):
                result_copy = copy.deepcopy(result)
                result_copy.append(number)
                memo[targetSum] = result_copy
                return memo[targetSum]
            
        memo[targetSum] = None
        return memo[targetSum]


def main():
    targetSum = 300
    numbers = [7, 14]
    print(howSum_memoized(targetSum, numbers))

if __name__ == '__main__':
    main()