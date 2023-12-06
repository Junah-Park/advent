package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

type Trie struct {
	root *TrieNode
}

type TrieNode struct {
	completed bool
	value     int
	children  map[rune]*TrieNode
}

func (t *Trie) insert(s string, val int) {
	node := t.root
	for _, r := range s {
		value, exist := node.children[r]
		if !exist {
			new_child := new(TrieNode)
			new_child.children = make(map[rune]*TrieNode)
			node.children[r] = new_child
			node = new_child
		} else {
			node = value
		}
	}
	node.completed = true
	node.value = val
}

func (t *Trie) search(s string) (int, bool) {
	node := t.root
	for _, r := range s {
		next_node, exist := node.children[r]
		if !exist {
			return 0, false
		}
		if next_node.completed {
			return next_node.value, true
		}
		node = next_node
	}
	return 0, false
}

func main() {
	trie := new(Trie)
	trie.root = new(TrieNode)
	trie.root.children = make(map[rune]*TrieNode)

	numbers := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	for i, num := range numbers {
		trie.insert(num, i+1)
	}

	// Open the input file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Read the file
	scanner := bufio.NewScanner(file)
	// running count
	count := 0

	for scanner.Scan() {

		line := scanner.Text()
		// Process each line
		fmt.Println(line)
		// left and right pointer for sliding window
		left := 0
		right := len(line) - 1

		leftValue := 0
		rightValue := 0

		// iterate left pointer until a digit is found
		for left < len(line) {
			value, exist := trie.search(line[left:])
			if exist {
				fmt.Printf("leftValue = %d\n", value)
				leftValue = 10 * value
				// end the loop
				break
			}
			if unicode.IsDigit(rune(line[left])) {
				leftValue = int(rune(line[left])-'0') * 10
				fmt.Printf("leftValue = %d\n", leftValue)
				break
			}
			left++
		}
		// iterate right pointer until a digit is found
		for right >= 0 {
			value, exist := trie.search(line[right:])
			if exist {
				fmt.Printf("rightValue = %d\n", value)
				rightValue = value
				break
			}
			if unicode.IsDigit(rune(line[right])) {
				rightValue = int(rune(line[right]) - '0')
				fmt.Printf("rightValue = %d\n", rightValue)
				break
			}
			right--
		}
		// convert the digits to ints and add to count
		count += leftValue + rightValue
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading from file:", err)
	}

	// Print output
	fmt.Println(count)
}
