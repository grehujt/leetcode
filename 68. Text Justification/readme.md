# 68. Text Justification

## Problem
- Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
- You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
- Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
- For the last line of text, it should be left justified and no extra space is inserted between words.

> For example,
> 
> words: ["This", "is", "an", "example", "of", "text", "justification."]
> 
> L: 16.
> 
> Return the formatted lines as:
> 
> [
> 
>    "This    is    an",
>    
>    "example  of text",
>    
>    "justification.  "
>    
> ]

## Solution
```python
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
        ret.append(process_row(row, rowLen, isLast=True))
        return ret
```
