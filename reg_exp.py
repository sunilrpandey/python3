import re
#print('\tTab')
#print(r'\tTab')
#
#text = "abc345sdfajsdabc"
#pattern = re.compile(r'abc')
#matches = pattern.finditer(text)
#for match in matches:
#    print(match)

pattern = re.compile(r'\d\d.\d\d.\d\d')
with  open('file.txt','r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.findall(contents)
    for match in matches:
        print(match)