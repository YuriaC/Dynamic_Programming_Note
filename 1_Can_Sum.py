""" Decision Problem """

def howSum(targetSum, numbers):
    """ return True if any combination of number within numbers can sum up to the targetSum; 
    false otherwise 
    size of array numbers: n
    size of taretSum: n 
    time complexity: O(n^m)
    space complexity: O(m)
    """
    if targetSum == 0:
        return True
    
    elif targetSum < 0:
        return False

    else:
        for number in numbers:
            differences = targetSum - number
            result = howSum(differences, numbers)
            if result:
                return True
            
        return False

def howSum_memoized(targetSum, numbers, memo = {}):
    """
    size of array numbers: n
    size of taretSum: n 
    time complexity: O(n* m)
    space complexity: O(m)
    """
    if targetSum in memo: 
        return memo[targetSum]
    
    elif targetSum == 0:
        return True
    
    elif targetSum < 0:
        return False
    
    else: 
        for number in numbers:
            difference = targetSum - number
            result = howSum_memoized(difference, numbers, memo)
            if result:  # if result returns True
                memo[targetSum] = True
                return memo[targetSum]
        
        memo[targetSum] = False
        return memo[targetSum]

def main():
    targetSum = 300
    numbers = [7, 14]
    # print(howSum(targetSum, numbers))
    print(howSum_memoized(targetSum, numbers))

if __name__ == '__main__':
    main()