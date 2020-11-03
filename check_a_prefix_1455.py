# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        str = sentence.split()
        a = 0
        for search in str:
            if search.startswith(searchWord):
                a = str.index(search)+1
                break
            else:
                a = -1
        return a