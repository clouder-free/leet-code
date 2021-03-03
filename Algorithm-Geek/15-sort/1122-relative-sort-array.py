# -*- coding: utf-8 -*-

class Solution(object):

    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        if not arr1 or not arr2:
            return []
        # arr2中出现的数据排序
        i = -1
        for arr in arr2:
            j = i + 1
            while j < len(arr1):
                if arr == arr1[j]:
                    i += 1
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                j += 1
        if i+1 < len(arr1):
            arr1[i+1:].sort()
            """
            # arr2中未出现的数据排序 冒泡排序
            for m in range(i+1, len(arr1)):
                # 当前最小值
                index = m
                for n in range(m+1, len(arr1)):
                    if arr1[index] >= arr1[n]:
                        index = n
                arr1[m], arr1[index] = arr1[index], arr1[m]
            """
        right = arr1[i+1:]
        right.sort()
        return arr1[:i+1] + right


def main():
    # arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19, 5, 10, 5, 7, 7]
    # arr2 = [2, 1, 4, 3, 9, 6]
    arr1 = [33,22,48,4,39,36,41,47,15,45]
    arr2 = [22,33,48,4]
    result = Solution().relativeSortArray(arr1=arr1, arr2=arr2)
    print(result)

if __name__ == '__main__':
    main()
