'''
This program counts the number of lines, words and characters present in a text file.
'''
with open("File1.txt") as f:

    #counts the number of line
    lines = f.readlines()
    print(f"The total number of lines in the file is {len(lines)}.")

    #counts the number of words and characters
    f.seek(0)
    content = f.read()
    words = content.split()
    #words
    print(f"The total number of words in the file is {len(words)}")

    #characters
    char = list(content)
    print(f"The total number of characters in the file is {len(char)}.") 