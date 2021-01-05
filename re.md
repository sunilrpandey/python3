# Regular Expression

Metacharacters need to be taken care

    . ^$*+?{}[]\|()

Need to escape these using '\\' e.g. \\.

Raw String
> print(r'\tTab)

re compile/finditer
```py
text = "abc345sdfajsdabc"
example = "Honesty is the best policy"
pattern = re.compile(r'abc')
#pattern = re.compile(r'.')
matches = pattern.finditer(text)
for match in matches:
    print(match)
```
and output would be 
```
<_sre.SRE_Match object; span=(0, 3), match='abc'>
<_sre.SRE_Match object; span=(13, 16), match='abc'>
```
. - Any charater except new line  
\d digit 0 -9  
\D No digit 0 -9  
\w - word characters a-z,A-Z 0-9, _
\W - not a word character  
\s - white space(spae tab newline)  
\S - not whitespace  

\b - word boundary    # pattern = re.compile(r'\bHonesty')
\B - not word bound  
^ - start of string  # pattern = re.compile(r'^Honesty')
$ - end of the string # pattern = re.compile(r'policy$')

Match 12-23-34 # re.compile(r'\d\d.\d\d.\d\d') # . means any character except newline  
re.compile(r'\d\d[-.]\d\d[-.]\d\d') # . or - using characyter set, matches only one character  
re.compile(r'[89]00[-.]\d\d[-.]\d\d') start with 800 or 900  
re.compile(r'1-5')  
re.compile(r'[a-zA-Z]')  
re.compile(r'[^a-zA-Z]')   # not a alphabet
re.compile(r'[^b]at')   # all 'at' but not bat   

re.compile(r'\d\d.\d\d.\d\d\d') 

Quantifier  
\* - 0 or more  
\+ - 1 or more  
? - 0 or One  
{3} - exact number  
{3,4} - Range(minium, maximum)

re.compile(r'\d\d.\d\d.\d\d\d') is same as   
re.compile(r'\d{2}.\d{2}.\d{3}') 

re.compile(r'Mr\.?') # after char  
re.compile(r'Mr\.?\s[A-Z]\w+') # Mr. Syha  
re.compile(r'Mr\.?\s[A-Z]\w*') # Mr. S    


Group  
Names    
re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # Mr. S    
re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # Mr. S  

Email   
re.compile(r'[a-zA-Z]+@[a-z]+\.com') # for emails  having alphabets only      
re.compile(r'[a-zA-Z0-9.-_]+@[a-z]+\.(com|edu|net)') # for emails  having alphabets only  

generic pattern for email address  
re.compile(r'[a-zA-Z0-9+.-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-0-.]+') # for emails  having alphabets only



urls  
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')   
matches = pattern.finditer(text_to_search)  
for match in matches   
print match.group(0) // print whole match  
print match.group(1) // 1 onward prints group of the matches

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')     
sub_urls = pattern.sub(r'\2\3', urls)
print(sub_urls)

finditer - including infos too    
find all - only matches, if group matches returns groups

match - just returns first match or none not iter,  matches at the begining only  
search - search entire string  

Flags  

re.compile(r'start',re.IGNORECASE)
re.compile(r'start',re.I)

ref  
https://www.youtube.com/watch?v=K8L6KVGG-7o
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions





