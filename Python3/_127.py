class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        wordLen = len(beginWord)
        lookSet = {beginWord}
        checkSet = {endWord}
        dist = 2

        while lookSet:
            newLookSet = set()

            for word in lookSet:
                for i in range(wordLen):
                    for c in string.ascii_lowercase:

                        if c != word[i]:
                            newWord = word[:i ] + c + word[i + 1:]

                            if newWord in checkSet:
                                return dist

                            if newWord in wordList:
                                newLookSet.add(newWord)
                                wordList.remove(newWord)

            dist += 1
            lookSet = newLookSet

            if len(checkSet) < len(lookSet):
                lookSet, checkSet = checkSet, lookSet

        return 0