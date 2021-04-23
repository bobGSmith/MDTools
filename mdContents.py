# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:38:31 2021

@author: bobby
"""
# ADD TABLE OF CONTENTS TO MARKDOWN FILES # 

import sys

test = sys.argv[1]
overwrite = input("overwrite original file?  [y/n]\n")
if overwrite in ["y","Y","yes","Yes","YES"]:
    newfile = test
else:
    newfile = input("enter new path/filename:\n")


#test = "TestMD1_output.md"
#newfile = "TestMD1_output_remove.md"

continue_script = True

with open(test, "r") as infile: 
    lines = infile.readlines()
  
if '## Table of Contents\n' in lines:
    print("clearing current table of contents")
    cont_start = lines.index('## Table of Contents\n')
    endfound = False
    for i in range(cont_start, len(lines)):
        if lines[i] == "\n":
            cont_end = i
            endfound = True
            break
    if endfound:
        del lines[cont_start:cont_end+1]
        import re
        for i in range(len(lines)):
            if lines[i][:3] == "## ":
                lines[i] = re.sub(r'<a name = (.*)</a>', "", lines[i])
    else:
        print("Warning: ## Table of Contents section must end with a empty line after last item")
        input("Hit return to terminate session")
        continue_script = False
        
if continue_script: 
    section_count = 1
    title = False
    contents = []
    for i in range(len(lines)):
        if lines[i][:3] == "## ":
            print(lines[i]) # debug 
            contents.append("{}. [{}](#{})\n".format(section_count, (lines[i][3:]).replace("\n",""), section_count))
            lines[i] = (lines[i]).replace("\n"," ") + " <a name = {}></a>\n".format(section_count)
            section_count += 1
        elif lines[i][:2] == "# ":
            title = True
            title_index = i
    
    cont = "y"        
    if title: 
        if title_index != 0:
            cont = input('''Warning: detected single "#" title not on first line. This 
                         doc may be incorrectly formatted. Please use "# your_title" 
                         on the first line for the Document title, and use double hash
                         ("## your_section") for the section or chapter headings.\n
                         Continue anyway >  [y/n]\n''')
    
    
    if cont in ["y","Y","yes","Yes","YES"]:
            
        with open(newfile, "w") as outfile:
            if title:
                outfile.write(lines[title_index])
                outfile.write("## Table of Contents\n")
                outfile.writelines(contents)
                outfile.write("\n")
                outfile.writelines(lines[title_index + 1:])
            else:
                outfile.write("## Table of Contents\n")
                outfile.writelines(contents)
                outfile.write("\n")
                outfile.writelines(lines)
            
    else:
        input("Hit return to terminate session")
                
                
