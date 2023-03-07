import os, wget

dictionary = [] # used in load dict
temp_letters = [] #variable to store our list w
matching = []
confirmed_letters = [] # letters confirmed green

DIRECTORY = os.getcwd() + "\\"
DOWNLOAD_DICT = "https://sabercathost.com/mFdW/dictionary.txt"

def check_dict(): # made by joe
    if os.path.exists(DIRECTORY + "dictionary.txt") == False: # checks if theres no dict txt file
        print("Downloading Dictionary...") 
        try:
            wget.download(DOWNLOAD_DICT, "dictionary.txt") # downloads it from the link
            os.system('cls') # clears the command prompt to empty
            print("Finished Downloading Dictionary.")
        except:
            print("\nError Downloading File")
    else:
        print("Found Dictionary File.")

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

def look_for_yellow(a, b, c, d, e):
    print("does nothing yet cuz of kosta")
    #kosta put ur bitch ass shit here tard

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

check_dict()
load_dict()

print('\nPut greys into input statment as periods. [Ex. Steak, .t.ak]')
while True:
    green_letters = str(input('\nLetter Formation [Green Letters]: \n')).lower()
    for i in green_letters:
        temp_letters.append(i)
        if "." not in i:
            confirmed_letters.append(i)
    look_for_word(temp_letters[0], temp_letters[1], temp_letters[2], temp_letters[3], temp_letters[4])
    temp_letters.clear()
    gay_letters = str(input("\nLetter Formation [Gray Letters]: \n")).lower()
    for i in gay_letters:
        temp_letters.append(i)
    look_for_gay(temp_letters[0], temp_letters[1], temp_letters[2], temp_letters[3], temp_letters[4])
    print("\nPredicted Word|s\n" + str(dictionary))
    temp_letters.clear()
