package main

import "fmt"

var successors map[string]map[string]bool
var result [][]string

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	successors = make(map[string]map[string]bool)
	result = [][]string{}
	flag := bfs(beginWord, endWord, wordList, successors)
	if flag {
		fmt.Printf("%v\n", successors)
		dfs1(beginWord, endWord, successors, []string{endWord})
	}
	fmt.Printf("flag:%v\n", flag)
	for k, v := range successors {
		fmt.Printf("key:%v value:%v\n", k, v)
	}

	return result
}

func bfs(beginWord string, endWord string, wordList []string, successors map[string]map[string]bool) bool {
	var flag bool
	visited := make(map[string]bool)
	visited[beginWord] = true
	q := []string{beginWord}
	// wordlist to map
	wordMap := make(map[string]bool)
	for i := 0; i < len(wordList); i++ {
		wordMap[wordList[i]] = true
	}
	for len(q) > 0 {
		temp := []string{}
		nextToVisit := make(map[string]bool)
		for i := 0; i < len(q); i++ {
			fmt.Printf("%v\n", q[i])
			for j := 0; j < len(q[i]); j++ {
				s := "abcdefghijklmnopqrstuvwxyz"
				for k := 0; k < len(s); k++ {
					word := q[i][:j] + string([]byte{s[k]}) + q[i][j+1:]
					if wordMap[word] {
						if !visited[word] {
							if word == endWord {
								flag = true
							}
							if !nextToVisit[word] {
								nextToVisit[word] = true
								temp = append(temp, word)
							}
							if successors[q[i]] == nil {
								successors[q[i]] = make(map[string]bool)
							}
							successors[q[i]][word] = true
						}
					}
				}
			}
		}
		// 找到结果
		if flag {
			break
		}
		for k := range nextToVisit {
			visited[k] = true
		}
		q = temp[:]
	}
	return flag
}

func dfs(beginWord string, endWord string, successors map[string]map[string]bool, path []string) {
	if beginWord == endWord {
		p := make([]string, len(path))
		copy(p, path)
		result = append(result, p)
		return
	}
	for word := range successors[beginWord] {
		dfs(word, endWord, successors, append(path, word))
	}
}

func dfs1(beginWord string, endWord string, successors map[string]map[string]bool, path []string) {
	if beginWord == endWord {
		p := make([]string, len(path))
		copy(p, path)
		result = append(result, p)
		return
	}
	for k, v := range successors {
		if v[endWord] {
			dfs1(beginWord, k, successors, append([]string{k}, path...))
		}
	}
}

