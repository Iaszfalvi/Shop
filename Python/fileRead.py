# myfile = open("inputs.txt", "a+")

# userInput = input("Enter something you want to save to the file: ")

# oldInput = myfile.read()

# print(oldInput, userInput)
# myfile.writelines(userInput)

# myfile.close()




    # data = f.read()

    # words = data.split()

    # print(len(words))

    # arr = []

    # for line in f.readlines():
    #     arr.append(line)

    # print(arr)

macbeth = "/home/paul/Programming/Work/Python/macbeth.txt"

# with open(r"") as f:
    
#     count = 0

#     for line in f.readlines():
#         count += len(line.split())

#     print(count)
  

# userInput = input("Enter some input ")


# for element in userInput:

#     print(element)

# array_Words = userInput.split()

# print(array_Words)

# count = 0

# for e in array_Words:
#     count += 1

# print(count)



#File path
myfile = "/home/paul/Programming/Work/Python/file.txt"
declaration = "/home/paul/Programming/Work/Python/declaration.txt"
hemingway = "/home/paul/Programming/Work/Python/hemingway.txt"

# Read a file and return word count
with open(hemingway) as f:

    # print(f.readline().split())
    #This is just comment text that will be ignored
    count = 0
    words = {}


    for line in f.readlines():    
        for word in line.split():
            words[word.lower()] = words.get(word, 0) + 1
        
        count += len(line.split())

    print(count)
    print(words)










