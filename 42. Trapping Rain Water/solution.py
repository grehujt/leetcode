class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def calc(curItem, maxH, stack):
            ret = 0
            i, h = curItem
            if stack:
                if h >= maxH:
                    while stack:
                        lastI, lastH = stack.pop()
                        ret -= lastH
                    tmp = min(lastH, h) * (i-lastI)
                    ret += tmp if tmp!=0 else lastH
            return ret

        stack = []
        result, maxH = 0, -1
        for i, h in enumerate(height):
            result += calc((i, h), maxH, stack)
            maxH = max(h, maxH)
            stack.append((i, h))
        if stack:
            result += calc(stack.pop(), h, stack[::-1])
        return result


print Solution().trap([0, 2, 0, 2])
