def replacestring(filename,oldword,newword):
    fhandle = open(filename,'r')
    content = fhandle.read()
    if oldword in content:
        content = content.replace(oldword,newword)
    elif newword in content:
        content = content.replace(newword,oldword)
    fhandle.close()
    fhandle = open(filename,'w')
    fhandle.write(content)
    fhandle.close()

replacestring('14_file_content_update_with _if_else.txt','Sagar','Snaket')

print('Data Changed')
fhandle = open('files/14_file_content_update_with _if_else.txt','r')
print(fhandle.read())

