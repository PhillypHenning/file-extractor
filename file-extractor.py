#!/usr/bin/env python

# file_extractor
import sys
import os.path
import hashlib

class FileHandler():
    def __init__(self, **kwargs):
        self.file = kwargs.get('file')
        self.fh = open(self.file)


    def verify(self):
        if not os.path.isfile(self.file) :
            print('File not found, run file-extractor.py help for usage')
            exit()
        

    def parse_filename(self):
        out_file = ""
        for c in reversed(self.file) :
            if c == '/' :
                break
            
            else :
                out_file += c

        self.filename = out_file[::-1] 


    def byte_counter(self):
        self.file_bytes = os.path.getsize(self.file)


    def sha1_digest(self) :
        sha_file = hashlib.sha1()
        with open(self.file) as f :
            sha_file.update(f.readline())
        self.sha_hex = sha_file.hexdigest()
        

    def md5_digest(self) :
        md5_file = hashlib.md5()
        with open(self.file) as f:
            md5_file.update(f.readline())
        self.md5_hex = md5_file.hexdigest()


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
        fh.parse_filename()
        fh.byte_counter()
        fh.sha1_digest()

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