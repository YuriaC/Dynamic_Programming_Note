def allCostruct(targetWord, wordbank):
    """
    m: targetWord length
    n: wordband size
    time complexity: O(n^m): exponential
    space complexity: O(m): just the depth of the recursion tree
    """
    if targetWord == '':
        return [[]]  # returns an empty two dimentional array

    else:
        construct_means = []
        for word in wordbank:
            if word in targetWord and targetWord.index(word) == 0:
                suffix = targetWord.replace(word, '', 1)
                result = allCostruct(suffix, wordbank)
                if isinstance(result, list):
                    for num in range(len(result)):
                        result[num].insert(0, word)
        
                    construct_means += result
        
        return construct_means

def allCostruct_memoized(targetWord, wordbank, memo = {}):
    """  
    in this case the memoized solution doesn't help to reduce either 
    time nor space complexity in the worst case
    """
    if targetWord == '':
        return [[]]  # returns an empty two dimentional array

    else:
        construct_means = []
        for word in wordbank:
            if word in targetWord and targetWord.index(word) == 0:
                suffix = targetWord.replace(word, '', 1)
                result = allCostruct(suffix, wordbank)
                if isinstance(result, list):
                    for num in range(len(result)):
                        result[num].insert(0, word)
        
                    construct_means += result

        memo[targetWord] = construct_means
        return construct_means

def main():
    targetWord = 'purple'
    wordbank = ['purp', 'le','p', 'ur', 'purpl']
    print(allCostruct(targetWord, wordbank))
    
    targetWord = 'abcdef'
    wordbank = ['ab', 'abc','cd', 'def', 'abcd','ef','c']
    print(allCostruct(targetWord, wordbank))

    targetWord_1 = 'eeeeeeeeeeeeeee'
    wordbank_1 = ['e', 'ee','eee', 'eeee', 'eeeee']
    print(allCostruct(targetWord_1, wordbank_1))

    print(allCostruct_memoized(targetWord_1, wordbank_1))


if __name__ == '__main__':
    main()