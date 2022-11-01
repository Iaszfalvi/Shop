
# This is where you put all of your functions, at the top.
def readFile(filePath):
 
    arrayWords = []

    with open(filePath) as file:

        for line in file.readlines():
            arrayWords = arrayWords + line.split()

    print(arrayWords)
    return arrayWords


def countWords(word, listWords):

    count = 0
        
    for every_word in listWords:
        if every_word.replace(".", "").replace(",", "") == word:
            count += 1

    return count

# This is where you put your actual program
words_hemingway = readFile("Python/hemingway.txt")
with_count = countWords("with", words_hemingway)

print(time_count)