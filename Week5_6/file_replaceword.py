'''
This program replace a specific word with another word in a file with the help of file handling.
'''
def check_word(x , file):
    '''
    Checks if a given word exists in the file or not.

    Parameter:
    x: The word(str) to check
    file: The filename including extension

    Returns bool: True if x is in file otherwise bool: False.
    '''
    with open(file,'r') as f1:
        c1 = f1.read()
        return True if x in c1 else False

def replace_word(x, r ,file):
    '''
    Replaces all the occurences of a word in the given file with new word.

    Argument:
    x: Word to be replaced
    r: Replacement Word
    file: Filename where the replacement will happen

    '''
    with open(file,'r') as f2:
        content = f2.read()
    
    content = content.replace(x,r)
    with open(file,'w') as f2:
        f2.write(content)

while True:
    x = input("Enter the word you want to replace: ")
    f = input("Enter the file name you want to check, along with extension: ")
    check = check_word(x,f)
    if check == False:
        continue
    else:
        r = input("Enter the new word: ")
        replace_word(x, r, f)
        break
