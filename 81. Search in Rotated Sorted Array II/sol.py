class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def _find_max(beg, end):
            if beg == end: return beg
            mid = (beg+end) >> 1
            if beg+1 == end:
                return beg if nums[beg] > nums[end] else None
            elif nums[beg] < nums[mid] > nums[end]:
                return _find_max(beg+1, end)
            else:
                ret = _find_max(beg, mid)
                return ret if ret is not None else _find_max(mid, end)
                # wrong statement, _find_max can return zero
                # return _find_max(beg, mid) or _find_max(mid, end)

        def _binary_search(beg, end):
            while beg <= end:
                mid = (beg+end) >> 1
                if target == nums[mid]:
                    return True
                elif target > nums[mid]:
                    beg = mid+1
                else:
                    end = mid-1
            return False

        if nums:
            an = _find_max(0, len(nums)-1)
            if an is not None:
                if target == nums[an]: return True
                if target > nums[an]: return False
                return _binary_search(0, an) or _binary_search(an+1, len(nums)-1)
            else:
                return _binary_search(0, len(nums)-1)
        return False


print Solution().search([3,1,1], 3)
