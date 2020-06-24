#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""

class Solution(object):

    # 递归
    def restoreIpAddresses(self, s: str) -> [str]:
        results = []
        def valid(s):
            if not s or len(s) > 3 or (len(s) > 1 and s[0] == "0"):
                return False
            return 0 <= int(s) <= 255
        def restore_ip_addresses(s, k, res):
            if k == 0:
                if not s:
                    results.append(res)
            else:
                for i in range(1, 4):
                    # 判断s[:i]是否合法
                    if len(s) >= i and valid(s[:i]):
                        if k == 4:
                            restore_ip_addresses(s[i:], k-1, res + s[:i])
                        else:
                            restore_ip_addresses(s[i:], k-1, res + "." + s[:i])
        restore_ip_addresses(s, 4, "")
        return results

def main():
    s = "25525511135"
    solution = Solution()
    result = solution.restoreIpAddresses(s=s)
    print(result)

if __name__ == "__main__":
    main()


