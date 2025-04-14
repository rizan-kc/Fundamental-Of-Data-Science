'''
This program conts the occurence of each word in a file.
'''
with open("File3.txt","r") as f:
    content = f.read()
    content = content.split()
content_dic = dict()
for x in content:
    if x in content_dic:
        content_dic[x] += 1
    else:
        content_dic[x] = 1
print(content_dic)
