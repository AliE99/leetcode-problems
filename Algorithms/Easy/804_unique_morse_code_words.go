package main

import "fmt"

func uniqueMorseRepresentations(words []string) int {
	var set = make(map[string]bool)
	for _, word := range words {
		set[generateMorse(word)] = true
	}
	return len(set)
}

func generateMorse(word string) string {
	morseCode := map[string]string{
		"a": ".-",
		"b": "-...",
		"c": "-.-.",
		"d": "-..",
		"e": ".",
		"f": "..-.",
		"g": "--.",
		"h": "....",
		"i": "..",
		"j": ".---",
		"k": "-.-",
		"l": ".-..",
		"m": "--",
		"n": "-.",
		"o": "---",
		"p": ".--.",
		"q": "--.-",
		"r": ".-.",
		"s": "...",
		"t": "-",
		"u": "..-",
		"v": "...-",
		"w": ".--",
		"x": "-..-",
		"y": "-.--",
		"z": "--..",
	}
	morsedWord := ""
	for _, char := range word {
		morsedWord += morseCode[string(char)]
	}
	return morsedWord
}

func main() {
	words := []string{"gin", "zen", "gig", "msg"}
	fmt.Println(uniqueMorseRepresentations(words))
}
