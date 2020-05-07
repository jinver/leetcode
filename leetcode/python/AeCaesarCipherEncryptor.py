# Given a non-empty string of lowercase letters and a non-negative integer representing
# a key, write a function that returns a new string obtained by shifting every letter
# in the input string by k positions in the alphabet, where k is the key.
# Note that letters should wrap around the alphabet; in other words, the letter z shifted
# by one returns the letter a.


def caesarCipherEncryptor(string, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
	lettersArr = []
	lettersDict = {}
	
	for index, char in enumerate(letters):
		lettersDict[char] = index
		lettersArr.append(char)
	result = ""
	for char in string:
		charIndex = lettersDict[char]
		newIndex = charIndex + key
		newChar = lettersArr[newIndex % 26]
		result += newChar
	return result
