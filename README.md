# MarkDown Tools 
## Table of Contents
1. [About  ](#1)
2. [mdContents.py  ](#2)
3. [Why](#3)


## About    <a name = 1></a>
I started writing and making notes in markdown recently, so I made a python script that will add and update a tables of contents to a markdown document. It may never happen, but I if I make any more markdown related stuff I'll add it here. 

## mdContents.py    <a name = 2></a>
### Input document format
Adds a Table of Contents to a markdown file below the title (formatted using heading one "#"), if there is a title. Sections titled with heading 2 "##" will be included in the contents table. Sub headings (e.g. "###") wont be included in the contents page. It doesn't like it if you use heading 1 "#" for section headings.

### Quick start
Run the script from terminal, it takes one arg which is the path to your md file:
	$ python mdContents.py /path/your_file.md 

## Why  <a name = 3></a>
I also need to learn how to use github properly for some other projects, so I'm testing a few things here. Also, the Table of Contents section for this README.md was made with the mdContents.py script :)



