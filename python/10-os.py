#!/usr/bin/env python3

'''
OS

Includes: Invoking the OS, Receiving arguments

-> Python can invoke the operating system
-> You can call any command existing in the current running OS
-> You can also transform your Python scripts into something that looks like a command!
-> If you want interoperability, you should use the os module functions, which will
call the right system commands depending on which OS is this script running

We will focus in invoking Unix native functions
(Review IO example for os module functions)
'''

import os
import sys
import subprocess

EXPRESSION_FLAG = '-e'
FILE_FLAG = '-f'

def main():
    '''
    -> The first argument of the program is always the script name
    -> Hence your first argument is in the first index
    '''
    if len(sys.argv) > 1:
        #If user is asking for help, show usage and terminate program
        if('--help' in sys.argv):
            print('Usage: ./10-os.py -e <expression> -f <datafile>')
            return
        
        #If it's not help then we need to extract the parameters
        if(EXPRESSION_FLAG, FILE_FLAG in sys.argv):
            #Extract expression parameter
            flag_index = sys.argv.index(EXPRESSION_FLAG)
            expression = sys.argv[flag_index + 1]

            #Extract file location parameter
            flag_index = sys.argv.index(FILE_FLAG)
            file_location = sys.argv[flag_index + 1]

            #Print a message showing parameters
            print('Performing grep ' + expression + ' ' + file_location)
        else:
            raise ValueError('Invalid flags detected')

        grep_command = 'grep {} {}'.format(expression, file_location)

        #We can invoke the operating system now
        input('Invoking the OS directly...')
        os.system(grep_command)

        #If we wanted to process the output, we would have to use the subprocess module
        input('Invoking the OS and processing internally...')
        process = subprocess.Popen(grep_command, shell=True, stdout=subprocess.PIPE)

        #We will receive bytes, so we need to decode into a string and then split to created list
        output = process.stdout.read().decode(encoding='UTF-8').split('\n')
        for line in output:
            print(line)
    else:
        print('No arguments detected. Use --help')

if __name__ == '__main__':
    main()