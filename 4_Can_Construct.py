from operator import truediv


def canConstruct(targetWord, wordbank):
    """
    targetWord length = m
    wordbank length = n
    time complexity = O(n^m*m) multiplying m due to spliting operation
    space complexity O(m^2)
    """
    if targetWord == '':
        return True
    
    else:
        for word in wordbank: 
            if word in targetWord and targetWord.index(word) == 0: 
                suffix = targetWord.replace(word, "", 1)  # only let the replacment happen once
                result = canConstruct(suffix, wordbank)
                if result:
                    return True
        
        return False

def canConstruct_memoized(targetWord, wordbank, memo = {}):
    """
    targetWord length = m
    wordbank length = n
    time complexity = O(n*m^2) multiplying m due to spliting operation
    space complexity O(m^2)
    """
    if targetWord in memo:
        return memo[targetWord]

    elif targetWord == '':
        return True
    
    else:
        for word in wordbank: 
            if word in targetWord and targetWord.index(word) == 0:
                suffix = targetWord.replace(word, "", 1)  # only let the replacment happen once
                result = canConstruct_memoized(suffix, wordbank, memo)  
                if result:
                    memo[targetWord] = True
                    return True
        
        memo[targetWord] = False
        return False
    
def main():
    targetWord = 'eeeeeeeeeeeeeeef'
    wordbank = ['e', 'ee', 'eee', 'eeee', 'eeeeef']
    print(canConstruct_memoized(targetWord, wordbank))


if __name__ == '__main__':
    main()


