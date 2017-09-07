import os
import re
import fnmatch
path='C:\\Users\\rishi\\Desktop\\Search_Engine\\folder'
Programs = '''
1.Search based on filename
2.Search based on file title
3.Search based on file creation/modified date
4.Search based on file size
5.Search based on file type(pdf,img,doc,txt)


 counter_contents = 0
    counter_names = 0
    if not os.path.exists(path):
        print 'Path does not exist'
        return False
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            # replace contents
            indata = open(os.path.join(dirpath, filename)).read()
            if search in indata:
                new = indata.replace(search, replace)
                output = open(os.path.join(dirpath, filename), "w")
                output.write(new)
                counter_contents +=1
                
            # replace in filename
            if search in filename:
                os.rename(
                    os.path.join(dirpath, filename),
                    os.path.join(dirpath, filename.replace(search, replace))
                )
                counter_names +=1
            
    print '%s files renamed, %s files contents altered' % (counter_names,counter_contents)
    return True
'''
	

count=[]

print('hello world')
def searchbasedonfilename():
    file=input('Enter the file to be searched')
    for i,j,k in os.walk(path):
        print(i,j,k)

'''
        for f1 in k:
            if fnmatch.fnmatch(f1,file):
				print('file matched')
				break
		dirpath=i
print("{0} file found in path{1} :".format(f1,dirpath))
       

def searchbasedonfiletitle():
    for i,j,k in os.walk(path):
        c1=0,c2=0,c3=0,c4=0
        for f1 in k:
            if f1.endswith(".txt"):
                c1=c1+1
            if f1.endswith(".img"):
                c2=c2+1
            if f1.endswith(".pdf"):
                c3=c3+1
            if f1.endswith(".doc"):
                c4=c4+1
def searchbasedondate():
    for i,j,k in os.walk(path):
        c1=0,c2=0,c3=0,c4=0
        for f1 in k:
            if f1.endswith(".txt"):
                c1=c1+1
            if f1.endswith(".img"):
                c2=c2+1
            if f1.endswith(".pdf"):
                c3=c3+1
            if f1.endswith(".doc"):
                c4=c4+1
def searchbasedonsize():
    for i,j,k in os.walk(path):
        c1=0,c2=0,c3=0,c4=0
        for f1 in k:
            if f1.endswith(".txt"):
                c1=c1+1
            if f1.endswith(".img"):
                c2=c2+1
            if f1.endswith(".pdf"):
                c3=c3+1
            if f1.endswith(".doc"):
                c4=c4+1
				
def searchbasedontypeoffile():
    for i,j,k in os.walk(path):
        c1=0,c2=0,c3=0,c4=0
        for f1 in k:
            if f1.endswith(".txt"):
                c1=c1+1
            if f1.endswith(".img"):
                c2=c2+1
            if f1.endswith(".pdf"):
                c3=c3+1
            if f1.endswith(".doc"):
                c4=c4+1
       
        count.append(c1)
        count.append(c2)
        count.append(c3)
        count.append(c4)
        print("Total number text files in path {0} is :{1}".format(i,count[0]))
        print("Total number image files in path {0} is :{1}".format(i,count[1]))
        print("Total number pdf files in path {0} is :{1}".format(i,count[2]))
        print("Total number word documnet files in path {0} is :{1}".format(i,count[3]))
            








options = {1: searchbasedonfilename, 2:searchbasedonfiletitle , 3: searchbasedondate, 4:searchbasedonsize, 5:searchbasedontypeoffile} 
'''
options = {1: searchbasedonfilename}    

print(Programs)

key = 'Y'

# ch=int(input('Enter the program Number :'))
while (key == 'Y') or (key == 'y') or (key == 'yes') or key == 'Yes' or key == 'YES':
    print("#####################################################\n")
    ch = int(input('Enter the Search criteria :'))
    print("\n")
    print("#####################################################\n")
    options[ch]()
    key = input('Do you want to continue : Press Y/Yes/y/yes or N/No/no/n : ')

if key == 'N' or key == 'n' or key == 'no' or key == 'NO' or key == 'No':
    os.system('exit')
	
