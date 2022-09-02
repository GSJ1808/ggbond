from dataclasses import replace
import os
import re
from unicodedata import category 

g = os.walk(r".")  

for path,dir_list,file_list in g:  
    for file_name in file_list: 
        if os.path.splitext(file_name)[-1] == ".md": 
            with open(file_name, 'r+') as f:
                lines = f.read() ##Assume the sample file has 3 lines
                title = lines.split('\n', 1)[0].split('# ',1)[1]
                print(title)
                categories = lines.split('\n', 5)[2].split('Tags: ',1)[1]
                print(categories)       
                f.seek(0, 0)
                f.write('---\ntitle: ' + title + '\ncategories: ' + 'Tree' + '\n---\n'+lines)

