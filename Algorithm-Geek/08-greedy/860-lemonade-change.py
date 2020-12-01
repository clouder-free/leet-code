# -*- coding: utf-8 -*-

class Solution(object):

    def lemonadeChange(self, bills: [int]) -> bool:
        bill_map = {5: 0, 10: 0, 20: 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                bill_map[5] += 1
            elif bills[i] == 10:
                if bill_map[5] <= 0:
                    return False
                bill_map[5] -= 1
                bill_map[10] += 1
            else:
                if bill_map[5] >= 1 and bill_map[10] >= 1:
                    bill_map[5] -= 1
                    bill_map[10] -= 1
                    bill_map[20] += 1
                elif bill_map[5] >= 3:
                    bill_map[5] -= 3
                    bill_map[20] += 1
                else:
                    return False

        return True

def main():
    bills = [5, 5, 10, 10, 20]
    solution = Solution()
    result = solution.lemonadeChange(bills=bills)
    print(result)

if __name__ == '__main__':
    main()

