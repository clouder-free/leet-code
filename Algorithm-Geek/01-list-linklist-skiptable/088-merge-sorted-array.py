# -*- coding: utf-8 -*-

class Solution(object):

    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                k = m
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                j += 1
                m += 1
            i += 1

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        print(nums2)
        print(nums1)

    def merge2(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        print(nums1)


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution = Solution()
    solution.merge2(nums1=nums1, m=m, nums2=nums2, n=n)

if __name__ == '__main__':
    main()

