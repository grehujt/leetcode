# from collections import Counter  ## get TLE!!!
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d1 = {}
        for w in words:
            if w not in d1:
                d1[w] = 1
            else:
                d1[w] += 1
        singleLen, wordsCnt = len(words[0]), len(words)
        result = []
        for i in xrange(len(s) - singleLen * wordsCnt + 1):
            d2 = {}
            j = 0
            while j < wordsCnt:
                key = s[i+j*singleLen:i+(j+1)*singleLen]
                if key not in d1:
                    break
                if key not in d2:
                    d2[key] = 1
                else:
                    d2[key] += 1
                    if d2[key] > d1[key]:
                        break
                j += 1
            if j == wordsCnt:
                result.append(i)
        return result
Solution().findSubstring('abcba',['a','b'])

