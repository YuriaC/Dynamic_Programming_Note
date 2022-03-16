def fib_generator(term):
    """
    time complexity: O(n^2)
    space complexity O(1)

    """
    if 0 < term <= 2:
        return 1
    
    else:
        return fib_generator(term - 1) + fib_generator(term - 2)
    
def fib_generator_memoized(term, memo = {}):
    """
    time complexity: O(n)
    space complexity O(n)
    """
    if term in memo: 
        return memo[term]
    
    elif 0 < term <= 2:
        return 1
    
    else:
        memo[term] = fib_generator_memoized(term - 1) + fib_generator_memoized(term - 2)
        return memo[term]


def fib_tabulation(term):
    """ O(n) time, O(n) space"""
    table = [0] * (term + 2)  # initialize a term-size array with initialized value = 0
    table[0] = 0
    table[1] = 1
    for index in range(term):
        table[index + 1] += table[index]
        table[index + 2] += table[index]

    return table[term]

def main():
    term = 100   
    # result = fib_generator(term)  # expect long run time
    # result = fib_generator_memoized(term) 
    result = fib_tabulation(6)
    print(result)

if __name__ == '__main__':
    main()
