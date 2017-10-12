#!/usr/bin/env python

# file_extractor
import sys

class FileHandler():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def main(args):
    new_dict = dict()
    for arg in args:
        key = arg.split('=')[0]
        value = arg.split('=')[1]
        new_dict[key] = value


def __name__ == '__main__' :
    main(sys.argv[1:])