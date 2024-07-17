package main

import (
	"bufio"
	"fmt"
	"os"
	"pan/pan"
	"strconv"
	"strings"
)

func main() {

	printMenu()

	var done bool
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input := scanner.Text()
		switch input {
		case "1":
			checkPan(scanner)
		case "quit", "exit":
			done = true
		}
		if done {
			break
		}

		printMenu()
	}
}

func printMenu() {
	fmt.Print("1 - Check single PAN\n")
	fmt.Print("'quit' to exit\n")
	fmt.Print("Select option: ")
}

func checkPan(scanner *bufio.Scanner) {
	fmt.Printf("Enter PAN: ")
	scanner.Scan()
	input := scanner.Text()

	if !validateInput(input) {
		fmt.Printf("Invalid PAN\n")
		return
	}
	n, err := strconv.ParseInt(input, 10, 64)
	if err != nil {
		fmt.Printf("Input is not a number\n")
		return
	}
	check(n)
}

func validateInput(input string) bool {
	isAlpha := func(c rune) bool { return c < '0' || c > '9' }
	isNumeric := strings.IndexFunc(input, isAlpha) == -1
	return (len(input) >= 14 || len(input) <= 19) && isNumeric
}

func check(n int64) {
	r := pan.Check(n)
	fmt.Println()
	switch r {
	case pan.CheckResultNotPAN:
		fmt.Printf("Not a PAN\n")
	case pan.CheckResultPAN:
		fmt.Printf("Valid PAN but not a prime\n")
	case pan.CheckResultPrimePAN:
		fmt.Printf("Valid PAN and a prime\n")
	}
	fmt.Println()
}
