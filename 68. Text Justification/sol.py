class Solution(object):
    def fullJustify(self, words, maxWidth):
        ret, row, rowLen = [], [], 0
        for w in words:
            if rowLen + len(row) + len(w) > maxWidth:
                for i in range(maxWidth-rowLen):
                    row[i % (len(row)-1 or 1)] += ' '
                ret.append(''.join(row))
                row, rowLen = [w], len(w)
            else:
                row.append(w)
                rowLen += len(w)
        ret.append(' '.join(row).ljust(maxWidth))
        return ret


words = ["This", "is", "an", "example", "of", "text", "justification."]
for r in Solution().fullJustify(words, 16):
    print r
