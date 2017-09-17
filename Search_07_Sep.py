import os
import re
import fnmatch
from datetime import datetime
path='C:/Users/rishi/Desktop/ManjuFlaskSearchEngine'
from flask import Flask, render_template, Response, request, redirect, url_for
import codecs
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
    return render_template('home.html')

	
@app.route("/" , methods=['GET','POST'])
def my_form_post():
    option = request.form.get('comp_select')
    text = request.form['text']
    
    if int(option)==1:
        
        result=searchbasedonfilename(text)
        if(result):
            return  render_template('Results.html')
        else:
            return "No Matches found"
            
    elif int(option)==2:
        list1=text.split(",")
        if(len(list1)<2):
            list1.append(list1[0])
        result=searchbasedonfilecontent(list1[0],list1[1])
        if(result):
            return  render_template('Results.html')
        else:
            return "No Matches found"
            
        
            
    elif int(option)==3:
        result=searchbasedondate(text)
        if(result):
            return  render_template('Results.html')
        else:
            return "No Matches found"
            
    
    elif int(option)==4:
        result=searchbasedontypeoffile(text)
        if(result):
            return  render_template('Results.html')
        else:
            return "No Matches found"
            
    
    
    elif int(option)==5:
        result=searchbasedontypeoffile(text)
        if(result):
            return  render_template('Results.html')
        else:
            return "No Matches found"
            
@app.route('/results')
def results():
    render_template('Hello results are here')



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
                result+=';'+item
        with open(path+"/templates/Results.html",'w+') as f:
            f.write('<h1>SEARCH OUTPUT BASED ON THE FILENAME SPECIFIED</h1><br><br>')
            for item in match_files:
                x=item.split('\\')
                res=''
                for i in x:
                 res+='/'+i
                
                linkUrl = 'file://'+res
                linkText = '<a href="{}">{}</a><br>'.format(linkUrl,item)
                f.write(linkText)
                
                f.write('\n')
                
    return match_files
       
def pdfreadder(file):
    import PyPDF2
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    print (page_content.encode('utf-8' ,error='ignore'))
    return page_content


       

def searchbasedonfilecontent(pattern,filename):
    
    
    count_files=searchbasedonfilename(filename)
    #count_files=result.split(";")
    
    flag1=0
    

    if len(count_files):
        with codecs.open(path+"/temp.txt", "w+",encoding='utf-8', errors='ignore') as fdata:
               
               for file in count_files:
                   fdata.write("SEARCHING KEYWORD IN  FILE:{}\n".format(file))
                   if 'pdf' in file:
                    content=pdfreadder(file)
                    content=content.split(";")
                    with codecs.open(path+"/tem.txt", "w+",encoding='utf-8', errors='ignore') as f1:
                     for ele in content:
                          f1.write(ele)
                          f1.write('\n')
                     file=path+'/tem.txt'
                   
                   with codecs.open(file, 'r',encoding='utf-8', errors='ignore') as f2:
                       for line in f2.readlines():
                           match=re.search(pattern,line)
                           if(match):
                               flag1=1
                               fdata.write(line)
                       
        if(flag1):
            with open(path+"/templates/Results.html",'w+') as f2:
                    with codecs.open(path+"/temp.txt", "r+",encoding='utf-8', errors='ignore') as fdata:
                
                        f2.write('<h1>SEARCH OUTPUT BASED ON FILE CONTENT </h1><br><br>')
                        for line in fdata:
                            f2.write('<p>{}</p>'.format(line))
                            f2.write('\n')
                        
                    
            return 1

    else: 
        
        return 'File not found'


def searchbasedondate(pattern):
    match_files=[]
    result=''
    flag=0
    
    for root,dirs,files in os.walk(path):
        for directory in dirs:
            path1=os.path.join(root,directory)
            ctime=datetime.fromtimestamp(os.path.getctime(path1)).strftime('%d-%m-%Y')
            mtime=os.stat(path1).st_mtime
            
            if (ctime==pattern) or (mtime==pattern):
                flag=1
                match_files.append(path1)
           
        for name in files:
            path2=os.path.join(root,name)
            ctime=datetime.fromtimestamp(os.path.getctime(path2)).strftime('%d-%m-%Y')
            mtime=os.stat(path2).st_mtime
            
            if (ctime==pattern) or (mtime==pattern):
                flag=1
                match_files.append(path1)
                
   
    if(flag):
        
        for item in match_files:
                result+=';'+item
        with open(path+"/templates/Results.html",'w+') as f:
            f.write('<h1>SEARCH OUTPUT BASED ON CREATION/MODIFICATION DATE </h1><br><br>')
            for item in match_files:
                x=item.split('\\')
                res=''
                for i in x:
                 res+='/'+i
                
                linkUrl = 'file://'+res
                linkText = '<a href="{{ url_for(results) }}">{}</a><br>'.format(item)
                f.write(linkText)
                
                f.write('\n')
                
    return result
           
             
                
def searchbasedonsize(pattern):
    match_files=[]
    result=''
    flag=0
    
    for root,dirs,files in os.walk(path):
        for directory in dirs:
            path1=os.path.join(root,directory)
            size=os.path.getsize(directory)
            if (size==pattern):
                #print("Folder is created on date {0}".format(directory))
                flag=1
                match_files.append(path1)
           
        for name in files:
            path1=os.path.join(root,name)
            size=os.path.getsize(path1)
            if (size==pattern):
                #print("Folder is created on date {0}".format(path1))
                match_files.append(path1)
                flag=1
    if(flag):
        
        for item in match_files:
                result+=';'+item
        with open(path+"/templates/Results.html",'w+') as f:
            f.write('<h1>SEARCH OUTPUT BASED ON CREATION/MODIFICATION DATE </h1><br><br>')
            for item in match_files:
                x=item.split('\\')
                res=''
                for i in x:
                 res+='/'+i
                
                linkUrl = 'file://'+res
                linkText = '<a href="{}">{}</a><br>'.format(linkUrl,item)
                f.write(linkText)
                
                f.write('\n')
                
    return result
           
			
def searchbasedontypeoffile(pattern):
    match_files=[]
    result=''
    flag=0
        
    for root,dirs,files in os.walk(path):
        for f1 in files:
            
            ext=os.path.splitext(f1)[-1].lower()
            path1=os.path.join(root,f1)
            
            if ext.endswith(pattern) or f1.endswith(pattern):
                flag=1
                match_files.append(path1)
            
    if(flag):
        
        for item in match_files:
                result+=';'+item
        with open(path+"/templates/Results.html",'w+') as f:
            f.write('<h1>SEARCH OUTPUT BASED ON THE TYPE OF FILE SPECIFIED</h1><br><br>')
            for item in match_files:
                x=item.split('\\')
                res=''
                for i in x:
                 res+='/'+i
                
                linkUrl = 'file://'+res
                linkText = '<a href="{{ url_for(results) }}">{}</a><br>'.format(item)
                f.write(linkText)
                
                f.write('\n')
                
    return result
            
if __name__ == '__main__':
    app.run(debug=True)




 

