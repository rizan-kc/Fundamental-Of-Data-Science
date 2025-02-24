'''
The program prints the Unicode encoding for your name.
'''
name = 'Rizan'
unicode = [ord(char) for char in name]
print("Unicode encoding for name: ",unicode)