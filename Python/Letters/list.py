import string
from letters import Letters

class bcolors:   
    GREEN = '\033[92m'  
    RED = '\033[91m'
    ENDC = '\033[0m'

def getVowels(alphabet):
    
    for e in alphabet:
        if e == "a" or e == "i" or e == "o" or e == "u":
            vowels.put(e)
            print(bcolors.GREEN + f"{e} is a Vowel" + bcolors.ENDC)
        else:
            nonVowels.put(e)
            print(bcolors.RED + f"{e} is a consonant" + bcolors.ENDC)

vowels = Letters()
nonVowels = Letters()

alphabet = list(string.ascii_lowercase)
getVowels(alphabet)

print(vowels.getValues())
print(nonVowels.getValues())
# words = readFile("./Python/declaration.txt")
# for x in words.split():
#     print(x)

# def readFile(filePath):
 
#     arrayWords = []

#     with open(filePath) as file:

#         for line in file.readlines():
#             arrayWords = arrayWords + line.split()

#     print(arrayWords)
#     return arrayWords
