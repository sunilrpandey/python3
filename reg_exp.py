#match matches if it starts with pattern, search matches whole string


import re


nums = '''
12+23+34, 
80*23*34, 
90-23-34,
122-14-1234,
2c*23*34, 
3M-23-34,
8M-2P-34,
*M-26-34,
'''

quote = "Honesty is the best policy"
emails = '''
FirstKLast@email.com
first.last@school.edu
first.12.last@office.net
'''

def demo_verify_num_patterns():
    print("all delim")
    pat = re.compile(r'\d\d.\d\d.\d\d')
    matches = pat.finditer(nums)

    for match in matches:
        print(match)

    print("only delim : +*")
    pat = re.compile(r'\d\d[+*]\d\d[+*]\d\d')
    matches = pat.finditer(nums)

    for match in matches:
        print(match)
    
    print("First part 80 or 90, all delims")
    pat = re.compile(r'[89]0.\d\d.\d\d')
    matches = pat.finditer(nums)

    for match in matches:
        print(match)

    print("First part num_alpha, all delims")
    pat = re.compile(r'[1-5][a-zA-Z].\d\d.\d\d')
    matches = pat.finditer(nums)

    for match in matches:
        print(match)
    
    print("Not num_alpha, all delims")
    pat = re.compile(r'[^1-5][a-zA-Z].\d\d.\d\d')
    matches = pat.finditer(nums)

    for match in matches:
        print(match)
        

def demo_match_saluations():
    saluations = '''
    Mr Fox
    Mr. fox
    Mrs Fox
    Mr B
    '''
    print("Demo: Mr or Mr.")
    pat = re.compile(r'Mr\.?') # ? after char  0 or 1
    matches = pat.finditer(saluations)
    for m in matches:
        print(m)

    print("Demo: Any with name starts with capital letter")
    # \w word char and + means 1 or many so will not shw Mr B while * means 0 or many 
    # and will show Mr B
    pat = re.compile(r'Mr\.?s?\s[a-zA-Z]\w+') 
    matches = pat.finditer(saluations)
    for m in matches:
        print(m)

def demo_raw_string():
    print("Demo : demo_raw_string()")
    print("For raw string prepend string with `r`")
    print('\tTab')
    print(r'\tTab')


def demo_finditer():
    text = "abc345sdfajsdabc"
    pattern = re.compile(r'abc')
    matches = pattern.finditer(text)
    for match in matches:
        print(match)

def demo_check_patterns():
    pattern = re.compile(r'\d\d.\d\d.\d\d') 
    #re.compile(r'\d\d.\d\d.\d\d') 
    with  open('file.txt','r', encoding='utf-8') as f:
        contents = f.read()
        matches = pattern.finditer(contents)
        for match in matches:
            print(match)
            print(match.span())


def demo_regular_expression():
    demo_raw_string()

def demo_match_and_search_method():
    print("Demo : demo_match_and_earch_method()")
    print("Match matches only if it start with a pattern, similar to ^pattern")
    pattern = re.compile(r'Honesty',re.I) # flag to ignore case
    res = pattern.match(quote)
    print("Match Method : ", res)

    # wont match
    pattern = re.compile(r'policy') 
    res = pattern.match(quote)
    print("Match Method : ", res)

    # search matches whole text (quote)
    res = pattern.search(quote)
    print("Search Method : ", res)

def mimick_match_method_using_findall():
    pattern = re.compile(r'^Honesty',re.I) # flag to ignore case
    res = pattern.findall(quote)
    for out in res:
        print("Mimicking match Method : ", out)

def demo_check_urls():
    urls = '''
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    '''

    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')   
    matches = pattern.finditer(urls)  
    for match in matches:   
        print(match.group(0)) # print whole match  
        print(match.group(1)) # 1 onward prints group of the matches

    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')     
    sub_urls = pattern.sub(r'\0\1\2\3', urls)
    print(sub_urls)

if __name__ == "__main__":
    #demo_regular_expression()
    #demo_match_and_search_method()
    #demo_verify_num_patterns()
    #demo_match_saluations()
    #demo_finditer()
    #demo_check_patterns()
    #mimick_match_method_using_findall()
    demo_check_urls()