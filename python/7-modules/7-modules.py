#!/usr/bin/env python3

'''
Modules

Includes: Module Management

-> The main modules of Python are: logging, datetime, os, sys, threading, yaml, json 
-> Any script can be imported as a module, which means you can create your own!
'''

#Add an alias to an import
import custom as m

#Import a single function, object
from custom import welcome

#Importing a function from within folders (package)
'''
- You should leverage this for your project to make it modular
- com.revature.model -> your classes
- com.revature.io -> your file io
- com.revature.console -> your console printing (controller)
- Be creative!
'''
from com.revature.package.inpackage import my_function

def main():
    #Calling functions from the module object
    m.welcome()
    m.tothe()
    m.module()

    #Since we imported the function, we don't need to call the module object
    welcome()

    #Calling function imported from package
    my_function()

if __name__ == '__main__':
    main()