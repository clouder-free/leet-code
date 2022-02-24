package main

import (
	"fmt"
	"strings"
)

func simplifyPath(path string) string {
	if path == "/" {
		return path
	}
	var result []string
	path = strings.Trim(path, "/")
	paths := strings.Split(path, "/")
	//fmt.Println("paths:", paths)
	for i := range paths {
		//fmt.Println("i:", i, "p:", paths[i])
		// 当前目录
		if paths[i] == "." || paths[i] == "" {
			continue
			// 父目录
		} else if paths[i] == ".." {
			if result != nil && len(result) > 0 {
				result = result[:len(result)-1]
			}
		} else {
			result = append(result, paths[i])
		}
	}
	//fmt.Println("result:", len(result))
	if len(result) != 0 {
		return "/" + strings.Join(result, "/")
	}
	return "/"
}

func main() {
	path := "/a/./b/../../c/"
	result := simplifyPath(path)
	fmt.Println("result:", result)
}
