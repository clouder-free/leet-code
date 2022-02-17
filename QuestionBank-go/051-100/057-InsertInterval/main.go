package main

import "fmt"

func insert(intervals [][]int, newInterval []int) [][]int {
	if len(newInterval) == 0 {
		return intervals
	}
	if len(intervals) == 0 {
		return [][]int{newInterval}
	}
	var result [][]int
	for i := 0; i < len(intervals); i++ {
		// newInterval位于intervals[i]左侧
		if newInterval[1] < intervals[i][0] {
			// append 退出
			result = append(append(result, newInterval), intervals[i:]...)
			return result
		}
		// newInterval位于intervals[i]右侧
		if newInterval[0] > intervals[i][1] {
			// append intervals[i]
			result = append(result, intervals[i])
			continue
		}
		// newInterval 与 intervals[i] 有交集 更新newInterval
		if intervals[i][0] <= newInterval[0] {
			newInterval[0] = intervals[i][0]
		}
		if intervals[i][1] >= newInterval[1] {
			newInterval[1] = intervals[i][1]
		}
	}
	// newInterval位于最右侧 或 将intervals中右半部分的区间全部合并
	result = append(result, newInterval)
	return result
}

func main() {
	intervals := [][]int{
		{1, 3}, {6, 9},
	}
	newInterval := []int{2, 5}
	result := insert(intervals, newInterval)
	fmt.Printf("%v\n", result)
}
