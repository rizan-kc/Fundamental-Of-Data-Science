'''
This program prompts the user to input two words and displays the letter which are common in both.
'''
def word_intersection(w1,w2):
    '''
    Compares two words and returns the letter which are common to both words.

    Parameters:
    w1: A string(str), the first word.
    w2: A string(str), the second word.

    Returns the string(str) which contains common letters between two words and separated by spaces.
    '''
    lst1 = list(w1)
    lst2 = list(w2)
    set1 = set(lst1)
    set2 = set(lst2)
    x = set1.intersection(set2)
    if x == set():
        return "nothing"
    else:
        x = " ".join(x)
        return x
w1 = input("Enter the first word: ")
w2 = input("Enter the second word: ")
print(f"The two words have these letters in common: {word_intersection(w1,w2)}.")