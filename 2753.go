package main

import (
	"fmt"
)

func main() {
	var a int
	fmt.Scanln(&a)
	if a%4 == 0 && a%100 != 0 {
		fmt.Print("1")
	} else if a%400 == 0 {
		fmt.Print("1")
	} else {
		fmt.Print("0")
	}
}