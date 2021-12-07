# MarkDown Tools 
## Table of Contents
1. [About ](#1)
2. [Contents table generator (mdToC.py)](#2)
3. [CSV to Markdown (mdCSV.py) ](#3)
4. [multiToC](#4)


## About <a name = 1></a>
So far we have a markdown Table of contents generator and a csv to markdown converter :)

## Contents table generator (mdToC.py)<a name = 2></a>
### Input document format
Adds a Table of Contents to a markdown file below the title (formatted using heading one "#"), if there is a title. Sections titled with heading 2 "##" will be included in the contents table. Sub headings (e.g. "###") wont be included in the contents page. It doesn't like it if you use heading 1 "#" for section headings.

### Quick start
Run the script from terminal, it takes one argument, which is the path to your md file. Should look like this:

	>python mdToC.py "/path/your_file.md" 

This will then ask you if you want to overwrite the original or make a new markdown file. It will then output the file with a table of contents added (it will look like the table of contents on this README.md file)

## CSV to Markdown (mdCSV.py) <a name = 3></a>
Converts csv files to markdown. Also searches markdown documents for embedded csv tables tagged with <csv> </csv>. 

### Embedded csv format 
Enter the path to the md file as the argument in terminal. 
	>python mdCSV.py "/path/your_file.md" 
tables must have the csv tags on separate lines and have the same number of commas on each line (no comma needed on last item - may change this) 
#### Example

	<csv>  
	name, height, weight, type   	
	bob, 172, 75, human   
	bear, 50, 30, dog   
	jaws, 1, 0.1, goldfish   
	</csv>  

### Convert .csv file
just enter the path to the csv file as the argument and it will do the rest (use .csv file extension if it is a .csv file)
	>python mdCSV.py "/path/your_file.csv"

## multiToC<a name = 4></a>
This script and module takes a directory filled with markdown files, and sub-directoreis filled with markdown/ further subdirectores. It uses this to create a table of contents for the root directory. Sub drectories will be indented like chapters in the table of contents. It has the option to add the ToC to a README.md file or to create a new table_of_contents.md file. 

```
python multiToC.py "path_to_dir"
```

### Example output 
Here is an example of what a ToC would might like for a dir contianing 3 markdowns and a sub-directory contiaing 2 further markdowns. 

 
* a markdown
* another
* markdowns about a topic:
  * details about the topic
  * more details
* one more markdown

