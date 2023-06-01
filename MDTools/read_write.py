def import_file (path) : 
    """Imports text files"""
    return (open (path, 'r')).read() 
    
def write_file (outpath, text) :
    (open(outpath, 'w')).write(text)       