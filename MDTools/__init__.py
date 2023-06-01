'''MDTools

A collection of functions/ scripts for working with markdown documents 

scripts 
=======
scripts can be called with the following command: 

> python3 -m MDTools.SCRIPT_NAME ARGS 

The following scripts are included: 
* MDTools.abbreviate : finds first instance of a phrase that you want to 
  abbreviate, adds the abbreviation behind it in brackets, and then replaces all future instances. 
* MDTools.CSV2MD: converts csv format to markdown format tables 
* MDTools.MultiTOC: takes a directory of markdown files and subdirectories
  containing more markdown files, then creates a hyperlinked table of contents in a 
  readme.me at the root of the dir
* MDTools.TOC: Adds a table of contents to a single markdown document at the top (with hyperlinks) 
'''
import sys 
if len(sys.argv) == 1:
  print(__doc__)

