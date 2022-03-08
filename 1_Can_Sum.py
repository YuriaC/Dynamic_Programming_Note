def howSum(targetSum, numbers):
    """ return True if any combination of number within numbers can sum up to the targetSum; false otherwise """
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


def main():
    targetSum = 7
    numbers = [8]
    print(howSum(targetSum, numbers))

if __name__ == '__main__':
    main()