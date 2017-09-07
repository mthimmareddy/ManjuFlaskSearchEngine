import os
import re
import fnmatch
from datetime import datetime
path='C:\\Users\\rishi\\Desktop\\Search_Engine'
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)


Programs = ''' 
    First argument:
        
    1.Search based on filename
    2.Search based on file content
    3.Search based on file creation/modified date
    4.Search based on file size
    5.Search based on file type(pdf,img,doc,txt)
    
    c= 
    1.whole filename
    2.begining of filename
    3.end of filename
    4.anywhere in filename
    
   
    
    python search.py ('Enter the Search criteria :') ('Enter the pattern based on Search criteria :')
    Example:    python search.py 1 "filename","c"
                python search.py 2 "keyword in file" "filename"
                python search.py 3 "creation/modification" "date of creation"
                python search.py 4 "size of file"
                python search.py 5 "type of file(doc/pdf/img/)"
  
    '''
    




@app.route('/')
def home():
    return render_template('Search1.html')
	
	

	
@app.route("/" , methods=['GET','POST'])
def my_form_post():
    option = request.form.get('comp_select')
    text = request.form['text']
    
    if int(option)==1:
        redirect(url_for('results'))
        return result
    elif int(option)==2:
        result=searchbasedonfilecontent(text)
        return result
    elif int(option)==3:
        result=searchbasedondate(text)
        return result
    elif int(option)==4:
        result=searchbasedonsize(text)
        return result
    elif int(option)==5:
	    redirect(url_for('searchbasedontypeoffile'),pattern=text)
        
        
          
@app.route('/results',methods=['GET', 'POST'])
def results():
    return render_template('Results.html')




def searchbasedonfilename(pattern):
    flag=0
    match_files=[]
    result=''
   
    for root,dirs,files in os.walk(path):
        for name in files:
            
            if fnmatch.fnmatch(name,pattern):
                flag=1
                match_files.append(os.path.join(root, name))
            elif name.startswith(pattern):
                flag=1
                match_files.append(os.path.join(root, name))
                
            elif name.endswith(pattern):
                flag=1
                match_files.append(os.path.join(root, name))
                
            elif pattern in name:
                flag=1
                match_files.append(os.path.join(root, name))
                

    if(flag):
        for item in match_files:
            result+=' '+(item)
        return result
    else:
        return 'File not found'
       
def pdfreadder(file):
    import PyPDF2
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    print (page_content.encode('utf-8'))
    return page_content


       

def searchbasedonfilecontent(pattern,filename):
    #file=input('Enter the file in which pattern to be searched') 
    count=searchbasedonfilename(filename)
   
    
    flag1=0
    print(count)
    if count:
        for file in count:
          if 'pdf' in file:
            content=pdfreadder(file)
            content=content.split(";")
            with open('tem.txt','w') as f1:
             for ele in content:
              f1.write(ele)
              f1.write('\n')
            with open('tem.txt', 'r') as f2:
             for line in f2.readlines():
              #rint(line)
              match=re.search(pattern,line)
              #rint(match)
              if(match):
                 flag1=1
                 print(line)
                 with open("temp.txt",'w') as f:
                     f.write(line)
                     
          else:
           for file in count:
               with open(file, 'r') as f2:
                   for line in f2.readlines():
                       match=re.search(pattern,line)
                       if(match):
                           flag1=1
                           print (line)
                           with open("temp.txt",'w') as f:
                               f.write(line)
               
          if(flag1):
             print('Pattern found')
             return "temp.txt"
          else:
             print('Pattern Not found')
             return None
          
                 
    else: 
        print('File not found')
        return None

def searchbasedondate(pattern):
    count=[]
    #path='C:\\Users\\rishi\\Desktop\\Search_Engine'
    for root,dirs,files in os.walk(path):
        for directory in dirs:
            ctime=datetime.fromtimestamp(os.path.getctime(directory)).strftime('%d-%m-%Y')
            if (ctime==pattern):
                print("Folder is created on date {0}".format(directory))
           
        for name in files:
            path1=os.path.join(root,name)
            #ctime=datetime.fromtimestamp(os.path.getctime(path1)).strftime('%d-%m-%Y')
            #print(name,ctime)
            if (ctime==pattern):
                print("Name of file created on date {0}".format(path1))
                count.append(path1)
    return count
           
             
                
def searchbasedonsize(pattern):
    count=[]
    
    for root,dirs,files in os.walk(path):
        for directory in dirs:
            size=os.path.getsize(directory)
            if (size==pattern):
                print("Folder is created on date {0}".format(directory))
           
        for name in files:
            path1=os.path.join(root,name)
            size=os.path.getsize(path1)
            if (size==pattern):
                print("Folder is created on date {0}".format(path1))
                count.append(path1)
    return count


@app.route('/searchbasedontypeoffile/<pattern>',methods=['GET', 'POST'])			
def searchbasedontypeoffile(pattern):
    count_files=[]
    
    for root,dirs,files in os.walk(path):
        c1=0
        c2=0
        c3=0
        c4=0
        count=[]
        
        for f1 in files:
            path1=os.path.join(root,f1)
            if f1.endswith(".txt") and (pattern in f1):
                c1=c1+1
                count_files.append(path1)
            elif (f1.endswith(".img") or f1.endswith(".png") or f1.endswith(".jpeg") or f1.endswith(".mp3"))and (pattern in f1):
                c2=c2+1
                count_files.append(path1)
            elif f1.endswith(".pdf") and (pattern in f1):
                c3=c3+1
                count_files.append(path1)
            elif f1.endswith(".doc") and (pattern in f1):
                c4=c4+1
                count_files.append(path1)
       
        count.append(c1)
        count.append(c2)
        count.append(c3)
        count.append(c4)
		
    with open("templates/Results.html",'w') as f:
        for item in count_files:
            f.write(item)
            f.write('\n')
            
       
    

if __name__ == '__main__':
    app.run()




 

