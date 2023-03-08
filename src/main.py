dictionary = [] # used in load dict
temp_letters = [] #variable to store our list w
matching = []
confirmed_letters = [] # letters confirmed green

def load_dict(): # made by joe | loads the dictionary to a list
    print("Loading Dictionary...")
    dic = open("dictionary.txt", "r+") # sets var dic to open our dictionary text file with reading
    split_dic = dic.read() # reads the opened file
    split_dic = split_dic.split("\n") # splits every new line
    for i in split_dic: # checks for every word
        if len(i) == 5:
            dictionary.append(i.lower()) # adds the word to the dictionary array
    print("Finished loading Dictionary\n" + str(len(dictionary)), "words found.")

def look_for_word(a, b, c, d, e): # made by joe | gets the index values of the letters
    matching.clear()
    look_for = a + b + c + d + e # adds the letters together
    print("This may take a little...")
    print("Checking for", look_for)
    for i in range(1, len(look_for) + 1): # loops for the amount of indexes
        if look_for[i-1] != ".": # checks if the placement if valid
            for p in dictionary:
                if p[i-1] == look_for[i-1]:
                    matching.append(p)
            dictionary.clear()
            for m in matching:
                dictionary.append(m)
            matching.clear()

def look_for_yellow(a, b, c, d, e):#made by kosta
    matching.clear()
    look_for = a + b + c + d + e#combines the letters
    for i in range(1, len(look_for) + 1):#loops indexes
         if look_for[i-1] != ".":#checks placement
                for p in dictionary:
                    if look_for[i-1] in p:#if the yellow letter is in the word it returns the word
                        matching.append(p)
                dictionary.clear()
                for m in matching:
                    dictionary.append(m) 
                matching.clear()                

def look_for_gay(a, b, c, d, e): #made by joe
    matching.clear()
    look_for = a + b + c + d + e # adds the letters together
    for i in range(1, len(look_for) + 1): # loops for the amount of indexes
        if look_for[i-1] != ".": # checks if the placement if valid
            if look_for[i-1] not in confirmed_letters:
                for p in dictionary:
                    if look_for[i-1] not in p:
                        matching.append(p)
                dictionary.clear()
                for m in matching:
                    dictionary.append(m)
                matching.clear()

load_dict()

print('\nPut greys into input statment as periods. [Ex. Steak, .t.ak]')#made by kosta & joe
while True:
    green_letters = str(input('\nLetter Formation [Green Letters]: \n')).lower()
    for i in green_letters:
        temp_letters.append(i)
        if "." not in i:
            confirmed_letters.append(i)
    look_for_word(temp_letters[0], temp_letters[1], temp_letters[2], temp_letters[3], temp_letters[4])
    temp_letters.clear()
    yellow_letters = str(input('\nLetter Formation [Yellow Letters]: \n')).lower()
    for i in yellow_letters:
        temp_letters.append(i)
        if "." not in i:
            confirmed_letters.append(i)
    look_for_yellow(temp_letters[0], temp_letters[1], temp_letters[2], temp_letters[3], temp_letters[4])
    temp_letters.clear()
        
    gay_letters = str(input("\nLetter Formation [Gray Letters]: \n")).lower()
    for i in gay_letters:
        temp_letters.append(i)
    look_for_gay(temp_letters[0], temp_letters[1], temp_letters[2], temp_letters[3], temp_letters[4])
    print("\nPredicted Word|s\n" + str(dictionary))
    temp_letters.clear()
