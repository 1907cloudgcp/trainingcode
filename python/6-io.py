#!/usr/bin/env python3

'''
File IO

Includes: Using files, Basic directory manipulation, Standard input/output/error
'''

import os
import sys

def main():
    input('==== File Basics ====')
    print()
    demo_open()
    print()

    input('==== Directories ====')
    print()
    demo_dirs()
    print()

    input('==== Standard I/O ====')
    print()
    demo_io()

def demo_open():
    input('Writing initial lines')
    fileobject = open('test_file.txt', 'w')
    fileobject.write('one\ntwo\nthree')
    fileobject.close()

    #Use with so you don't have to manually close the resource
    input('Check directory contents again')
    with open('test_file.txt', 'r') as fff:
        result = fff.read()
        print(type(result))
        print('File contents:', result)

    input('Append and read from a file')
    with open('test_file.txt', 'a+') as f:
        f.write('\nanother line\nand another\none more')
        #Set the cursor to the start of the file
        f.seek(0)
        print('We got: {}'.format(f.read()))

    input('Delete the file...')
    os.remove('test_file.txt')

def demo_dirs():
    input('List directories')
    print(os.listdir())

    input('Create a directory')
    os.mkdir('testdir', mode=0o750)

    input('Create recursive directories')
    os.makedirs('testdir/second/third', exist_ok=True)

    input('Remove a single directory')
    os.rmdir('testdir/second/third')

    input('Remove all directories')
    os.removedirs('testdir/second')

def demo_io():
    input('Reading from stdin directly')
    print(sys.stdin.readline())

    input('Reading from stdin using input()')
    result = input('Type something: ')
    print(result)

    print('Printing to stdout with print()')
    print('Printing to stdout directly', file=sys.stdout)

    input('Writing to a file directly from user input')
    with open('test_io.txt', 'w') as f:
        print(input('Put something into test_io.txt: '), file=f)

    input('Print to stderr')
    print('Error!', file=sys.stderr)
    input()

if __name__ == '__main__':
    main()