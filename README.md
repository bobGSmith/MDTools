# MarkDown Tools 

## About
I started writing and making notes in markdown recently, so I made a python script that will add and update a tables of contents to a markdown document. It may never happen, but I if I make any more markdown related stuff I'll add it here. 

## mdContents.py
### Input document format
Adds a Table of Contents to a markdown file below the title (formatted using heading one "#"), if there is a title. Sections titled with heading 2 "##" will be included in the contents table. Example format below:

> # Your title
> ## Section 1 
> writing about stuff.
> ## Section 1 
> etc.. 

*sub headings (e.g. "###") wont be included in the contents page. It doesn't like it if you use heading 1 "#" for section headings.*

### Quick start
Run the script from terminal, it takes one arg which is the path to your md file:
	$ python mdContents.py /path/your_file.md 

 



