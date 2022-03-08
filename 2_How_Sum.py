def howSum(targetSum, numbers):
    """ return any combintation of number within numbers that can sum up to the targetSum """
    if targetSum == 0:
        return []
    
    elif targetSum < 0:
        return None

    else:
        for number in numbers:
            differences = targetSum - number
            result = howSum(differences, numbers)
            if isinstance(result, list):
                result.append(number)
                return result
            
        
        return None

def howSum_memoized(targetSum, numbers, memo = {}):
    """ return any combintation of number within numbers that can sum up to the targetSum """
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
                result.append(number)
                memo[targetSum] = result
                return memo[targetSum]
            
        memo[targetSum] = None
        return memo[targetSum]


def main():
    targetSum = 300
    numbers = [7, 14]
    print(howSum_memoized(targetSum, numbers))

if __name__ == '__main__':
    main()