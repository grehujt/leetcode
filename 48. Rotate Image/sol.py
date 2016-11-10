class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for i in xrange(n):
            for j in xrange(n-i):
                matrix[i][j], matrix[n-j][n-i] = matrix[n-j][n-i], matrix[i][j]
        i, j = 0, n
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

a = [[1,2],[3,4]]
Solution().rotate(a)
print a
