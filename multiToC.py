'''
MultiToC - Take a directory of markdown files and sub-directoreis of more markdowns and create a table of contents. 

## Quickstart  
in terminal run
```
python multiToC.py "path_to_notes_dir"
```
Can also import this as a module to use the functions

```
import multiToC
```

'''

import sys 
import os 

def relative_link (name, path, replace_underscores = True) :
    '''Takes name and path and creates a markdown format link
    
    Args
    -------
    name : str
        The name for the link (e.g. "my_markdown")
    path : str
        The relative path to the file (e.g. "my_folder/my_markdown.md")
    replace_underscores : bool
        If true name "my_markdown" would become "my markdown"
    '''
    if replace_underscores:
        return "[" + name.replace("_"," ") + "](" + path + ")"
    else:
        return "[" + name + "](" + path + ")"
    
def dir_to_toc (path, root_dir, indentation_level = 0) :
    '''Recursive function that creates a table of contents indented by heading level'''
    ToC = ""
    indent = "  " * indentation_level
    files = os.listdir(path) 
    relative_path = path.replace(root_dir, "")
    names = [f.replace(".md","") for f in files]
    links = [relative_path + "/" + f for f in files]
    full_paths = [path + "/" + f for f in files]
    for i in range(len(links)):
        if not ".md" in links[i]:
            try:
                ToC += indent + "* " + names[i].replace("_"," ") + ":\n"
                ToC += dir_to_toc(full_paths[i], root_dir, indentation_level + 1)
            except:
                print("Error related to file: ", links[i])
        else:
            ToC += (indent + "* " + relative_link(names[i], links[i]) + "\n")
    return ToC   

def strip_toc (path) :
    no_toc = ""
    with open(path, "r") as infile:
        ToC = False
        for l in infile.readlines():
            if "## Contents" in l:
                ToC = True
            if not ToC:
                no_toc += l
            if ToC and not "## Contents" in l and not "*" in l and not "\n" == l:
                ToC = False
                no_toc += l
    with open(path, "w") as outfile: 
        outfile.write(no_toc)   
        if not no_toc[-1] == "\n":
            outfile.write("\n") 
    
if __name__ == '__main__':
    path = sys.argv[1] 
    files_main = os.listdir(path)
    add_to_readme = input("Add ToC to README.md? (y/n) >  ")
    ToC = dir_to_toc(path, path, 0)
    if add_to_readme.lower() in ["y", "yes", "ye", "yea", "yeah"]:
        if "README.md" in os.listdir(path):
            strip_toc(path + "/" + "README.md")
            with open(path + "/" + "README.md", "a") as infile: 
                infile.write("## Contents    \n")
                infile.write(ToC)
        else:
            with open(path + "/" + "README.md", "w") as infile: 
                infile.write("# README    \n## Contents    \n")
                infile.write(ToC)
    else:
        with open(path + "/" + "Table_of_contents.md", "w") as infile: 
            infile.write("# README    \n## Contents    \n")
            infile.write(ToC)
            
            
        