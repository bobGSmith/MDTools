# -*- coding: utf-8 -*-
"""

@author: Bobby (ovrhuman)
"""

import sys

proceed = input("""
===============================
| MARKDOWN CSV - Instructions |
===============================
                            
This script converts .csv files to markdown format, and also finds tables 
within markdown files which have been tagged with <csv>. So, you can place 
a table anywhere in your doc, formatted like this: 

<csv>
name, height, weight, type
bob, 172, 75, human
bear, 50, 30, dog
jaws, 1, 0.1, goldfish
</csv>

csv tags are on separate lines, separate values by comma and have the 
same number of commas in each row (even if no value present).

If converting a .csv file to markdown table, no adjustment necessary. 
Just make sure input markdown files have .md and csv files have .csv 


Continue [y/n]  >>
\n""")

if proceed.lower() in ["y","yes"]:
    test = sys.argv[1]

    overwrite = input("overwrite original file?  [y/n]\n")
    if overwrite in ["y","Y","yes","Yes","YES"]:
        newfile = test
    else:
        newfile = input("enter new path/filename:\n")
    

    #test = "FL_insurance_sample.csv"
    #newfile = test
    
    
    with open(test, "r") as infile:
        lines = infile.readlines()
    
    cols = None
    row = 0   
    error = False
    new_lines = []
    
    if test[-4:].lower() == ".csv":
        table = True
        csv = True
    else:
        table = False
        csv = False
    
    
    for i in range(len(lines)):
        if not table:
            if "<csv>" in lines[i]:
                table = True 
                new_lines.append("  \n")
            elif "<csv+>" in lines[i]:
                table = True
                row = 1; cols = (lines[i+1].count(",") + 1)
            else:
                new_lines.append(lines[i])
        elif table:
            if "</csv>" in lines[i] or "</csv+>" in lines[i]:
                new_lines.append("  \n")
                table = False
                row = 0
                cols = 0
            elif row == 0:
                cols = (lines[i].count(",") + 1)
                new_lines.append("|" + (lines[i].replace(",","|")).replace("\n","|\n"))
                new_lines.append(("|:--"*cols)+"|\n")
                row += 1 
            else:
                if cols != (lines[i].count(",") + 1):
                    error = True
                    break
                else:
                    new_lines.append("|" + (lines[i].replace(",","|")).replace("\n","|\n"))
      
    
    
    if error:
        print("Error: all rows must be of equal length, empty fields can just be a space or NA, but they need the correct number of commas")         
     
    elif table and not csv:
        print("""Error: a table starting with <csv> did not end with </csv>. 
              Make sure tables are in the following format:
                  
                  <csv>
                  col1, col2, col3, col4
                  item1, item2, item3, item4
                  item5, item6, item7, item8
                  </csv>
                  """   )   
                 

    else: 
        with open(newfile.replace(".csv",".md"),"w") as outfile:
            outfile.writelines(new_lines)