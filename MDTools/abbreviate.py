"""Markdown Abbreviator 

This script can be run from terminal with three args (and fourth optional):
    path : str
        The path to a .md file. 
    phrase : str 
        The phrase to be abbreviated (e.g. Muscle protein synthesis).
    abbr : str  
        The abbreviation of the phrase (e.g. MPS). 
    out : str 
        Optional argument for output path. By default, original file will be replaced. 
"""

import sys
from .read_write import import_file, write_file


def abbreviate (infile, phrase, abbr) : 
    outfile = infile.replace(phrase, abbr)
    return outfile.replace(abbr, f'{phrase} ({abbr})', 1)
    
def main () :
    outpath = sys.argv[4] if len(sys.argv) == 5 else sys.argv[1]
    print(f'File: {sys.argv[1]}\nPhrase: {sys.argv[2]}\nAbbreviation: {sys.argv[3]}\nOutput: {outpath}')
    infile = import_file (sys.argv[1])
    outfile = abbreviate(infile, sys.argv[2], sys.argv[3])
    write_file(outpath, outfile)
        
if __name__ == '__main__': 
    main () 
    
    