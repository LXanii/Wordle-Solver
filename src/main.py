dictionary = [] # used in load dict
temp_letters = [] #variable to store our list w

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
    matching = []
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

    print("Search Term", look_for, "\n" + str(dictionary))
    
load_dict()

print('Put greys into input statment as periods. [Ex. Steak, .t.ak]')
print("Set letter formation to 'found' if word was found")
while True:
    green_letters = str(input('Letter Formation:\n')).lower()
    if green_letters != "found":
        for i in green_letters:
            temp_letters.append(i)
        look_for_word(temp_letters[0], temp_letters[1], temp_letters[2], temp_letters[3], temp_letters[4])
        temp_letters.clear()
    else:
        play_again = str(input("Find Another Word? [Y/N]: ")).lower()
        if play_again == "y":
            dictionary.clear()
            load_dict()
            continue
        else:
            break
