#!/usr/bin/env python

# file_extractor
import sys

class FileHandler():
    def __init__(self, **kwargs):
        self.file = kwargs.get('file')

    def verify(self):
        print('TODO')
        


    def parse_file_name(self):
        print(len(self.file)) 


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
            # Add keyword arg here for **kwargs 
        )



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