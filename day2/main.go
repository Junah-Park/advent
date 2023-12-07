package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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

	index := 1

	cubeMap := make(map[string]int)
	cubeMap["red"] = 0
	cubeMap["blue"] = 0
	cubeMap["green"] = 0
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		// Process each line
		// remove all characters before ":" in the line string
		valid := true
		line = line[strings.Index(line, ":")+2:]

		// split line by ";"
		game := strings.Split(line, ";")

		cubeMap["red"] = 0
		cubeMap["blue"] = 0
		cubeMap["green"] = 0

		// check if game is valid
		for _, round := range game {
			// split round by ","
			round := strings.Split(round, ", ")
			// check if round is valid
			for _, cube := range round {
				fmt.Println("CUBE: ", cube)
				// check if cube is valid
				// trim starting whitespace from cube
				cube = strings.TrimLeft(cube, " ")
				// parse number of cubes
				cubeSplit := strings.Split(cube, " ")
				numCubes := cubeSplit[0]
				color := cubeSplit[1]
				// convert numCubes to int
				numCubesInt, err := strconv.Atoi(numCubes)
				if err != nil {
					fmt.Println("Error converting numCubes to int:", err)
				}
				fmt.Println("number of cubes ", numCubes, " color", color)
				// check if cube is smaller than min
				if numCubesInt > cubeMap[color] {
					// if cubeMap[color] is empty
					cubeMap[color] = max(numCubesInt, cubeMap[color])
				}

			}
		}

		fmt.Println(line)
		fmt.Println(valid)

		power := cubeMap["red"] * cubeMap["blue"] * cubeMap["green"]
		fmt.Println("power: ", power)
		sum += power
		index++
	}
	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading from file:", err)
	}

	// Print output
	fmt.Println("Output Text")
}
