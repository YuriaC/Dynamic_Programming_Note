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


def main():
    term = 100   
    # result = fib_generator(term)  # expect long run time
    result = fib_generator_memoized(term) 
    print(result)

if __name__ == '__main__':
    main()
