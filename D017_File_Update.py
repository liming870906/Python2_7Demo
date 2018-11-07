

oldFile = open('files/Text_Content','r')
newFile = open('files/Text_Content_New','w')

for i in oldFile:
    print(i.strip())
oldFile.seek(0)
oldContent = input('源文件内容>>>>>>:')
newContent = input('替换内容>>>>>>:')

for i in oldFile:
    if oldContent in i:
        i = i.replace(oldContent,newContent)
    newFile.write(i)
newFile.flush()
newFile.close()
oldFile.close()