func main() {
	beginWord := "aaaaa"
	endWord := "uuuuu"
	wordList := []string{
		"aaaaa", "waaaa", "wbaaa", "xaaaa", "xbaaa", "bbaaa", "bbwaa", "bbwba", "bbxaa", "bbxba", "bbbba", "wbbba", "wbbbb", "xbbba", "xbbbb", "cbbbb", "cwbbb", "cwcbb", "cxbbb", "cxcbb", "cccbb", "cccwb", "cccwc", "cccxb", "cccxc", "ccccc", "wcccc", "wdccc", "xcccc", "xdccc", "ddccc", "ddwcc", "ddwdc", "ddxcc", "ddxdc", "ddddc", "wdddc", "wdddd", "xdddc", "xdddd", "edddd", "ewddd", "ewedd", "exddd", "exedd", "eeedd", "eeewd", "eeewe", "eeexd", "eeexe", "eeeee", "weeee", "wfeee", "xeeee", "xfeee", "ffeee", "ffwee", "ffwfe", "ffxee", "ffxfe", "ffffe", "wfffe", "wffff", "xfffe", "xffff", "gffff", "gwfff", "gwgff", "gxfff", "gxgff", "gggff", "gggwf", "gggwg", "gggxf", "gggxg", "ggggg", "wgggg", "whggg", "xgggg", "xhggg", "hhggg", "hhwgg", "hhwhg", "hhxgg", "hhxhg", "hhhhg", "whhhg", "whhhh", "xhhhg", "xhhhh", "ihhhh", "iwhhh", "iwihh", "ixhhh", "ixihh", "iiihh", "iiiwh", "iiiwi", "iiixh", "iiixi", "iiiii", "wiiii", "wjiii", "xiiii", "xjiii", "jjiii", "jjwii", "jjwji", "jjxii", "jjxji", "jjjji", "wjjji", "wjjjj", "xjjji", "xjjjj", "kjjjj", "kwjjj", "kwkjj", "kxjjj", "kxkjj", "kkkjj", "kkkwj", "kkkwk", "kkkxj", "kkkxk", "kkkkk", "wkkkk", "wlkkk", "xkkkk", "xlkkk", "llkkk", "llwkk", "llwlk", "llxkk", "llxlk", "llllk", "wlllk", "wllll", "xlllk", "xllll", "mllll", "mwlll", "mwmll", "mxlll", "mxmll", "mmmll", "mmmwl", "mmmwm", "mmmxl", "mmmxm", "mmmmm", "wmmmm", "wnmmm", "xmmmm", "xnmmm", "nnmmm", "nnwmm", "nnwnm", "nnxmm", "nnxnm", "nnnnm", "wnnnm", "wnnnn", "xnnnm", "xnnnn", "onnnn", "ownnn", "owonn", "oxnnn", "oxonn", "ooonn", "ooown", "ooowo", "oooxn", "oooxo", "ooooo", "woooo", "wpooo", "xoooo", "xpooo", "ppooo", "ppwoo", "ppwpo", "ppxoo", "ppxpo", "ppppo", "wpppo", "wpppp", "xpppo", "xpppp", "qpppp", "qwppp", "qwqpp", "qxppp", "qxqpp", "qqqpp", "qqqwp", "qqqwq", "qqqxp", "qqqxq", "qqqqq", "wqqqq", "wrqqq", "xqqqq", "xrqqq", "rrqqq", "rrwqq", "rrwrq", "rrxqq", "rrxrq", "rrrrq", "wrrrq", "wrrrr", "xrrrq", "xrrrr", "srrrr", "swrrr", "swsrr", "sxrrr", "sxsrr", "sssrr", "ssswr", "sssws", "sssxr", "sssxs", "sssss", "wssss", "wtsss", "xssss", "xtsss", "ttsss", "ttwss", "ttwts", "ttxss", "ttxts", "tttts", "wttts", "wtttt", "xttts", "xtttt", "utttt", "uwttt", "uwutt", "uxttt", "uxutt", "uuutt", "uuuwt", "uuuwu", "uuuxt", "uuuxu", "uuuuu", "zzzzz", "zzzzy", "zzzyy", "zzyyy", "zzyyx", "zzyxx", "zzxxx", "zzxxw", "zzxww", "zzwww", "zzwwv", "zzwvv", "zzvvv", "zzvvu", "zzvuu", "zzuuu", "zzuut", "zzutt", "zzttt", "zztts", "zztss", "zzsss", "zzssr", "zzsrr", "zzrrr", "zzrrq", "zzrqq", "zzqqq", "zzqqp", "zzqpp", "zzppp", "zzppo", "zzpoo", "zzooo", "zzoon", "zzonn", "zznnn", "zznnm", "zznmm", "zzmmm", "zzmml", "zzmll", "zzlll", "zzllk", "zzlkk", "zzkkk", "zzkkj", "zzkjj", "zzjjj", "zzjji", "zzjii", "zziii", "zziih", "zzihh", "zzhhh", "zzhhg", "zzhgg", "zzggg", "zzggf", "zzgff", "zzfff", "zzffe", "zzfee", "zzeee", "zzeed", "zzedd", "zzddd", "zzddc", "zzdcc", "zzccc", "zzccz", "azccz", "aaccz", "aaacz", "aaaaz", "uuuzu", "uuzzu", "uzzzu", "zzzzu"}
	result := findLadders(beginWord, endWord, wordList)
	for i := 0; i < len(result); i++ {
		fmt.Printf("i:%v %v\n", i, result[i])
	}
}
