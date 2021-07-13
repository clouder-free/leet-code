# -*- coding: utf-8 -*-
"""
任务调度器
"""

class Solution:

    def leastInterval(self, tasks: [str], n: int) -> int:
        """任务执行最短时间取决于出现次数最多的任务类别
        (A-1)*(n+1) + count
        """
        if n < 1:
            return len(tasks)
        td = {}
        for task in tasks:
            td[task] = td.get(task, 0) + 1
        # 从大到小排序
        sort_task = sorted(td.items(), key=lambda item: item[1], reverse=True)
        result = (sort_task[0][1]-1) * (n+1)
        for st in sort_task:
            if st[1] == sort_task[0][1]:
                result += 1
        return len(tasks) if result < len(tasks) else result

def main():
    # tasks = ["A", "A", "A", "B", "B", "B"]
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    print(Solution().leastInterval(tasks=tasks, n=n))


if __name__ == '__main__':
    main()
