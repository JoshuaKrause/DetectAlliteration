'''
Detect Alliteration
A Python exercise from reddit.com/r/dailyprogrammer/

Detects alliteration in a supplied string.
'''


PATH = 'C:/Users/VFX_07_2/Desktop/alliteration/'

def detect_alliteration(input):
    # Output starts as an empty string.
    output = ''

    # Split the input into lines and extract the total line count.
    lines = input.splitlines()
    line_count = int(lines.pop(0))

    # Iterate through each line.
    for i in range(line_count):
        # Strip out the stop words and create an empty list for output.
        word_list = clean_word_list(lines[i])
        out_list = []        

        # Iterate through each word. 
        for w in range(len(word_list)):
            # If the word is the first in the line and its first letter matches the first letter of the next word, add it to the output_list.
            if w == 0:
               if word_list[w][0].lower() == word_list[w + 1][0].lower():
                    if word_list[w] not in out_list: 
                        out_list.append(word_list[w])
            # If the word is the last in the line and its first letter matches the previous word, add it to the output list.
            elif w == len(word_list) - 1:
                if word_list[w][0].lower() == word_list[w - 1][0].lower():
                    if word_list[w] not in out_list: 
                        out_list.append(word_list[w])
            # If the word's first letter matches either the previous or next word, add it to the output list.
            elif word_list[w][0].lower() == word_list[w-1][0].lower() or word_list[w][0].lower() == word_list[w+1][0].lower(): 
                    if word_list[w] not in out_list: 
                        out_list.append(word_list[w])
                      
        # Join the list and add it to the output string.
        output += ' '.join(out_list) + '\n'

    return output         

                
# Helper function to remove stop words from lines and puncuation from words.
def clean_word_list(input):
    f = open(PATH + 'stopWords.txt', 'r')
    stop_words = f.read().splitlines()
    
    output_list = []

    for word in input.split():
        if word.rstrip('\'\"-,.:;!?') not in stop_words:
            output_list.append(word.rstrip('\'\"-,.:;!?'))

    return output_list


a = "3\nPeter Piper Picked a Peck of Pickled Peppers\nBugs Bunny likes to dance the slow and simple shuffle\nYou'll never put a better bit of butter on your knife"
b = (   '8\n'
        'The daily diary of the American dream\n'
        'For the sky and the sea, and the sea and the sky\n'
        'Three grey geese in a green field grazing, Grey were the geese and green was the grazing.\n'
        'But a better butter makes a batter better.\n'
        '"His soul swooned slowly as he heard the snow falling faintly through the universe and faintly falling, like the descent of their last end, upon all the living and the dead."\n'
        'Whisper words of wisdom, let it be.\n'
        'They paved paradise and put up a parking lot.\n'
        'So what we gonna have, dessert or disaster?' )
#print b

print detect_alliteration(b)