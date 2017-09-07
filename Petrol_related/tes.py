
import PyPDF2
pdf_file = open('C:\\Users\\rishi\\Desktop\\Search_Engine\\MDG - AUTOMATION amendment.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content.encode('utf-8'))

 '''
    parser=argparse.ArgumentParser()
      
    
    parser.add_argument("Search_criteria",help="Specify the what based Search")
    parser.add_argument("pattern",help="search pattern")
    parser.add_argument("-o","--out",help="search option specific")
    args=parser.parse_args()
    
    print(args.Search_criteria)
    print(args.pattern)
     
    if int(args.Search_criteria)==1:
        result=searchbasedonfilename(args.pattern,sys.argv[3])
    elif int(args.Search_criteria)==2:
        result=searchbasedonfilecontent(args.pattern)
    elif int(args.Search_criteria)==3:
        result=searchbasedondate(args.pattern)
    elif int(args.Search_criteria)==4:
        result=searchbasedonsize(args.pattern)
    elif int(args.Search_criteria)==5:
        result=searchbasedontypeoffile(args.pattern)
    else:
        print("Search criteria range from 1-5")
    ''' 