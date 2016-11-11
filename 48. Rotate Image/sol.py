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
        matrix.reverse()

a = [[1,2],[3,4]]
Solution().rotate(a)
print a
