#!/usr/bin/env python

# file_extractor
import sys
import os.path

class FileHandler():
    def __init__(self, **kwargs):
        self.file = kwargs.get('file')


    def verify(self):
        if not os.path.isfile(self.file) :
            print('File not found, run file-extractor.py help for usage')
            exit()
        

    def parse_file_name(self):
        out_file = ""
        for c in reversed(self.file) :
            print(c)
            if c == '/' :
                break
            
            else :
                out_file += c

        self.filename = out_file[::-1] 


    def byte_counter(self):
        print('TODO')


def main(args):
    """
    Need        Command            Usage
    Start       run                file-extractor.py <PathtoFile> run
    """
    
    if (len(args) > 2):
        print('Incorrect amount of arguements, run file-extractor.py help for usage')
        exit()
    
    if(args[1] == 'run'):
        fh = FileHandler(
            **{'file' : args[0], })

        fh.verify()
        fh.parse_file_name()

    else:
        print(
            """
            Need        Command            Usage
            Start       run                file-extractor.py <PathtoFile> run
            """
        )
        exit()


if __name__ == '__main__' :
    main(sys.argv[1:])