# MarkDown Tools 
## Table of Contents
1. [Install ](#1)
2. [TOC](#2)
3. [CSV2MD ](#3)
4. [MultiTOC ](#4)
5. [Dev To Do ](#5)


Add tables of contents for repositores or single files, insert abbreviations, convert csv tables to markdown. 


## Install <a name = 1></a>

```
pip install git+https://github.com/bobGSmith/MDTools@master
```

## TOC<a name = 2></a>

The TOC for this README.md was created with MDTools.TOC

```
python3 -m MDTools.TOC path_to_file.md
```

This adds a Table of Contents to a markdown file below the title (title ahs a single "#"), if there is a title. Sections titled with heading 2 "##" will be included in the contents table. Sub headings (e.g. "###") wont be included in the contents page. It doesn't like it if you use heading 1 "#" for section headings.

To update a pre existing TOC just re run it.

## CSV2MD <a name = 3></a>
Converts csv files to markdown. Also searches markdown documents for embedded csv tables tagged with <csv> </csv>. 

Enter the path to the md file as the argument in terminal. 
	
'''
python3 -m MDTools.CSV2MD path_to_file
'''

tables must have the csv tags on separate lines and have the same number of commas on each line (no comma needed on last item - may change this) 

### Example embedded CSV within md

	<csv>  
	name, height, weight, type   	
	bob, 172, 75, human   
	bear, 50, 30, dog   
	jaws, 1, 0.1, goldfish   
	</csv>  

### Convert .csv file
just enter the path to the csv file as the argument and it will do the rest (use .csv file extension if it is a .csv file)
	>python mdCSV.py "/path/your_file.csv"

## MultiTOC <a name = 4></a>
This script and module takes a directory filled with markdown files, and sub-directoreis filled with markdown/ further subdirectores. It uses this to create a table of contents for the root directory. Sub drectories will be indented like chapters in the table of contents. It has the option to add the ToC to a README.md file or to create a new table_of_contents.md file. 

```
python3 -m MDTools.MultiTOC path_to_directory
```

It can also be used to update a pre-existing TOC after you have edited some filenames, deleted files or added more.

### Example MultiTOC output 
Here is an example of what a ToC would might like for a dir contianing 3 markdowns and a sub-directory contiaing 2 further markdowns. 

 
* a markdown
* another
* markdowns about a topic:
  * details about the topic
  * more details
* one more markdown

## Dev To Do <a name = 5></a>
Made a lot of this early on when  was learning to program. Needs to be reworked a little and some scripts need to be re written as functions that could be imported.  
