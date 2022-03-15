def countCostruct(targetWord, wordbank):
    """time and space complexity is the same as the preious example"""
    if targetWord == '':
        return 1  # 1 way to construct the target word

    else:
        construct_count = 0
        for word in wordbank:
            if word in targetWord and targetWord.index(word) == 0:
                suffix = targetWord.replace(word, '', 1)
                result = countCostruct(suffix, wordbank)
                construct_count += result

        return construct_count

def countCostruct_memoized(targetWord, wordbank, memo = {}):
    """time and space complexity is the same as the previous example"""
    if targetWord in memo:
        return memo[targetWord]

    elif targetWord == '':
        return 1  # 1 way to construct the target word
    
    else:
        construct_count = 0
        for word in wordbank:
            if word in targetWord and targetWord.index(word) == 0:
                suffix = targetWord.replace(word, '', 1)
                result = countCostruct_memoized(suffix, wordbank, memo)
                construct_count += result

        memo[targetWord] = construct_count
        return construct_count  # no feasible way to construct the target word



def main():
    targetWord = 'abcdef'
    wordbank = ['ab', 'abc','cd', 'def', 'abcd']
    print(countCostruct(targetWord, wordbank))
    
    targetWord_1 = 'eeeeeeeeeeeeeeef'
    wordbank_1 = ['e', 'ee','eee', 'eeee', 'eeeee']
    print(countCostruct_memoized(targetWord_1, wordbank_1))

if __name__ == '__main__':
    main()