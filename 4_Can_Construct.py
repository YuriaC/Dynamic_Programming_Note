def canConstruct(targetWord, wordbank):
    if targetWord == '':
        return True
    
    else:
        for word in wordbank: 
            if word in targetWord:
                if targetWord.index(word) == 0:
                    suffix = targetWord.strip(word)
                    result = canConstruct(suffix, wordbank)
                    if result:
                        return True
        
        return False
    
def main():
    targetWord = 'albado'
    wordbank = ['ab', 'abc', 'cd', 'def', 'abcd']
    print(canConstruct(targetWord, wordbank))

if __name__ == '__main__':
    main()


