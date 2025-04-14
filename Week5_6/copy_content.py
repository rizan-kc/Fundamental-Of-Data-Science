'''
This program copies the content of one file to another.
For this, two files are used: File1.txt and File2.txt
File1.txt is used for copying the content.
File2.txt is the file to paste the copied content from File1.txt
'''
x = open("File1.txt","r")
content = x.read()
print("The content inside the File1.txt is:")
print(content)
x.close()
print()

z = open("File2.txt","r")
content_file2 = z.read()
print("The content inside the File2.txt is:")
print(content_file2)
z.close()

# Pasting the content of other file.
y = open("File2.txt","w")
y.write(content)
y.close()

# Reading to verify if the content are copied or not!
z = open("File2.txt","r")
content_copied = z.read()
print("The content inside the File2.txt after pasting is:")
print(content_copied)
z.close()