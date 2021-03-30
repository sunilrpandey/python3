from PyPDF2 import PdfFileReader
import re

with open('3.pdf','rb') as f:
    rdr = PdfFileReader(f)
    num_page =  rdr.getNumPages()
    print("Num Page : ", num_page)
    target_page_num = 1
    page_obj = rdr.getPage(target_page_num-1)
    print("Page Info : \n")
    print(page_obj)
    print("\n\n\nPage Content : \n")
    #print(page_obj.extractText())
    #print(f.write())
    #print(re.split('\n\d+.+[ \t][a-zA-Z].+\n',page_content))
    
