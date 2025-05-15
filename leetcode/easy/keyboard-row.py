# https://leetcode.com/problems/keyboard-row/
class Solution(object):
    def findWords(self, words):
        row1=list("qwertyuiop")
        row2=list("asdfghjkl")
        row3=list("zxcvbnm")
        result = []
        for word in words:
            lower_word = word.lower()
            if all(char in row1 for char in lower_word) or \
               all(char in row2 for char in lower_word) or \
               all(char in row3 for char in lower_word):
                result.append(word)
        return result


words = ["Hello","Alaska","Dad","Peace"]
solution=Solution()
print(solution.findWords(words))