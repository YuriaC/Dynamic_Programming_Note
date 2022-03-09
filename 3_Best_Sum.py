import copy # for deep copy
""" optimization problem of the previous problem """

def BestSum(targetSum, numbers):
    """ returns the best combination (least number required) that sums 
    to be the targetSum. None if no combination exists 
    size of array = n
    size of targetSum = m
    time complexity: O(n^m*m)
    since the return value (array) can store up to m object 
    space complexity: O(m^2)
    """
    if targetSum == 0:
        return []
    
    elif targetSum < 0:
        return None

    else:
        best_sum = None
        for number in numbers:
            differences = targetSum - number
            result = BestSum(differences, numbers)
            if isinstance(result, list):
                result.append(number)
                if best_sum == None or len(result) < len(best_sum):
                    best_sum = result
         

        return best_sum

def BestSum_memoized(targetSum, numbers, memo = {}):
    """ returns the best combination (least number required) that sums 
    to be the targetSum. None if no combination exists 
    size of array = n
    size of targetSum = m
    time complexity O(n*m^2)
    space complexity O(m^2) [remain unchanged compare to the unmemoized version]
    """
    if targetSum in memo:
        return memo[targetSum]

    elif targetSum == 0:
        return []
    
    elif targetSum < 0:
        return None

    else:
        best_sum = None
        for number in numbers:
            differences = targetSum - number
            result = BestSum_memoized(differences, numbers, memo)
            if isinstance(result, list):
                result_copy = copy.deepcopy(result)
                result_copy.append(number)
                if best_sum == None or len(result_copy) < len(best_sum):
                    best_sum = result_copy
                              
        memo[targetSum] = best_sum  
        return best_sum

def main():
    targetSum = 969
    numbers = [1, 968, 25, 100, 7, 14]
    print(BestSum_memoized(targetSum, numbers))

if __name__ == '__main__':
    main()