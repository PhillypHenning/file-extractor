#!/usr/bin/env python

# file_extractor
import sys

class FileHandler():
    def __init__(self, **kwargs):
        self.file = kwargs.get('file')

    def verify(self):
        print('TODO')
        


    def parse_file_name(self):
        print('TODO')


    def byte_counter(self):
        print('TODO')


def main(args):
    new_dict = dict()
    for arg in args:
        key = arg.split('=')[0]
        value = arg.split('=')[1]
        new_dict[key] = value


def __name__ == '__main__' :
    main(sys.argv[1:])