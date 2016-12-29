class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def process_row(row, rowLen, isLast=False):
            cnt = len(row)
            if rowLen == maxWidth:
                return ' '.join(row)
            elif cnt == 1 or isLast:
                return '%s%s' % (' '.join(row), ' ' * (maxWidth-rowLen))
            else:
                ret = [row[0]]
                avgSpaces = (maxWidth-rowLen)/(cnt-1) + 1
                mod = (maxWidth-rowLen) % (cnt-1)
                for i in range(cnt-1):
                    numSpaces = avgSpaces+1 if i < mod else avgSpaces
                    ret.append('%s%s' % (' ' * numSpaces, row[i+1]))
                return ''.join(ret)

        ret = []
        row, rowLen, wordCnt = [words[0]], len(words[0]), len(words)
        for i in range(1, wordCnt):
            if len(words[i])+1+rowLen <= maxWidth:
                row.append(words[i])
                rowLen += len(words[i])+1
            else:
                ret.append(process_row(row, rowLen))
                row = [words[i]]
                rowLen = len(words[i])
        if row:
            ret.append(process_row(row, rowLen, isLast=True))
        return ret

words = ["This", "is", "an", "example", "of", "text", "justification."]
for r in Solution().fullJustify(words, 16):
    print r
