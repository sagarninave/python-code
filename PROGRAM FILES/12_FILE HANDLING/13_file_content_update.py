def replaceinline(filename,wordtoreplace,replacedword):
    
    fhandle = open(filename,'r')
    content = ""
    data = ""
    for i in fhandle:
        content = i.replace(wordtoreplace,replacedword)
        data = data + content
    fhandle.close()
    
    fhandle = open(filename,'w')
    fhandle.write(data)
    fhandle.close()
    
replaceinline('files/13_file_content_update.txt','sagar','sanket')
print('Your work done')

