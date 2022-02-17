package main

func merge(intervals [][]int) [][]int {
	// 插入法排序
	for i := 1; i < len(intervals); i++ {
		j, temp := i-1, intervals[i]
		for ; j >= 0; j-- {
			if intervals[j][0] <= temp[0] {
				break
			}
			intervals[j+1] = intervals[j]
		}
		// 最终位置
		intervals[j+1] = temp
	}
	//fmt.Printf("%v\n", intervals)
	for i := 0; i < len(intervals); i++ {
		for j := i + 1; j < len(intervals); {
			if intervals[i][0] <= intervals[j][0] && intervals[j][0] <= intervals[i][1] {
				// 合并区间
				if intervals[i][1] < intervals[j][1] {
					intervals[i][1] = intervals[j][1]
				}
				// 修改intervals
				var temp [][]int
				temp = append(temp, intervals[:j]...)
				temp = append(temp, intervals[j+1:]...)
				intervals = temp
				j = i + 1
			} else {
				j++
			}
		}
	}
	//fmt.Printf("%v\n", intervals)
	return intervals
}

func main() {
	intervals := [][]int{
		//{8, 10}, {2, 6}, {15, 18}, {1, 3},
		{1, 4}, {4, 5},
	}
	merge(intervals)
}
