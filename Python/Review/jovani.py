import string
from letter import letter
 
class bocolor:
   GREEN = '\033[92M'
   RED = '\033[91M'
   ENDC = '\033[0M'
  
def getVowels(alphabet):
 
   for e in alphabet:
       if e == "a" or e == "i" or e == "o" or e == "u"
           vowels.put(e)
       else:
           nonVowels.put(e)
 
def readFiles(filePath):
 
   arrayWords = []
 
   with open(filesPath) as file:
 
       for line in file.readlines():
           arrayWords = arrayWords + line.split()
          
vowels = letter()
nonVowels = letter()
 
alphabet = list(string.ascii_lowercase)
getVowels(alphabet)
 
print(vowels.getValues())
print(nonVowels.getValues())

