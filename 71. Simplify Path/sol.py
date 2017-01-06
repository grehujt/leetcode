class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = []
        for item in path.split('/'):
            if item and item != '.':
                if ret and item == '..':
                    ret.pop()
                elif item != '..':
                    ret.append(item)
        return '/%s' % '/'.join(ret)


print Solution().simplifyPath('/./')
