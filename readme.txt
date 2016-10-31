Detect Alliteration
A Python exercise from reddit.com/r/dailyprogrammer/

Detects alliteration in a supplied string. Ignores common words found in the accompanying 'stopWords.txt'.

Flows as follows:
	Breaks a string into a list of lines.
	Strips each line of puncuation and stop words. 
	Iterates through the remaining words.
	If the first letter of a word matches the previous or next word, count and save it.
	Return the final count and collection of alliterative words.