class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def _search(l1, l2, k):
            if len(l1) == 0:
                return l2[k]
            if len(l2) == 0:
                return l1[k]
            mid1 = len(l1) >> 1
            mid2 = len(l2) >> 1
            if mid1 + mid2 < k:
                if l1[mid1] > l2[mid2]:
                    return _search(l1, l2[mid2+1:], k - mid2 - 1)
                else:
                    return _search(l1[mid1+1:], l2, k - mid1 - 1)
            else:
                if l1[mid1] > l2[mid2]:
                    return _search(l1[:mid1], l2, k)
                else:
                    return _search(l1, l2[:mid2], k)
        totalLen = len(nums1) + len(nums2)
        if totalLen % 2 == 0:
            return (_search(nums1, nums2, totalLen >> 1) + _search(nums1, nums2, (totalLen >> 1) - 1)) / 2.0
        else:
            return _search(nums1, nums2, totalLen >> 1)
