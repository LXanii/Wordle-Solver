dictionary = []

def load_dict(): # made by joe
    print("Loading Dictionary...")
    dic = open("dictionary.txt", "r+") # sets var dic to open our dictionary text file with reading
    split_dic = dic.read() # reads the opened file
    split_dic = split_dic.split("\n") # splits every new line
    for i in split_dic: # checks for every word
        dictionary.append(i) # adds the word to the dictionary array
    print("Finished loading Dictionary\n" + str(len(dictionary)), "words found.")

load_dict()