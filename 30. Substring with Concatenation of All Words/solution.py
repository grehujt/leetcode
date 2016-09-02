# from collections import Counter  ## slow!!!
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d1 = {}
        for w in words:
            d1[w] = d1[w]+1 if w in d1 else 1
        singleLen, wordsCnt, result, i = len(words[0]), len(words), [], 0
        totalLen = singleLen * wordsCnt
        for i in xrange(min(singleLen, len(s)-totalLen+1)):
            d2, left, right = {}, i, i
            while right + singleLen <= len(s):
                key = s[right : right+singleLen]
                right += singleLen
                if key not in d1:
                    d2 = {}
                    left = right
                else:
                    d2[key] =  d2[key]+1 if key in d2 else 1
                    while d2[key] > d1[key]:
                        d2[s[left : left+singleLen]] -= 1
                        left += singleLen
                    if right-left == totalLen:
                        result.append(left)
        # print result
        return result
Solution().findSubstring('abcba',['a','b'])
# Solution().findSubstring("barfoothefoobarman",["foo","bar"])
Solution().findSubstring("ababaab",["ab","ba","ba"])

