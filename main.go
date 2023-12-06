package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Open the input file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Read the file
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		// Process each line
		fmt.Println(line)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading from file:", err)
	}

	// Print output
	fmt.Println("Output Text")
}
